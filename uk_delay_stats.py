import pandas as pd
import numpy as np

df_1019 = pd.read_csv('201910_Punctuality_Statistics_Full_Analysis.csv')
df_1020 = pd.read_csv('202010_Punctuality_Statistics_Full_Analysis.csv')

df = df_1019
dfb = df_1020


destlist = ['HEATHROW', 'GATWICK']

df1 = df[df['reporting_airport'].isin(destlist)].copy()
df2 = dfb[dfb['reporting_airport'].isin(destlist)].copy()
#Creates new df dealing with just airports named in destlist. .copy() method
#prevents setcopywarning in delay_percent creation.

df1['on_time_or_early_percent'] =\
    df1['flights_more_than_15_minutes_early_percent'] +\
    df1['flights_15_minutes_early_to_1_minute_early_percent']

df1['delay_percent'] = df1.loc[:,'flights_0_to_15_minutes_late_percent'\
    :'flights_more_than_360_minutes_late_percent'].sum(axis = 1)

#Creates new column summing early or late percentages

df1['num_flights_delayed'] = (df1['number_flights_matched'] -\
    df1['number_flights_cancelled']) * (df1['delay_percent'] / 100)

df1['num_flights_delayed'] = df1['num_flights_delayed'].round(0).astype(int)

df1['num_flights_ontime'] = (df1['number_flights_matched'] -\
    df1['number_flights_cancelled']) * (df1['on_time_or_early_percent'] / 100)

df1['num_flights_ontime'] = df1['num_flights_ontime'].round(0).astype(int)

#uses percentage ontime or early to calculate raw number of flights early or
#late



print(df1.columns)


print("Number of rows: " + str(len(df1)))

print(df1.shape)

print("There are {} unique origin countries considered".format\
    (df1['origin_destination_country'].nunique()))

print("There are {} unique origins".format(df1['origin_destination'].nunique()))

print("=" * 40)

print("The origin countries are:")
print(df1.origin_destination_country.unique())

print("=" * 40)

print("The unique origins are:")
print(df1.origin_destination.unique())

print("=" * 40)
print("=" * 40)
#check for NaN

#print(df.isna().sum())

#there are no NaN - function de activated

#aggregation_functions = {'reporting_period': 'first',\
    #'reporting_airport': 'first', 'origin_destination_country': 'first',\
    #'origin_destination': 'first', 'number_flights_matched': 'sum',\
    #'num_flights_ontime': 'sum', 'num_flights_delayed': 'sum'}

#df1 = df1.groupby(df1['origin_destination']).aggregate(aggregation_functions)

#df1 = df1.sort_values('reporting_airport')


df2['on_time_or_early_percent'] =\
    df2['flights_more_than_15_minutes_early_percent'] +\
    df2['flights_15_minutes_early_to_1_minute_early_percent']

df2['delay_percent'] = df2.loc[:,'flights_0_to_15_minutes_late_percent'\
    :'flights_more_than_360_minutes_late_percent'].sum(axis = 1)

#Creates new column summing early or late percentages

df2['num_flights_delayed'] = (df2['number_flights_matched'] -\
    df2['number_flights_cancelled']) * (df2['delay_percent'] / 100)

df2['num_flights_delayed'] = df2['num_flights_delayed'].round(0).astype(int)

df2['num_flights_ontime'] = (df2['number_flights_matched'] -\
    df2['number_flights_cancelled']) * (df2['on_time_or_early_percent'] / 100)

df2['num_flights_ontime'] = df2['num_flights_ontime'].round(0).astype(int)

# Print Below Prints raw data for destination, num flights ontime, % delayed,
#% for 2019 (limited to 10)
print(df1.groupby(['origin_destination', 'reporting_airport',\
    'number_flights_matched']).agg({'num_flights_ontime':\
    np.sum, 'on_time_or_early_percent': np.mean, 'num_flights_delayed':\
    np.sum, 'delay_percent': np.mean}).head(10))



print("=" * 40)

#Print Below lists number of flights ontime, delayed as raw number of flights
#for 2019
print(df1[['reporting_period', 'reporting_airport',\
    'origin_destination_country','origin_destination',\
    'number_flights_matched', 'num_flights_ontime',\
    'num_flights_delayed']].head(10))

print("=" * 40)

#Print Below lists 10 flights with best early / ontime performance for all
#airports for 2019


print(df1[['reporting_airport', 'origin_destination',\
    'on_time_or_early_percent','num_flights_ontime']]\
    .groupby('origin_destination').agg(['mean','count']).sort_values\
    (by=('on_time_or_early_percent','mean'), ascending=False).head(10))

print("=" * 40)
#Print Below lists 10 flights with worst late performance for all
#airports

print(df1[['reporting_airport', 'origin_destination',\
    'delay_percent', 'num_flights_delayed']]\
    .groupby('origin_destination').agg(['mean','count']).sort_values\
    (by=('delay_percent','mean'), ascending=False).head(10))

print("=" * 40)
print("=" * 40)


#Print Below shows all flights in Alphabet order with num matched vs early
#late for 2020
print(df2.groupby(['origin_destination', 'reporting_airport',\
    'number_flights_matched']).agg({'num_flights_ontime':\
    np.sum, 'on_time_or_early_percent': np.mean, 'num_flights_delayed':\
    np.sum, 'delay_percent': np.mean}).head(10))



print("=" * 40)

#Lists all flights for 2020 with numbers of flights
print(df2[['reporting_period', 'reporting_airport',\
    'origin_destination_country','origin_destination',\
    'number_flights_matched', 'num_flights_ontime',\
    'num_flights_delayed']].head(10))

print("=" * 40)

#Print Below lists 10 flights with best early / ontime performance for all
#airports for 2020

print(df2[['reporting_airport', 'origin_destination',\
    'on_time_or_early_percent','num_flights_ontime']]\
    .groupby('origin_destination').agg(['mean','count']).sort_values\
    (by=('on_time_or_early_percent','mean'), ascending=False).head(10))

print("=" * 40)
#Print Below lists 10 flights with worst delay performance for all
#airports for 2020

print(df2[['reporting_airport', 'origin_destination',\
    'delay_percent', 'num_flights_delayed']]\
    .groupby('origin_destination').agg(['mean','count']).sort_values\
    (by=('delay_percent','mean'), ascending=False).head(10))

print("=" * 40)
print("=" * 40)

print("The average % of flights delayed in October 2019 (pre COVID) was {}."\
    .format(df1['delay_percent'].agg(['mean'])))

print("The average % of flights delayed in October 2020 (post COVID) was {}."\
    .format(df2['delay_percent'].agg(['mean'])))

print("The number of flights that were logged in 2019 was {}.".format(\
    (df1['number_flights_matched'] - df1['number_flights_cancelled'])\
    .agg(['sum'])))

print("The number of flights that were logged in 2020 was {}.".format(\
    (df2['number_flights_matched'] - df2['number_flights_cancelled'])\
    .agg(['sum'])))


#TODO: Sort Destinations by early / late % needs to filter by number of
#flights being operated there - ideally at least 12 to give a good spread over
#the whole month.

#TODO: Generate stats for delays - Mean, Median, Mode, LH / SH split
#TODO: Pull all data together.
#TODO: (Stretch Goal) Consider dashboard / program to allow users to explore
#data - similar to bikeshare.

#Then we need to find out what % for each destiantion was delayed


#Then we need to split by date - use run_date or reporting_period
