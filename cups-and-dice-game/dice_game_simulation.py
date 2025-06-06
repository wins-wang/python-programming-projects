from dice_and_cup_classes  import Cup
import random

class User:
    '''A user's info, inculding name, balance check, add or deduct balance, set the stake'''
    def __init__(self):
        'Defualt user balance 100 coins and name is None'
        self.balance = 100
        self.name = None


    def getName(self):
        '''Ask and set the user's name'''
        self.name = input('\nHow may I address you? ')
        print ("Hello {}, please take this 100 coins as a gift and the stake.".format(self.name))

    def stake(self):
        '''Ask and set the stake that user wish to bet and return it'''
        self.bet = int(input('How many coins would you like to bet? '))

        while self.bet > self.balance or self.bet <0:
            # stake can't bigger than balance
            if self.bet > self.balance:
                print ("Insufficient Balance, please enter less or equal than {}".format(self.balance))
                self.bet = int(input('How many coins would you like to bet? '))
             # stake can't be negative
            elif self.bet < 0 :
                print ("Stake can't be negative")
                self.bet = int(input('How many coins would you like to bet? '))

        self.balanceDeduct(self.bet)
        return self.bet

    def balanceCheck(self):
        'Check the current balance and return'
        print ("\nDear {},\nYour Balance Now is {} coins.".format(self.name,self.balance))
        return self.balance

    def balanceDeduct(self,bet):
        'Deduct the bet stake from balance'
        self.balance -= bet

    def balanceAdd(self,bouns):
        'Add the bouns to the balance'
        self.balance += bouns

class Info:
    'Program information display and ask for proceed'
    def welcomeInfo(self):
        'Welcome banner'
        print('Welcome to the game!')

    def rules(self):
        'Prind the game rule'
        print('''
        In this game, we have three different dices. Six sided dices, ten sided dices
        and twenty sided dices. At the beginning, system will randomly generate a integer
        as the goal and display it on the screen. You will be asked to enter the bet.
        Then you can choose any number of these three different dices.
        After this, the cup will roll automaticlly and then give a result of the sum of
        these face value of these dices.

        If the roll exactly matches the goal, you will receives 10x bet added to your balance.
        If the roll is within 3 of the goal but not over, you will receives 5x bet added to
        your balance. If the roll is within 10 of the goal but not over, you will receives 2x
        bet added to your balance.

        You can play this game until you wish to exit.
        ''')

    def playOrNot(self):
        'Ask user if they would like to play and return True for yes False for no'
        self.resp = input('Do you want to play the game?(Y/N) ')
        return self.resp == "Y"

    def diceNumber(self):
        'Ask user for the how many of each die they would like to roll and return'
        self.a = int(input('How many Six Sided Dice do you want? '))
        self.b = int(input('How many Ten Sided Dice do you want? '))
        self.c = int(input('How many Twenty Sided Dice do you want? '))
        return self.a,self.b,self.c

def main():
    'Cups and dice gambling game main function'
    # create a new info and print welcome info
    a = Info()
    a.welcomeInfo()
    # create a new user and get the name
    user = User()
    user.getName()
    # introduce the rule of this game
    a.rules()
    # set default balance for the first run
    balance = 1
    # ask user if they wish to play this game
    run = a.playOrNot()
    # loop, if True and non-zero balance, run the game, otherwise end the game
    while (run==True and balance > 0):
        # generate the ramdom goal and display it
        goal = random.randint(1,100)
        print ("\nThe goal is {}".format(goal))
        # ask for the stake user wish to put
        bet = user.stake()
        # ask for how many of each die user wish to have
        six,ten,twenty = a.diceNumber()
        # no more than 100 dices in total
        while six+ten+twenty > 100:
            print("Total number of dices cannot exceed 100, or you will certainly lose\n")
            six,ten,twenty = a.diceNumber()
        # get a new cup with these numbers of dies
        cup = Cup(six,ten,twenty)
        # roll the cup and print the result and reprint the goal
        roll = cup.roll()
        print('\nRolling the cup ...\nThe result is: {}'.format(roll))
        print ("The goal is {}\n\nOpen Cup:".format(goal))
        # print the current dices in the cup
        print(cup)
        # difference use to calculate the result
        diff = goal - roll
        # if roll matches goal, 10x rewards
        if diff == 0:
            user.balanceAdd(10*bet)
            print('\nCongrats! You win 10 times of your stake: {} coins'.format(10*bet))
        # otherwise if roll within 3 of the goal but not over, 5x rewards
        elif diff <= 3 and diff > 0:
            user.balanceAdd(5*bet)
            print('\nCongrats! You win 5 times of your stake: {} coins'.format(5*bet))
        # otherwise if roll within 10 of the goal but not over, 2x rewards
        elif diff <= 10 and diff > 3:
            user.balanceAdd(2*bet)
            print('\nCongrats! You win 2 times of your stake: {} coins'.format(2*bet))
        # otherwise User lose
        else: print('\nSorry, you lose. Good Luck Next Time ~')
        # show the current balance after this round
        balance = user.balanceCheck()
        # ask for if user wish to play again
        run = a.playOrNot()

    # print termination reminder
    print("\nYour final balance is {} coins.".format(balance))
    print("\nThanks for playing.\nService terminated")

main()
