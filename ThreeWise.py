import pandas as pd #the pandas
import random
import numpy as np
import Excel
import itertools
from collections import defaultdict

class ThreeWise:

    def __init__(self,filename,colnums):
        self.filename=filename
        self.colnums=colnums
        self.Three_wise_list = []
        self.Three_wise_dict = {}

    def create_dict(self):

        my_list = self.Three_wise_list
        n=len(my_list)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    for a in my_list[i]:
                        for b in my_list[j]:
                            for c in my_list[k]:
                                self.Three_wise_dict[((i,a),(j,b),(k,c))] = 0
            
        print("there are",len(self.Three_wise_dict),"pairs in total")

    def choose_case(self):
        result = []
        covers=0
        #找一个result
        for i,a in enumerate(self.Three_wise_list):
            result.append(self.find_max(i,a,result))

            #根据result里面是three_wise对更新
            #每次向当前测试记录加入一个order就更新字典
            for ii in range(len(result) - 2):
                for j in range(ii + 1, len(result) - 1):
                    for tuple in itertools.permutations([(ii,result[ii]), (j,result[j]), (i,result[-1])]):
                        if self.Three_wise_dict.get(tuple)==0:
                            covers+=1
                            self.Three_wise_dict[tuple] = 1
        if covers!=0:
            return result+[covers]
        else:
            return None



    def find_max(self,i,candi_list, result):

        count_disappear = [0]*len(candi_list)

            
        #根据还未出现的全排列数量计算最需要的Candidate
        for ii,can in enumerate(candi_list):
            for j in range(len(result) - 1):
                for k in range(j + 1, len(result)):
                    for a in itertools.permutations([(i,can), (j,result[j]), (k,result[k])]):
                        #根据三元组是否出现判断一个order的不频繁程度
                        if self.Three_wise_dict.get(a)==0:
                            count_disappear[ii] += 1
                            break


        #有没有纳入测试的三元组，就选拥有处于最低出现率的元素
        if sum(count_disappear)!=0:
            return candi_list[count_disappear.index(max(count_disappear))]
        else:
            return random.choice(candi_list)






    def three_wise(self):

        df = pd.DataFrame(columns=Excel.get_factor(self.filename))
        self.Three_wise_list=Excel.excel_to_list(self.filename,self.colnums)
        self.create_dict()

        count = 1
        while 1:
            if 0 not in self.Three_wise_dict.values():   break

            a=self.choose_case()
            if a is not None:
                df.loc[count] = a
                count = count + 1

            print(count)
        df.to_excel(self.filename.strip('.xlsx')+'_three_wise_result.xlsx')
