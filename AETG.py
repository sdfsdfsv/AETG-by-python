from TwoWise import TwoWise 
from ThreeWise import ThreeWise


if __name__ == '__main__':
    
    two=TwoWise("test1.xlsx",6)
    two.two_wise()

    three=ThreeWise("test2.xlsx",3)
    three.three_wise()