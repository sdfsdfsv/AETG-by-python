import pandas as pd #the pandas
import numpy as np
# filename: the name of the Excel file to read
# col_number: the number of the column to read from the Excel file

# The function reads the specified column from the Excel file using the pandas.read_excel() function, and stores the data in a pandas DataFrame object. 
# It then removes any rows that have any missing values (NaN values) using the dropna() function.

# Next, the function converts the DataFrame to a list of lists using the values.tolist() method, and iterates over the list of lists. 
# For each sublist, it extracts the first element (which is the value from the specified column) and appends it to a result list.

# Finally, the function returns the result list, which contains all the values from the specified column of the Excel file, with any missing values removed.


# def read_excel1(filename, col_number):
#     df = pd.read_excel(filename, usecols=[col_number], names=None)
    
#     # df = df.dropna(axis=0, how='any')
#     #drop empty col

#     df_li = df.values.tolist()
#     result = []
#     for s_li in df_li:
#         result.append(s_li[0])

#     return result


# 输出一个[[]]，每项又是一个包含每个factor的所有order的[],比如[[淘宝,京东][windows,macos,linux,android][华为,小米,联想]]


def excel_to_list(filename, number):
    df= pd.read_excel(filename)
    a=df.head(number).T.values.tolist()[1::]
    
    
    for i in range(len(a)):
        #去除空项nan,动用黑科技
        a[i]=list(i for i in a[i] if i == i)
    print("the order in each factor of",filename,"is\n",a,"\n")
    return a


def get_factor(filename):

   
    return pd.read_excel(filename).keys().values.tolist()[1::]+['覆盖数量']


