import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Metadata_Country_API_NY.GDP.MKTP.CD_DS2_en_csv_v2_6298258.csv', index_col=0)

data["Duration"].plot(kind = 'hist')

plt.show()

# print("*****")
# print(data.head())



# data = data.loc[data.columns.str.contains('Unnamed')]
# print(data)

