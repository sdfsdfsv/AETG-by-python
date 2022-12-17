from TwoWise import TwoWise 
from ThreeWise import ThreeWise


if __name__ == '__main__':


    #文件名，表格字段数
    two1=TwoWise("JD.xlsx",18)
    two1.two_wise()
    

    two2=TwoWise("XC.xlsx",7)
    two2.two_wise()


    three1=ThreeWise("JD.xlsx",18)
    three1.three_wise()

    three2=ThreeWise("XC.xlsx",7)
    three2.three_wise()