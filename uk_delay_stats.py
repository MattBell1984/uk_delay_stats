#Investigate delay statistics at UK airport and compare whether the COVID-19
#pandemic has had an effect on delays due to severe weather events

import pandas as pd
import numpy as np

#read files and import rows
df_1019 = pd.read_csv('201910_Punctuality_Statistics_Full_Analysis.csv')
df_1020 = pd.read_csv('202010_Punctuality_Statistics_Full_Analysis.csv')

df = pd.concat([df_1019, df_1020], ignore_index=True )

#investigate database structure

print("Number of rows: " + str(len(df)))

print(df.shape)

#reshape df to only consider useful information
#df should only have date, departure, dest, sum of early/late/canx flights

df['on_time_or_early_percent'] =\
    df['flights_more_than_15_minutes_early_percent'] +\
    df['flights_15_minutes_early_to_1_minute_early_percent']

df['delay_percent'] = df.loc[:,'flights_0_to_15_minutes_late_percent':'flights_more_than_360_minutes_late_percent'].sum(axis = 1)

print(df.columns)


#check for NaN

#print(df.isna().sum())

#there are no NaN - function de activated

#Choose airports to compare

print("There are {} unique origin countries considered".format\
    (df['origin_destination_country'].nunique()))

print("There are {} unique origins".format(df['origin_destination'].nunique()))

print("The origin countries are:")
print(df.origin_destination_country.unique())

print("The unique origins are:")
print(df.origin_destination.unique())

#Can slice either by Country (UK) or Airport. Lets choose Heathrow &
#Gatwick initially. Limit to 10 rows for readability.

destlist = ['HEATHROW', 'GATWICK']

df1 = df[df.reporting_airport.isin(destlist)]

#This returns the values for all flights that originated from the airports in
#the destlist list.

print(df1[['origin_destination_country', 'reporting_airport',\
    'origin_destination','number_flights_matched', 'on_time_or_early_percent',\
    'delay_percent']].head(10))

#Then we need to find out what % for each destiantion was delayed


#Then we need to split by date - use run_date or reporting_period
