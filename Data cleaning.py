import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
import seaborn as sns

# # read xlxs
# df1 = pd.read_excel('DATASET.VER1.xlsx', sheet_name='POS Data', index_col=None)
# df2 = pd.read_excel('DATASET.VER1.xlsx', sheet_name='Loyalty', index_col=None)
# df3 = pd.read_excel('DATASET.VER1.xlsx', sheet_name='Hierachy Categories & Barcodes', index_col=None)

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

#POS DATA

# df_posdata["Barcode"] = df_posdata["Barcode"].astype(str)
# df_posdata.to_pickle("posdata.pkl")

# df_categories["Barcode"] = df_categories["Barcode"].astype(str)
# df_categories.to_pickle("categories.pkl")

# invalid barcodes
# barcodes_posdata =  list(df_posdata["Barcode"])
# barcodes_categories =  list(df_categories["Barcode"])

# listnotin = []
# for barc in barcodes_posdata:
#     if barc not in barcodes_categories:
#         listnotin.append(barc)

# invalid_barcodes = df_posdata[df_posdata['Barcode'].isin(listnotin)]
# print(len(invalid_barcodes))

# for ind in invalid_barcodes.index:
#     df_posdata.drop(ind, inplace = True )

# df_posdata.to_pickle("posdata.pkl")
# print(df_posdata.shape)


# negative quantities
# print(df_posdata.iloc[1401])
# print(df_posdata.iloc[2163])

# print(sum(df_posdata["Quantity"] < 0))
# for index in np.where(df_posdata.Quantity < 0):
#     df_posdata.drop(df_posdata.index[index], inplace=True)
#     # print(index)

# df_posdata.to_pickle("posdata.pkl")
# print(df_posdata.shape)

# zero quantities
# print(sum(df_posdata["Quantity"] == 0))
# print(np.where(df_posdata.Quantity == 0))
# print(df_posdata.iloc[1897])
# for index in np.where(df_posdata.Quantity == 0):
#     print(index)
#     df_posdata.drop(df_posdata.index[index], inplace=True)

# df_posdata.to_pickle("posdata.pkl")
# print(df_posdata.shape)

#not integer quantities
# for index, quan in df_posdata['Quantity'].iteritems():
#     if not (quan.is_integer()):
#         print(index)
#         print(df_posdata.loc[index])
#         frac, whole = math.modf(quan)
#         if (frac < 0.5 and whole != 0):
#             df_posdata.loc[index, "Quantity"] = math.floor(quan)
#         else:
#             df_posdata.loc[index, "Quantity"] = math.ceil(quan)
#         print(df_posdata.loc[index])

# df_posdata.to_pickle("posdata.pkl")
# # print(df_posdata.loc[59])
# print(df_posdata.shape)

## negative values
# print(sum(df_posdata["Value"] < 0))

# df_posdata.to_pickle("posdata.pkl")
# print(df_posdata.shape)

## zero values
# print(sum(df_posdata["Value"] == 0))
# print(np.where(df_posdata.Value == 0))
# print(df_posdata.iloc[5])
# print(df_posdata.iloc[82])

# for index in np.where(df_posdata.Value == 0):
#     print(index)
#     df_posdata.drop(df_posdata.index[index], inplace=True)

# df_posdata.to_pickle("posdata.pkl")
# print(df_posdata.shape)

# for array in (np.where(df_posdata.Value == 0)):
#     for index in array:
#         # print(df_posdata.iloc[index])
#         barc = df_posdata.iloc[index, 2]
#         # print(barc)
#         print(index)
#         print(df_posdata.iloc[index])
#         # print(type(barc))

#         for array2 in np.where(df_posdata.Barcode == barc):
#             for index2 in array2:
#                 if df_posdata.iloc[index2, 4] != 0:
#                     ### 1 + 1 free???
#                     if (df_posdata.iloc[index, 0] == df_posdata.iloc[index2, 0] and 
#                         df_posdata.iloc[index, 1] == df_posdata.iloc[index2, 1] and
#                         df_posdata.iloc[index, 2] == df_posdata.iloc[index2, 2] and
#                         df_posdata.iloc[index, 3] == df_posdata.iloc[index2, 3] and 
#                         df_posdata.iloc[index, 5] == df_posdata.iloc[index2, 5]):

#                         print(index2)
#                         print(df_posdata.iloc[index2])
                        
#                     else:
#                         print("ELSEEEEEEEEEEEEEE")
#                         print(index2)
#                         print(df_posdata.iloc[index2])
                    
#                         new_value = (df_posdata.iloc[index2, 4]/df_posdata.iloc[index2, 3])*df_posdata.iloc[index, 3]
#                         df_posdata['Value'].iloc[index] = new_value
#                         print(df_posdata.iloc[index])
#                     print("------------------------------------------------------------------")
#                     # paok
#                     break


# print(len(pd.unique(df_posdata['LoyaltyCard_ID'])))
# print(len(pd.unique(df_loyalty['Cardholder'])))

# df_posdata["LoyaltyCard_ID"] = df_posdata["LoyaltyCard_ID"].astype(str)
# df_posdata.to_pickle("posdata.pkl")

# df_loyalty["Cardholder"] = df_loyalty["Cardholder"].astype(str)
# df_loyalty.to_pickle("loyalty.pkl")

# invalid loyalty cards
# df_posdata.to_pickle("posdata.pkl")


# print(df_posdata.head())
# print(df_posdata.shape)
# print(df_posdata.info())

# print(len(pd.unique(df_posdata['Basket_ID'])))
# print(sum(df_posdata.Basket_ID.map(str).apply(len) == 20))
# print("\n")



###Loyalty
# null cardholder
# df_loyalty = df_loyalty.dropna()
# df_loyalty.to_pickle("loyalty.pkl")

# unnecessary cardholder
# df_loyalty["Cardholder"] = pd.to_numeric(df_loyalty["Cardholder"], downcast='integer').astype(str)
# df_loyalty["Cardholder"] = df_loyalty["Cardholder"].astype(str)
# df_loyalty.to_pickle("loyalty.pkl")

# df_posdata["LoyaltyCard_ID"] = df_posdata["LoyaltyCard_ID"].astype(str)
# df_posdata.to_pickle("posdata.pkl")

# card_loyalty =  list(df_loyalty["Cardholder"])
# card_posdata =  list(df_posdata["LoyaltyCard_ID"])

# # print(card_loyalty)

# listnotin = []
# for card in card_loyalty:
#     if card not in card_posdata:
#         print(card)
#         df_loyalty.drop(df_loyalty.index[df_loyalty['Cardholder'] == card], inplace = True)


# print(pd.unique(df_loyalty['Status']))
# print(sum(df_loyalty["Status"] == "couple"))

# df_loyalty.to_pickle("loyalty.pkl")
# print(df_loyalty.head())
# print(df_loyalty.shape)
# print(df_loyalty.info())
# print(len((pd.unique(df_loyalty['Cardholder']))))
# print("\n")



###Categories
# print(len(pd.unique(df_categories['Barcode'])))
# print(sum((df_categories.Barcode.map(str).apply(len)) == 13))

# print(pd.unique(df_categories['Category C']))

# unnecessary barcodes
# barcodes_categories =  list(df_categories["Barcode"])
# barcodes_posdata =  list(df_posdata["Barcode"])

# listnotin = []
# for barc in barcodes_categories:
#     if barc not in barcodes_posdata:
#         # print(barc)
#         df_categories.drop(df_categories.index[df_categories['Barcode'] == barc], inplace = True)
        # listnotin.append(barc)

# invalid_barcodes = df_categories[df_categories['Barcode'].isin(listnotin)]
# print(len(invalid_barcodes))

 
# print(df_categories.head())
# print(df_categories.shape)
# print(df_categories.info())
# print("\n")


# print(df_posdata.shape)
# print(df_loyalty.shape)
# print(df_categories.shape)
# print(len((pd.unique(df_categories['Barcode']))))

###MEXRI EDO DATASET.VER1

## outliers

##delete baskets with 1 product
# print(sum(df_posdata.groupby("Basket_ID")["Barcode"].count() < 2))
# print((df_posdata.groupby("Basket_ID")["Barcode"].count()))

# morethan2barcodes = df_posdata.groupby("Basket_ID")["Barcode"].count().reset_index()
# morethan2barcodes = morethan2barcodes.loc[morethan2barcodes["Barcode"] >= 2]
# print(morethan2barcodes)

# print(df_posdata["Basket_ID"].isin(morethan2barcodes["Basket_ID"]).value_counts())
# df_posdata = df_posdata.loc[df_posdata["Basket_ID"].isin(morethan2barcodes["Basket_ID"])]
# print(df_posdata["Basket_ID"].isin(morethan2barcodes["Basket_ID"]).value_counts())

# df_posdata.to_pickle("posdata.pkl")
# print(df_posdata.shape)
# print(len(pd.unique(df_posdata['Basket_ID'])))

##delete invalid rows
# print(df_posdata.loc[(df_posdata['Value'] < 0.45) & (df_posdata['Quantity'] > 4)])
# df_posdata = df_posdata.drop(df_posdata[((df_posdata['Value'] < 0.45) & (df_posdata['Quantity'] > 4))].index)
# print(df_posdata[((df_posdata['Value'] < 0.45) & (df_posdata['Quantity'] > 4))].index)
# df_posdata.to_pickle("posdata.pkl")
# print(df_posdata.shape)
# print(len(pd.unique(df_posdata['Basket_ID'])))

##delete invalid baskets
# grouped_baskets = df_posdata.groupby("Basket_ID")["Quantity", "Value"].sum().reset_index()
# names = {'Quantity': 'Sum quantity', 'Value': 'Sum value'}
# grouped_baskets.rename(columns=names, inplace=True)

# for basket_id, quantity, value in zip(grouped_baskets['Basket_ID'], grouped_baskets['Sum quantity'], grouped_baskets['Sum value']):
#     if (quantity > 4 and value < 0.45):
#         # print(basket_id)
#         df_posdata.drop(df_posdata.index[df_posdata['Basket_ID'] == basket_id], inplace = True)

# df_posdata.to_pickle("posdata.pkl")
# print(df_posdata.shape)

# grouped_baskets.plot(kind = 'scatter', x = 'Sum quantity', y = 'Sum value')
# plt.show()

###MEXRI EDO DATASET.VER2



##delete customer with too much purchases
# max_customer = df_posdata.groupby("LoyaltyCard_ID")["Basket_ID"].count().reset_index()
# print(max_customer.sort_values(by=["Basket_ID"]))
# max_customer = max_customer.loc[max_customer["LoyaltyCard_ID"] != 28504821]
# print(max_customer.sort_values(by=["Basket_ID"]))


# print(df_posdata["LoyaltyCard_ID"].isin(max_customer["LoyaltyCard_ID"]).value_counts())
# df_posdata = df_posdata.loc[df_posdata["LoyaltyCard_ID"].isin(max_customer["LoyaltyCard_ID"])]
# print(df_posdata["LoyaltyCard_ID"].isin(max_customer["LoyaltyCard_ID"]).value_counts())

# df_posdata.to_pickle("posdata.pkl")
# print(df_posdata.shape)


##MEXRI EDO DATASET.VER3


##delete outliers from scatter plot (quan>50 or value>100)
# grouped_baskets = df_posdata.groupby("Basket_ID")["Quantity", "Value"].sum().reset_index()
# names = {'Quantity': 'Sum quantity', 'Value': 'Sum value'}
# grouped_baskets.rename(columns=names, inplace=True)

# # grouped_baskets.plot(kind = 'scatter', x = 'Sum quantity', y = 'Sum value')
# # plt.show()


# for basket_id, quantity, value in zip(grouped_baskets['Basket_ID'], grouped_baskets['Sum quantity'], grouped_baskets['Sum value']):
#     if (quantity > 50 or value > 100):
#         # print(basket_id)
#         df_posdata.drop(df_posdata.index[df_posdata['Basket_ID'] == basket_id], inplace = True)


# df_posdata.to_pickle("posdata.pkl")
# print(df_posdata.shape)

##MEXRI EDO DATASET.VER4








# print(df_posdata["Basket_ID"].isin(morethan2barcodes["Basket_ID"]).value_counts())
# df_posdata = df_posdata.loc[df_posdata["Basket_ID"].isin(morethan2barcodes["Basket_ID"])]
# print(df_posdata["Basket_ID"].isin(morethan2barcodes["Basket_ID"]).value_counts())

# print(df_posdata.loc[df_posdata["Basket_ID"] == "C28504821B8D20180922"])

# print(df_posdata.loc[df_posdata["LoyaltyCard_ID"] == "28504821"])

# df_posdata.plot(kind = 'scatter', x = 'Quantity', y = 'Value')
# plt.show()


# print(df_posdata.groupby("Basket_ID")["Quantity"].sum())
# print(sum(df_posdata.groupby("Basket_ID")["Quantity"].sum() == 1))
# print(np.where(df_posdata.groupby("Basket_ID")["Quantity"].sum() == 1))


# print(df_posdata.describe())
# print(df_posdata["Quantity"].median())
# print(df_posdata["Value"].median())



#delete baskets with >58 quantity and > 120 value
# grouped_baskets = df_posdata.groupby("Basket_ID")["Quantity", "Value"].sum().reset_index()
# # grouped_baskets = df_posdata.groupby("Basket_ID")["Quantity", "Value", "Barcode"].agg({'Quantity':'sum', 'Value': 'sum','Barcode':'count'})
# names = {'Quantity': 'Sum quantity', 'Value': 'Sum value'}
# grouped_baskets.rename(columns=names, inplace=True)
# # print (grouped_baskets)
# # print(grouped_baskets.shape)

# grouped_baskets.plot(kind = 'scatter', x = 'Sum quantity', y = 'Sum value')
# plt.show()

# print(df_posdata.shape)
# print(sum(df_posdata.groupby("Basket_ID")["Quantity"].sum() > 58))
# print(np.where(df_posdata.groupby("Basket_ID")["Quantity"].sum() > 58))

# for basket_id, quantity in zip(grouped_baskets['Basket_ID'], grouped_baskets['Sum quantity']):
#     if quantity >= 60:
#         # print(basket_id)
#         df_posdata.drop(df_posdata.index[df_posdata['Basket_ID'] == basket_id], inplace = True)

# for basket_id, quantity, value in zip(grouped_baskets['Basket_ID'], grouped_baskets['Sum quantity'], grouped_baskets['Sum value']):
#     if (quantity > 4 and value < 0.45):
#         print(basket_id)
        # df_posdata.drop(df_posdata.index[df_posdata['Basket_ID'] == basket_id], inplace = True)

# df_posdata.to_pickle("posdata.pkl")
# da['Value'] < 0.45) & (da['Quantity'] > 4)]

# print(df_posdata.shape)
# print(sum(df_posdata.groupby("Basket_ID")["Value"].sum() > 120))

# for basket_id, value in zip(grouped_baskets['Basket_ID'], grouped_baskets['Sum value']):
#     if value >= 120:
#         print(basket_id)
#         df_posdata.drop(df_posdata.index[df_posdata['Basket_ID'] == basket_id], inplace = True)
        
# df_posdata.to_pickle("posdata.pkl")
# print(df_posdata.shape)
# print(sum(df_posdata.groupby("Basket_ID")["Value"].sum() > 120))

# print(df_loyalty.describe())
# print(df_categories.describe())

# sns.set_style("whitegrid")
  
# sns.boxplot(x = 'Basket_ID', y = 'Sum quantity', data = grouped_baskets)


### export to excel file
# with pd.ExcelWriter('DATASET.VER5.xlsx') as writer:  
#     df_posdata.to_excel(writer, sheet_name='POS Data', index=False)
#     df_loyalty.to_excel(writer, sheet_name='Loyalty', index=False)
#     df_categories.to_excel(writer, sheet_name='Hierachy Categories & Barcodes', index=False)