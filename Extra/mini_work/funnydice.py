from random import randrange

class FunnyDice:
    def __init__(self, n=6): # default value of n is 6 as dice has 6 sides
        self.n = int(n) # in case set n as integer
        self.numbers = list(range(1, n+1)) # creates a list of range of numbers including n
        self.index = randrange(0, self.n) # creates a random range of numbers
        self.val = self.numbers[self.index] # shows the number by using numbers list and random index range
        '''(주사위 눈 속성에 바로 접근할 수도 있지만 일반적으로 이렇게 속성에 접근하는 메서드를 구현하여 제공합니다.
        파이썬 클린 코드, Design Pattern 관련된 내용이니 참고하세요)'''
        
    def throw(self): # action of throwing a dice and shows random eye on a dice
        self.index = randrange(0, self.n) # as attribute's already been defined in __init__, can replace as self.index
        self.val = self.numbers[self.index] # as attribute's already been defined in __init__, can replace as self.val
    
    def getval(self): # returns the shown random eye/value from throwing a dice
        return self.val
    
    def setval(self, val: int): # allowing user to set the eyes less or equal to given n
        if val <= self.n:
            self.val = val
        else:
            msg = "number isn't in a dice. Dice has a number from 1 ~ {0}".format(self.n)
            raise ValueError(msg)
    
def get_inputs():
    n = int(input("주사위 면의 개수를 입력하세요: "))
    return n

def main():
    n = get_inputs() # getting a number to choose how many sides on a dice
    mydice = FunnyDice(n) # instance and class
    mydice.throw()
    print("행운의 숫자는? {}".format(mydice.getval()))

if __name__ == '__main__': # means only run module in curernt file as name for current module/file is main
    main()