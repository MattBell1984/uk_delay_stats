#Investigate delay statistics at UK airport and compare whether the COVID-19
#pandemic has had an effect on delays due to severe weather events

import pandas as pd

#read files and import rows
df_1019 = pd.read_csv('201910_Punctuality_Statistics_Full_Analysis.csv')
df_1020 = pd.read_csv('202010_Punctuality_Statistics_Full_Analysis.csv')

df = pd.concat([df_1019, df_1020], ignore_index=True )

#print total number of rows

print("Number of rows: " + str(len(df)))




#Choose airports to compare
