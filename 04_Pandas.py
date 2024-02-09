import pandas as pd
# import numpy as np

#### DICT
# O(1) access complexity but sometimes user don't know about missing keys
d = dict()                              # empty dict, or d = {}
d['A'] = 123;     d['B'] = 345          # fill the dict (can be different types too)
print(d, d.keys(), d.values())          # print the dict
for i in d :
    print("%s  %d" %(i, d[i]) )         # alternative print

del d['A']                              # delete one record
print('A' in d)                         # to check if a key exist in a dict --> False

# print(d.has_key('B'))                 # same thing --> but gives error
print(d.get('A', "N/A"))                # get a key's value, o.w. return a msg --> N/A
print(d.setdefault('A', "None"))
print(d['A'], d['B'])                   # print as a list --> None 345
print(d.items())                        # get as list of pairs
#print (str(d))                         # get as a string (error!)
print(len(d))                           # count the pairs
# copy(), clear(),


#### SERIES
cuteness = pd.Series([1, 2, 4, 5], index=['Cockroach', 'Fish', 'Puppy', 'Kitten'])
print(cuteness > 3)                                         # boolean op over whole array
print(cuteness[cuteness > 3])                               # conditional select

data = {'a' : 0, 'b' : 1, 'c' : 2}                          # dict as data
sr1 = pd.Series(data, index=['b','c','d','a'])
sr1                                                         # order: b-->c-->d-->a. d: NaN
sr1['c']                                                    # access using the index


#### DATA FRAME
# Syntax: pandas.DataFrame(data, index, columns, dtype, copy)
# Can consist of lists, dict, series, arrays, another DF
df1 = pd.DataFrame(sr1,                                     # using series
                   dtype=float)                             # notice the data type cast
df1                                                         # notice it fills columns first

df2 = pd.DataFrame([['name1', 'sur1', 30],                  # using list
                    ['name2', 'sur2', 32],
                    ['name3', 'sur3', 35]],
                    columns=['Name','Surname', 'Age'],      # index = [0,1,2 ..] as default
                    dtype=float)
df2
df2 = pd.DataFrame({'Name': ['name1', 'name2', 'name3'],    # using dict
                    'Surname': ['sur1', 'sur2', 'sur3'],    # column names are inherent
                    'Age': [30, 32, 34]})
df2
df2.describe()                                              # stats of all columns w/ numbers
df2.dtypes                                                  # data types pf each column
df2.head(2)                                                 # select first  2 (default: 5)
df2.tail(2)                                                 # //    //      2  (//)
df2.loc[1]                                                  # get row --> name2, sur2 ..
df2.iloc[1]                                                 # accepts integer instead of row label
df2['Surname']                                              # get col --> sur1, sur2 ..
df2[['Surname', 'Age']]                                     # get multi col. as list (double phar.)

df2[df2['Age'] > 31]                                        # get conditional (inquiry)
df2['Name'][df2['Age'] > 31]                                # conditional + filtered

df2['Age'].values[2]                                        # get single element: converting to arr
df2.at[2, 'Age']                                            # or fast scalar access using indexes
df2.iat[2, 2]                                               # // using integer indexes


df2['Weight'] = pd.Series([110, 150, 180])                  # add column
df2['Age+Weight'] = df2['Age'] + df2['Weight']              # new col using other cols\
df2[:2]                                                     # choose rows <2 --> row0 + row1
del df2['Surname']                                          # del column --> can use pop to to capturedf
df3 = df2.drop(1)                                           # drops row1
df3
df3 = df2.append(df1)                                       # add tables --> NaN for non-matching indexes
df3

print(df2.columns.ravel())
df2.columns[1]                                              # get the 2nd col
print(df2[df2.columns[1]])                                  # direct print returns another DF
print(df2[df2.columns[1]].tolist())                         # use tolist() to return array




# few extra examples