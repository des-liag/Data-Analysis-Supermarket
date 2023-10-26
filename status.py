import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
import seaborn as sns

# # read xlxs
# df1 = pd.read_excel('DATASET.VER5.xlsx', sheet_name='POS Data', index_col=None)
# df2 = pd.read_excel('DATASET.VER5.xlsx', sheet_name='Loyalty', index_col=None)
# df3 = pd.read_excel('DATASET.VER5.xlsx', sheet_name='Hierachy Categories & Barcodes', index_col=None)

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


# print(sum(df_loyalty["Status"] == "Family"))
# print(sum(df_loyalty["Status"] == "man"))
# print(sum(df_loyalty["Status"] == "Woman"))
# print(sum(df_loyalty["Status"] == "Elder"))
# print(sum(df_loyalty["Status"] == "couple"))



# print(df_loyalty.shape)

# print(len((pd.unique(df_loyalty['Cardholder']))))
# print(sum(df_loyalty["Status"] == "na"))
# print(df_loyalty.loc[df_loyalty["Status"] == "na"])



# ## df_posdata = df_loyalty.join(on='Cardholder')
# # print(df_posdata)
# df_posdata.rename(columns = {'LoyaltyCard_ID':'Cardholder'}, inplace = True)
# # print(df_posdata)

# not_available = pd.merge(df_posdata, df_loyalty, on ='Cardholder')
# # print(total_df)
# not_available = not_available.loc[not_available["Status"] == "na"]
# not_available.drop(["Date", "Quantity", "Value"], axis=1, inplace=True)

# not_available = pd.merge(df_categories, not_available, on ='Barcode')
# not_available.drop(["Category A", "Category B"], axis=1, inplace=True)

# not_available = not_available[
#     (not_available["Category C"] == "ΑΝΔΡΙΚΑ") | (not_available["Category C"] == "ΓΥΝΑΙΚΕΙΑ") | (not_available["Category C"] == "ΠΑΙΔΙΚΑ") |
#     (not_available["Category Final"] == "ΠΑΙΔΙΚΗ ΠΕΡΙΠΟΙΗΣΗ") | (not_available["Category Final"] == "ΠΕΡΙΠΟΙΗΣΗ ΠΡΟΣΩΠΟΥ") |
#     (not_available["Category Final"] == "ΒΡΕΦΙΚΗ ΤΡΟΦΗ") | (not_available["Category Final"] == "ΓΥΝΑΙΚΕΙΑ ΥΓΙΕΙΝΗ") |
#     (not_available["Category Final"] == "ΠΑΝΕΣ ΑΚΡΑΤΕΙΑΣ") | (not_available["Category Final"] == "ΠΑΝΕΣ ΠΑΙΔΙΚΕΣ") ]

# # print(not_available)
# # print(not_available.info())
# # print(not_available.shape)
# # print(len(pd.unique(not_available['Cardholder'])))

# grouped_na = not_available.groupby('Cardholder')
# # print(grouped_na.first())
# # print(grouped_na.get_group(293782))
# # purchases = grouped_na.get_group(28854105)
# # print(type(purchases))

# for card in pd.unique(not_available['Cardholder']):
#     # print(card)
#     # print(grouped_na.get_group(card))
#     purchases = grouped_na.get_group(card)
#     # print(purchases)

#     man = 0
#     woman = 0
#     family = 0
#     elder = 0
#     for index, row in purchases.iterrows():
#         if (row["Category C"] == "ΑΝΔΡΙΚΑ"):
#             man = man + 1
#         elif ((row["Category C"] == "ΓΥΝΑΙΚΕΙΑ") or (row["Category Final"] == "ΠΕΡΙΠΟΙΗΣΗ ΠΡΟΣΩΠΟΥ") or (row["Category Final"] == "ΓΥΝΑΙΚΕΙΑ ΥΓΙΕΙΝΗ")):
#             woman = woman + 1
#         elif ((row["Category C"] == "ΠΑΙΔΙΚΑ") or (row["Category Final"] == "ΠΑΙΔΙΚΗ ΠΕΡΙΠΟΙΗΣΗ") or (row["Category Final"] == "ΒΡΕΦΙΚΗ ΤΡΟΦΗ") or (row["Category Final"] == "ΠΑΝΕΣ ΠΑΙΔΙΚΕΣ")):
#             family = family + 1
#         elif((row["Category Final"] == "ΠΑΝΕΣ ΑΚΡΑΤΕΙΑΣ")):
#             elder = elder + 1

#     max = man
#     status = "man"
#     if(woman > max):
#         max = woman
#         status = "Woman"
#     if(family > max):
#         max = family
#         status = "Family"
#     if(elder > max):
#         max = elder
#         status = "Elder"

#     # print(purchases)
#     # print(df_loyalty.loc[df_loyalty["Cardholder"] == card])
#     df_loyalty.loc[df_loyalty["Cardholder"] == card, "Status"] = status
#     # print(df_loyalty.loc[df_loyalty["Cardholder"] == card])

    

# # print(not_available.loc[not_available["Cardholder"] == 28325357])

# # print(sum(df_loyalty["Status"] == "na"))

# df_loyalty.to_pickle("loyalty.pkl")

### export to excel file
# with pd.ExcelWriter('LOYALTY.VER2.xlsx') as writer:  
#     df_posdata.to_excel(writer, sheet_name='POS Data', index=False)
#     df_loyalty.to_excel(writer, sheet_name='Loyalty', index=False)
#     df_categories.to_excel(writer, sheet_name='Hierachy Categories & Barcodes', index=False)