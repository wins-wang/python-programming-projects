# I am not keen on distributing solutions to assignments.
# They inevitably end up shared with other students.
# Please be aware that it is an academic integrity violation to share this solution with others.
# If someone in the future copies from this solution and I can trace it back to you, I ***will*** retroactively fail you.
# This might very well results in the ***revoking*** of your degree.


from html.parser import HTMLParser
from urllib.request import urlopen,urljoin,urlparse,Request
import re
import timeit

base_url = "http://www.cdm.depaul.edu/"

class WebCrawler():
    'A Class to manage web sites cralwing and data extraction'

    def __init__(self,url):
        'default construtor'
        self.target_url = url.lower()
        self.max_visited_urls = 100000
        self.visited_urls = set() # initialize visited to an empty set
        self.total_word_counters = {}
        self.progress = 0 # progress counter for ease of tracking crawling progress

    def crawl(self,url=None):
        'a recursive web crawler that calls analyze() on every visited web page'
        if url == None: url = self.target_url

        # exit if maximum number of visted urls is reached
        if(len(self.visited_urls) >= self.max_visited_urls or url == ""): return

        self.progress += 1
        print(getExecutionTime(),self.progress,"Crawling:", url)

        # add the url to visited urls set without the http(s) protocol prefix
        self.visited_urls.add("".join(urlparse(url)[1:]))
        # get the list of urls in a webpage
        links = self.analyze(url)

        # recursively continue crawl from every link in links
        for link in links:
            # check the url without the http(s) protocol prefix and follow link only if not visited
            if "".join(urlparse(link)[1:]) not in self.visited_urls:
                try:
                    self.crawl(link)
                except Exception:
                    print("^^^\t\t\tFailed\t\t\t^^^")
                    pass # skip if failed to crawl

    def analyze(self,url):
        'Parse the page at the url and returns all the valid links found and counts the words found in the page'

        # set request header to avoid the HTTP error 418
        user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
        request = Request(url)
        request.add_header("User-Agent",user_agent)
        content = urlopen(request).read().decode()

        # obtain links in the web page
        with urlopen(request) as response:
            content = response.read().decode()
        collector = Collector(url)
        collector.feed(content)
        
        # get set of links
        urls = collector.getLinks()
        
        # compute word frequencies
        page_text = collector.getPageText()
        #print(page_text)
        clean_text = self.cleanText(page_text)
        #print(clean_text)
        self.updateWordsCount(clean_text)

        return urls

    def cleanText(self,text):
        'Cleans the text from any unwanted characters, spaces, symbols, or words'
        clean_text = text.lower()
        filter_remove = re.compile(r"(\r\n|\r|\n)|\. *|\||\-|\"|\“|\”|\'|\’|\`|\(|\)|\, |\&|\?|\@|\<|\>|\/|\\")
        clean_text = re.sub(filter_remove, ' ', clean_text)
        filter_words = re.compile(r"\b(and|the|to|of|in|a|for|at|is|are|be|on|no|not|with|will|or|that|then|them|pm|am|all|from|about|[^ ])\b")
        clean_text = re.sub(filter_words, '', clean_text)
        filter_replace_repeated_space = re.compile(r"\s+")
        clean_text = re.sub(filter_replace_repeated_space, ' ', clean_text)
        return clean_text.strip()

    def updateWordsCount(self,text):
        'Counts words in text and updates the global word counters'
        words = text.split()
        for word in words:
            word = word.strip()
            if word in self.total_word_counters:
                self.total_word_counters[word] += 1
            else:
                self.total_word_counters[word] = 1
    
    def printResults(self):
        'Print out the crawler results'
        # iterate over the sorted dictionary by word count from the high count to lower, showing only the top 25 words 
        for index, word in enumerate(sorted(self.total_word_counters.items(), key=lambda x:x[1], reverse=True)[:25],start=1):
            print("{:2}){:10} {:10}".format(index, word[1], word[0]))

        # show the total number of pages crawled
        print()
        print("Crawled {} pages.".format(len(self.visited_urls)))
        print()

class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self, url):
        'initializes parser, the url, and a list'
        HTMLParser.__init__(self)
        self.skip_tags = ["script","img","meta","link","style","iframe","br","input","noscript","menu","ie:menuitem","nav","form"] # tags expected not to have reasonable text content
        self.base_url = url
        self.links = set()
        self.page_text = ""
        self.current_tag = ""

    def handle_starttag(self, tag, attrs):
        'collects hyperlink URLs in their absolute format'
        
        self.current_tag = tag # track the current tag to be checked in handle_data
        
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # construct absolute URL
                    absolute = urljoin(self.base_url, attr[1].strip())
                    absolute = self.checkURL(absolute)
                    if absolute: # if url is ok collect HTTP URLs
                        self.links.add(absolute)

    def handle_data(self,data):
        'extract the textual content of the page'
        
        if self.current_tag in self.skip_tags:
            return # ensure that the current tag is of acceptable type, skip otherwise

        data = data.strip()
        if data:
            self.page_text += data
            self.page_text += "\n"

    def checkURL(self,url):
        'Make sure that the url is acceptable'

        # make url lowercase to make checks easier
        url = url.lower()

        # remove local page shortcuts
        url = url.split("#")[0] 

        # ensure url is http or https
        if urlparse(url)[0] not in ("http","https"): return ""

        # ensure url is restricted within the base url domain
        if urlparse(url)[1] != urlparse(self.base_url)[1]: return ""

        # ignore urls with certain tokens
        restricted_url_tokens = ["course-evaluations","action=download","mailto","@","<","\n"]
        for token in restricted_url_tokens:
            if url.find(token) > -1: return ""

        # ignore urls with certain extensions
        restricted_extensions = ["pdf","doc","docx","xls","xlsx","ppt","pptx","dmg","exe","zip","jpg"]
        for extension in restricted_extensions:
            if url.find("."+extension) > -1: return ""

        return url

    def getPageText(self):
        'returns the page text'
        return self.page_text

    def getLinks(self):
        'returns the page URLs in their absolute format'
        return self.links

#define global timer
timer_start = None

def main():
    'Main Function'
    global timer_start
    # set start time
    timer_start = timeit.default_timer()
    new_crawler = WebCrawler(base_url)
    try:
        print()
        new_crawler.crawl()
    except KeyboardInterrupt:
        # handle the keyboard interrupt with ctrl+c
        print("\n\nQuitting...\n\n")
    finally:
        print()

        # always show the results up to the current progress
        new_crawler.printResults()

        print(getExecutionTime(True))
        print()

def getExecutionTime(expanded=False):
    'Calculate execution time'
    timer_now = timeit.default_timer()
    execution_time = timer_now - timer_start
    hours, rem = divmod(execution_time, 3600)
    minutes, seconds = divmod(rem, 60)
    if(expanded):
        return("[ {:0>2} h : {:0>2} m : {:05.2f} s ]".format(int(hours),int(minutes),seconds))
    else:
        return("[{:0>2}:{:0>2}:{:05.2f}]".format(int(hours),int(minutes),seconds))

if __name__ == "__main__":
    main()
