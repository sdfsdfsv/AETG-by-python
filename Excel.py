import pandas as pd #the pandas

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

# (1)dataframe.shape     #元组，返回dataframe形状 如（1000,10）即1000行10列
# (2)dataframe.head(3)    #新DataFrame，获取前三行，默认获取前五行
# (3)dataframe.tail(3)    #新DataFrame，获取后三行，默认获取后五行
# (4)dataframe.index     #获取DataFrame的index
# (5)dataframe.columns   #获取columns，DataFrame的列索引列表
# (6)dataframe.values    #获取values    ，获取所有values
# (7)dataframe.info      #获取dataframe的信息
# (8)dataframe.describe  #dataframe统计性描述
# (9)dataframe.dtypes    #查看dataframe所有列的数据类型

# (1)dataframe.T                     #转置，新DataFrame，行列互换
# (2)data.index = list               #设置index，新DataFrame按照list的数据内容修改index，必须整体全部修改
# (3)df.reset_index(drop=False)     #重设新的下标索引，新DataFrame,drop:默认为False，不删除原来索引，如果为True,删除原来的索引值
# (4)df.set_index(keys, drop=True)  #把某列值设置为新的索引，keys : 列索引名成或者列索引名称的列表；drop: 默认为False，不删除原来索引，如果为True,删除原来的索引值          
# (5)dataframe[‘A’].astype(np.float32)  #修改数据类型

# 输出一个[[]]，每项又是一个包含每个factor的所有order的[],比如[[淘宝,京东][windows,macos,linux,android][华为,小米,联想]]


def excel_to_list(filename, number):
    df= pd.read_excel(filename)

    print("the order in each factor of",filename,"is\n",df.head(number).T.values.tolist()[1::],"\n")


    #python一句话搞定牛逼


    return df.head(number).T.values.tolist()[1::]


def get_factor(filename):
    # print(pd.read_excel(filename).keys().values.tolist()[1::])
    return pd.read_excel(filename).keys().values.tolist()[1::]



if __name__ == '__main__':
    excel_to_list("test1.xlsx",5)
    get_factor("test1.xlsx")