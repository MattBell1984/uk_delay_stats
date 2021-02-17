import pandas as pd
import numpy as np

df_1019 = pd.read_csv('201910_Punctuality_Statistics_Full_Analysis.csv')
df_1020 = pd.read_csv('202010_Punctuality_Statistics_Full_Analysis.csv')

df = pd.concat([df_1019, df_1020], ignore_index=True )

#Read files & combine

destlist = ['HEATHROW', 'GATWICK']

df1 = df[df.reporting_airport.isin(destlist)].copy()

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

#check for NaN

#print(df.isna().sum())

#there are no NaN - function de activated

aggregation_functions = {'reporting_period': 'first',\
    'reporting_airport': 'first', 'origin_destination_country': 'first',\
    'origin_destination': 'first', 'number_flights_matched': 'sum',\
    'num_flights_ontime': 'sum', 'num_flights_delayed': 'sum'}

df1 = df1.groupby(df1['origin_destination']).aggregate(aggregation_functions)

df1 = df1.sort_values('reporting_airport')

print(df1[['reporting_period', 'reporting_airport',\
    'origin_destination_country',\
    'number_flights_matched', 'num_flights_ontime',\
    'num_flights_delayed',]].head(10))

#Displays selected columns from filtered database & limits to first 10 rows


#TODO: Clean Data (Remove duplicates) - This is caused by different airlines
#flying to the same destination. flights should be combined before the
#percentages are generated
#TODO: Organise by Date
#TODO: Generate stats for delays - Mean, Median, Mode, LH / SH split
#TODO: Pull all data together.
#TODO: (Stretch Goal) Consider dashboard / program to allow users to explore
#data - similar to bikeshare.

#Then we need to find out what % for each destiantion was delayed


#Then we need to split by date - use run_date or reporting_period
