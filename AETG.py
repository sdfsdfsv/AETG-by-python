from TwoWise import TwoWise 
from ThreeWise import ThreeWise


if __name__ == '__main__':


    #文件名，表格字段数
    two=TwoWise("JD.xlsx",47)
    two.two_wise()
    

    three=ThreeWise("XC.xlsx",71)
    three.three_wise()