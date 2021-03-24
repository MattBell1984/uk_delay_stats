df_1019 = pd.read_csv('201910_Punctuality_Statistics_Full_Analysis.csv')
df_1020 = pd.read_csv('202010_Punctuality_Statistics_Full_Analysis.csv')

df = pd.concat([df_1019, df_1020], ignore_index=True )

#Read files & combine

destlist = ['HEATHROW', 'GATWICK']

df1 = df[df.reporting_airport.isin(destlist)]

#Create new df dealing with just airports named in destlist

df1['on_time_or_early_percent'] =\
    df1['flights_more_than_15_minutes_early_percent'] +\
    df1['flights_15_minutes_early_to_1_minute_early_percent']

df1['delay_percent'] = df.loc[:,'flights_0_to_15_minutes_late_percent':'flights_more_than_360_minutes_late_percent'].sum(axis = 1)

print(df.columns)

#Sums up delay % for each destination + airline combo. Gives measure of whether
#on time or early.
