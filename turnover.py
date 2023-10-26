import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
import seaborn as sns

# # read xlxs
# df1 = pd.read_excel('LOYALTY.VER2.xlsx', sheet_name='POS Data', index_col=None)
# df2 = pd.read_excel('LOYALTY.VER2.xlsx', sheet_name='Loyalty', index_col=None)
# df3 = pd.read_excel('LOYALTY.VER2.xlsx', sheet_name='Hierachy Categories & Barcodes', index_col=None)

# # save to pickle
# df1.to_pickle("posdata.pkl")
# df2.to_pickle("loyalty.pkl")
# df3.to_pickle("categories.pkl")



# read the pickle file
picklefile1 = open('posdata.pkl', 'rb')
picklefile2 = open('loyalty.pkl', 'rb')
picklefile3 = open('categories.pkl', 'rb')

#unpickle the dataframe
df_posdata = pickle.load(picklefile1)
df_loyalty = pickle.load(picklefile2)
df_categories = pickle.load(picklefile3)

#close file
picklefile1.close()
picklefile2.close()
picklefile3.close()

df_posdata['Month'] = pd.DatetimeIndex(df_posdata['Date']).month



df_posdata = df_posdata.drop(columns=["Basket_ID"])
df_posdata = df_posdata.drop(columns=["Date"])
df_posdata = df_posdata.drop(columns=["Quantity"])
df_posdata = df_posdata.drop(columns=["Value"])
df_posdata = df_posdata.drop(columns=["Barcode"])
# print(df_posdata)

df_sem1 = df_posdata[(df_posdata.Month == 1) | (df_posdata.Month == 2) | ((df_posdata.Month >= 9) & (df_posdata.Month <= 12))]
df_sem1 = df_sem1.drop_duplicates('LoyaltyCard_ID')
print(df_sem1)

df_sem2 = df_posdata[((df_posdata.Month >= 3) & (df_posdata.Month <= 8))]
df_sem2 = df_sem2.drop_duplicates('LoyaltyCard_ID')
print(df_sem2)

