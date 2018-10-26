import pandas as pd 
import numpy as np 
import pdb
np.random.seed(22)

'''
Pandas basically operates on two data structures, Series and Dataframe. Series is one dimensional labelled array wheres as Dataframe
is multi-dimensional.
Read more and discover other operations on these data structures:
 Official documentation - http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro
'''
#Working on series:
data = np.random.randn(6)
srs1 = pd.Series(data) #Creates series with default integral index
srs2 = pd.Series(data[:3],index=['a','b','c']) #Assign alphabets as index
srs3 = pd.Series({'a':1,'b':3,'h':5}) #Dictionary initialization is also possible
print(srs1,"\n\n",srs2,'\n\n',srs3) 

#You can print using the alphbet indeces or the default integral indeces:
print(srs1[2],srs2['b'],srs2[0])

'''
Dataframe is 2-dimensional array like datastructure of Series:
'''
#Construct dataframe using dictionary
dictionary = {
    'first':pd.Series(np.random.randn(5)),
    'second': pd.Series(np.random.randn(10)),
}
d = {
    'first':pd.Series(np.random.randn(10)),
    'second': pd.Series(np.random.randn(10)),
}
#Empty rows are automatically filled with Nans
df1 = pd.DataFrame(dictionary)
df2 = pd.DataFrame(d)
df2.index = [  chr(i) for i in range(65,75) ] #change the row index
df2.columns= ['1st','2nd']
print(df1,'\n\n',df2)

#View the top of the datset
print(df2.head())

#View the end of the dataset
print(df2.tail(3)) #Default argument for both head and tail is 5
 
#Accessing index,columns and values of the dataframe
print(df1.index,'\n\n',df1.columns,'\n\n',df1.values)

#Accsess statistic summary of the data
print(df2.describe())

#Sorting the dataframe
df2 = df2.sort_index(axis=0,ascending=False) #our index is already arranged in ascending order, so let;s reverse that
print(df2)

df2 = df2.sort_values(by='1st') #sort by a column 
print(df2)

#Transposing
print(df2.T)