import pandas as pd #the pandas
import random
import numpy as np
import Excel


class ThreeWise:

    def __init__(self,filename,colnums):
        self.filename=filename
        self.colnums=colnums

    def create_dict(self,my_list):

        Three_wise_dict = {}
        n=len(my_list)
        for index1 in range(n - 2):
            for index2 in range(index1 + 1, n - 1):
                for index3 in range(index2 + 1, n):
                    for l4 in enumerate(my_list[index1]):
                        for l5 in enumerate(my_list[index2]):
                            for l6 in enumerate(my_list[index3]):
                                Three_wise_dict[(l4, l5, l6)] = 0
            

        return Three_wise_dict


    def choose_case(self,list, dict, number):
        result = []
        for index in range(number):
            result.append(self.find_max(list[index], dict, result))
        return result


    def find_max(self,candi_list, dict, result):
        Max_index = 0
        count_disappear = []
        Max_disappear = 0
        disappearance = {}

        for key in dict.keys():
            if dict[key] == 0:
                if disappearance.get((key[0], key[1])):
                    disappearance[(key[0], key[1])] += 1
                else:
                    disappearance[(key[0], key[1])] = 1
                if disappearance.get((key[0], key[2])):
                    disappearance[(key[0], key[2])] += 1
                else:
                    disappearance[(key[0], key[2])] = 1
                if disappearance.get((key[2], key[1])):
                    disappearance[(key[2], key[1])] += 1
                else:
                    disappearance[(key[2], key[1])] = 1
        flag = 0
        for can in candi_list:
            for res in result:
                if disappearance.get((can, res)):
                    flag = 1
                    if disappearance[(can, res)] > Max_disappear:
                        Max_disappear = disappearance[(can, res)]
                        Max_index = index
                if disappearance.get((res, can)):
                    flag = 1
                    if disappearance[(res, can)] > Max_disappear:
                        Max_disappear = disappearance[(res, can)]
                        Max_index = index
        if flag == 0:
            return random.choice(candi_list)

        for index in range(len(candi_list)):
            count_disappear.append(0)


        for index1 in range(len(candi_list)):
            for index2 in range(len(result) - 1):
                for index3 in range(index2 + 1, len(result)):
                    tuple1 = (candi_list[index1], result[index2], result[index3])
                    tuple2 = (candi_list[index1], result[index3], result[index2])
                    tuple3 = (result[index3], candi_list[index1], result[index2])
                    tuple4 = (result[index3], result[index2], candi_list[index1])
                    tuple5 = (result[index2], candi_list[index1], result[index3])
                    tuple6 = (result[index2], result[index3], candi_list[index1])
                    if dict.get(tuple1) == 0:
                        count_disappear[index1] += 1
                        continue
                    if dict.get(tuple2) == 0:
                        count_disappear[index1] += 1
                        continue
                    if dict.get(tuple3) == 0:
                        count_disappear[index1] += 1
                        continue
                    if dict.get(tuple4) == 0:
                        count_disappear[index1] += 1
                        continue
                    if dict.get(tuple5) == 0:
                        count_disappear[index1] += 1
                        continue
                    if dict.get(tuple6) == 0:
                        count_disappear[index1] += 1
        arr = np.array(count_disappear)
        if (arr == 0).all():
            return candi_list[Max_index]
        else:
            Max_index = count_disappear.index(max(count_disappear))
        return candi_list[Max_index]



    def three_wise(self):

        Three_wise_list=Excel.excel_to_list(self.filename,self.colnums)

        df = pd.DataFrame(columns=Excel.get_factor(self.filename))

        Three_wise_dict = self.create_dict(Three_wise_list)
        count = 1
        Keys = list(Three_wise_dict.keys())
        print(123)
        while 1:
            if 0 not in Three_wise_dict.values(): break
            count_pairs = 0
            testcase = self.choose_case(Three_wise_list, Three_wise_dict, self.colnums)

            for i in range(len(testcase) - 2):
                for j in range(i + 1, len(testcase) - 1):
                    for k in range(j + 1, len(testcase)):
                        new_tuple1 = (testcase[i], testcase[j], testcase[k])
                        new_tuple2 = (testcase[i], testcase[k], testcase[j])
                        new_tuple3 = (testcase[j], testcase[k], testcase[i])
                        new_tuple4 = (testcase[j], testcase[i], testcase[k])
                        new_tuple5 = (testcase[k], testcase[j], testcase[i])
                        new_tuple6 = (testcase[k], testcase[i], testcase[j])
                        if Three_wise_dict.get(new_tuple1) == 0:
                            Three_wise_dict[new_tuple1] = 1
                            count_pairs += 1
                        if Three_wise_dict.get(new_tuple2) == 0:
                            Three_wise_dict[new_tuple2] = 1
                            count_pairs += 1
                        if Three_wise_dict.get(new_tuple3) == 0:
                            Three_wise_dict[new_tuple3] = 1
                            count_pairs += 1
                        if Three_wise_dict.get(new_tuple4) == 0:
                            Three_wise_dict[new_tuple4] = 1
                            count_pairs += 1
                        if Three_wise_dict.get(new_tuple5) == 0:
                            Three_wise_dict[new_tuple5] = 1
                            count_pairs += 1
                        if Three_wise_dict.get(new_tuple6) == 0:
                            Three_wise_dict[new_tuple6] = 1
                            count_pairs += 1
            if count_pairs == 0:
                continue
            testcase.append(count_pairs)

            df.loc[count] = testcase
            count = count + 1
        df.to_excel(self.filename.strip('.xlsx')+'_three_wise_result.xlsx')
