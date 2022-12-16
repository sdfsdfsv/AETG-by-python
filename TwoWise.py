import pandas as pd #the pandas
import random
import numpy as np
import Excel


class TwoWise:


	def __init__(self,filename,colnums):
		self.filename=filename
		self.colnums=colnums

	#generate the pair wise coverage.

	def create_dict(self,my_list):

	    Two_wise_dict={}
	    n=len(my_list)
	    for index1 in range(n - 1):
	        for index2 in range(index1 + 1, n):
	            for l3 in my_list[index1]:
	                for l4 in my_list[index2]:
	                    Two_wise_dict[(l3,l4)] = 0

	    return Two_wise_dict



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
	            if disappearance.get(key[0]):
	                disappearance[key[0]] += 1
	            else:
	                disappearance[key[0]] = 1
	            if disappearance.get(key[1]):
	                disappearance[key[1]] += 1
	            else:
	                disappearance[key[1]] = 1

	    flag = 0

	    for index in range(len(candi_list)):
	        if disappearance.get(candi_list[index]):
	            flag = 1
	            if disappearance[candi_list[index]] > Max_disappear:
	                Max_disappear = disappearance[candi_list[index]]
	                Max_index = index

	    if flag == 0:
	        return random.choice(candi_list)

	    for index in range(len(candi_list)):
	        count_disappear.append(0)

	    for index1 in range(len(candi_list)):
	        for index2 in range(len(result)):
	            tuple1 = (candi_list[index1], result[index2])
	            tuple2 = (result[index2], candi_list[index1])
	            if dict.get(tuple1) == 0:
	                count_disappear[index1] += 1
	                continue
	            if dict.get(tuple2) == 0:
	                count_disappear[index1] += 1

	    arr = np.array(count_disappear)

	    if (arr == 0).all():
	        return candi_list[Max_index]
	    else:
	        Max_index = count_disappear.index(max(count_disappear))
	    return candi_list[Max_index]





	def two_wise(self):

		Two_wise_list=Excel.excel_to_list(self.filename,self.colnums)

		df = pd.DataFrame(columns=Excel.get_factor(self.filename))

		Two_wise_dict = self.create_dict(Two_wise_list)
		count = 1
		Keys = list(Two_wise_dict.keys())

		while 1:
		    if 0 not in Two_wise_dict.values(): break
		    count_pairs = 0
		    testcase = self.choose_case(Two_wise_list, Two_wise_dict, self.colnums)

		    for i in range(len(testcase) - 1):
		        for j in range(i + 1, len(testcase)):
		            new_tuple1 = (testcase[i], testcase[j])
		            new_tuple2 = (testcase[j], testcase[i])
		            if Two_wise_dict.get(new_tuple1) == 0:
		                Two_wise_dict[new_tuple1] = 1
		                count_pairs += 1
		            if Two_wise_dict.get(new_tuple2) == 0:
		                Two_wise_dict[new_tuple2] = 1
		                count_pairs += 1
		    testcase.append(count_pairs)
		    df.loc[count] = testcase
		    count = count + 1
		df.to_excel(self.filename.strip('.xlsx')+'_two_wise_result.xlsx')