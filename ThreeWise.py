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
                                self.Three_wise_dict[(a, b, c)] = 0
            

    def choose_case(self):
        result = []

        #找一个result
        for i in range(self.colnums):
            result.append(self.find_max(self.Three_wise_list[i],result))

            #根据result里面是three_wise对更新
            #每次向当前测试记录加入一个order就更新字典
            for i in range(len(result) - 2):
                for j in range(i + 1, len(result) - 1):
                    for tuple in itertools.permutations([result[i], result[j], result[-1]]):
                        if self.Three_wise_dict.get(tuple)==0:
                            self.Three_wise_dict[tuple] = 1

        return result


    def find_max(self,candi_list, result):
        # Max_index = 0
        count_disappear = [0]*len(candi_list)
        # Max_disappear = 0
        # disappearance = defaultdict(int)

        # for key in self.Three_wise_dict.keys():
        #     if self.Three_wise_dict[key] == 0:
        #         disappearance[(key[0], key[1])] += 1
        #         disappearance[(key[0], key[2])] += 1
        #         disappearance[(key[2], key[1])] += 1

        # fl=False
        # for i,can in enumerate(candi_list):
        #     for res in result:
        #         if disappearance.get((can, res)):
        #             fl=True
        #             if disappearance[(can, res)] > Max_disappear:
        #                 Max_disappear = disappearance[(can, res)]
        #                 Max_index = i
        #         if disappearance.get((res, can)):
        #             fl=True
        #             if disappearance[(res, can)] > Max_disappear:
        #                 Max_disappear = disappearance[(res, can)]
        #                 Max_index = i

        # if fl==False:
        #     return random.choice(candi_list)
            
        #根据还未出现的全排列数量计算最需要的Candidate
        for i,can in enumerate(candi_list):
            for j in range(len(result) - 1):
                for k in range(j + 1, len(result)):
                    for a in itertools.permutations([can, result[j], result[k]]):
                        #根据三元组是否出现判断一个order的不频繁程度
                        if self.Three_wise_dict.get(a)==0:
                            count_disappear[i] += 1
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


            df.loc[count] = self.choose_case()
            count = count + 1
            if count%10==0:
                print(count)
        df.to_excel(self.filename.strip('.xlsx')+'_three_wise_result.xlsx')
