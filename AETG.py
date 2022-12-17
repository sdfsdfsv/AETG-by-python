from TwoWise import TwoWise 
from ThreeWise import ThreeWise


if __name__ == '__main__':


    #文件名，表格字段数
    two=TwoWise("JD.xlsx",18)
    two.two_wise()
    

    two2=TwoWise("XC.xlsx",7)
    two2.two_wise()

    # three=ThreeWise("XC.xlsx",6)
    # three.three_wise()