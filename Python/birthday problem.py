from math import factorial as fac

def doubleBirthday(n):  #Check laplace and basic probability for clarification
    n = int(n)
    return 1 - (fac(365)/(pow(365, n)*fac((365-n))))

def main():
    print("How likely is it that in a given group of people, two have the same birthday?")
    print("Let's find out!")
    print("How many people are in the group?")
    chance = str(doubleBirthday(input()) * 100)
    print("The probability for two people in that group having a matching birthday is:" + chance[:4] + "%")

if __name__ == '__main__':
    main()