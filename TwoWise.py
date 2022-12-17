import pandas as pd  # the pandas
import random
import numpy as np
import Excel
import itertools
from collections import defaultdict


class TwoWise:

    def __init__(self, filename, colnums):
        self.filename = filename
        self.colnums = colnums
        self.Two_wise_list = []
        self.Two_wise_dict = {}

    # generate the pair wise coverage.
    # dict 里面的每个key含有两个factor
    def create_dict(self):

        my_list = self.Two_wise_list
        n = len(my_list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                for a in my_list[i]:
                    for b in my_list[j]:
                        self.Two_wise_dict[((i,a),(j,b))] = 0
                        #防止相同值导致漏算，所以得带上索引
        print("there are",len(self.Two_wise_dict),"pairs in total")


    def choose_case(self):
        result = []
        covers=0
        for i,a in enumerate(self.Two_wise_list):
    		# 每次从一个factor的所有order中选一个
            result.append(self.find_max(i,a, result))
            #每次向当前测试记录加入一个order就更新字典

            for ii in range(len(result) - 1):
                if self.Two_wise_dict.get(((ii,result[ii]), (i,result[-1])))==0:
                    covers+=1
                    self.Two_wise_dict[((ii,result[ii]), (i,result[-1]))] = 1
                if self.Two_wise_dict.get(((i,result[-1]), (ii,result[ii])))==0:
                    covers+=1
                    self.Two_wise_dict[((i,result[-1]), (ii,result[ii]))] = 1
        if covers!=0:
            return result+[covers]
        else:
            return None



    def find_max(self, i,candi_list, result):
        # Max_index = 0
        count_disappear = [0]*len(candi_list)
        # Max_disappear = 0
        # disappearance = defaultdict(int)

        # 将仍还是0的二元测试对加入,计算每个未加入测试的order的数量
        # for key in self.Two_wise_dict.keys():
        #     if self.Two_wise_dict.get(key) ==0:
        #         disappearance[key[0]] += 1
        #         disappearance[key[1]] += 1


        # for i, a in enumerate(candi_list):
        #     if disappearance.get(a)==0:

        #         if disappearance[a] > Max_disappear:
        #             Max_disappear = disappearance[a]
        #             Max_index = i


        # 如果之前的测试都有了，就随机选

        for ii, can in enumerate(candi_list):
            for j,res in enumerate(result):
                for a in itertools.permutations([(i,can), (j,res)]):
                    #根据二元组是否出现判断一个order的不频繁程度
                    if  self.Two_wise_dict.get(a) ==0:
                        count_disappear[ii] += 1
                        break

        #有没有纳入测试的二元组，就选拥有处于最低出现率的元素
        if sum(count_disappear) !=0:
            return candi_list[count_disappear.index(max(count_disappear))]
        else:#如果当前的所有二元组合都有了，就随机选一个
            return random.choice(candi_list)





    def two_wise(self):

        df = pd.DataFrame(columns=Excel.get_factor(self.filename))
        self.Two_wise_list = Excel.excel_to_list(self.filename,self.colnums)
        self.create_dict()

        count = 1

        while 1:

            if 0 not in self.Two_wise_dict.values(): break
            
            a=self.choose_case()
            if a is not None:
                df.loc[count] = a
                count = count + 1
            print(count)

        df.to_excel(self.filename.strip('.xlsx')+'_two_wise_result.xlsx')
