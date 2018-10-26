import pandas as pd 
import numpy as np 

'''
Standard python indexing methods work fine with pandas data structures but its recommended to use pandas indexing methods which are 
heavily optimized
'''
dict = {
    'A' : pd.Series(np.random.randn(5)),
     'g' : pd.Series(np.random.randn(5)),
    'r' : pd.Series(np.random.randn(5)),

}
df = pd.DataFrame(dict)
df.index = [ chr(i) for i in range(65,70)]
print(df)

#selecting using standard selection methods, ny using label or index
#print(df[0],'\n',df[0]) #access using index
print('\n',df['A'],'\n',df['A':'C']) #Access using labels 1st method selects columns 2nd slices through rows
print('\n',df[0:2])
print('\nList selection:\n',df[['A','r']])

#Let's use pandas optimized method accessing
#1)accessing using labels:
print('\n D of A' ,df.loc['D',['A']])
print('\n\n List selection ',df.loc['B':'D',['A','r']])

#2)Selection using index:
print('3\n\n',df.iloc[1]) #print particular column
print('\n\n',df.iloc[0:3,0:2])

#accessing a scalar:
print('\n scalar at 1,1',df.iloc[1,1])
####!!!NOTE: it is recommended to use iat for accessing a scalar as it is optimized
print('\n scalar at 1,1',df.iat[1,1])

'''
More about indexing and advanced indexing:
http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing
http://pandas.pydata.org/pandas-docs/stable/advanced.html#advanced
'''