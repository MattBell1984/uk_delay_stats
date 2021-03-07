import pandas as pd
import numpy as np

df_1019 = pd.read_csv('201910_Punctuality_Statistics_Full_Analysis.csv')
df_1020 = pd.read_csv('202010_Punctuality_Statistics_Full_Analysis.csv')

df = df_1019
dfb = df_1020

writer = pd.ExcelWriter('otp_multiple.xlsx')

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


def dfdetail(df1, df2):
    """
    Prints pertinent details of the database.

    Args:
        (df) df1: Data Frame of 2019 data filtered by reporting airport
        (df) df2: Data Frame of 2020 data filtered by reporting airport

    No Returns.
    """
    print("This is an overview of the data being considered:")

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
    print("Is any data missing?")
    print(df.isna().sum())



def dftopten(df1, df2):
    """ Prints the 10 best / worst performing destinations for filtered database

    Args:
        (df) df1: Data Frame of 2019 data filtered by reporting airport
        (df) df2: Data Frame of 2020 data filtered by reporting airport

    Returns:
        (df) otp2019: Pandas DataFrame containing 10 best performing routes
            in 2019 organised by on_time_or_early_percent
        (df) dla2019: Padas DataFrame containing 10 worst performing routes in
            2019 organised by on_time_or_early_percent
        (df) otp2020: Pandas DataFrame containing 10 best performing routes
            in 2020 organised by on_time_or_early_percent
        (df) dla2020: Pandas DataFrame containing 10 worst performing routes in
            2020 organised by on_time_or_early_percent
    """

#Print Below lists 10 flights with best early / ontime performance for all
#airports for 2019
    mask_df1 = (df1[df1.number_flights_matched > 4])
#>>>>> Export to Excel
    print(mask_df1[['reporting_airport', 'origin_destination',\
        'on_time_or_early_percent','num_flights_ontime']]\
        .groupby('origin_destination').agg(['mean','count']).sort_values\
        (by=('on_time_or_early_percent','mean'), ascending=False).head(10))

    otp2019 = mask_df1[['reporting_airport', 'origin_destination',\
        'on_time_or_early_percent','num_flights_ontime']]\
        .groupby('origin_destination').agg(['mean','count']).sort_values\
        (by=('on_time_or_early_percent','mean'), ascending=False).head(10)

    print("=" * 40)

#Print Below lists 10 flights with worst late performance for all
#airports
#>>>>> Export to Excel
    print(mask_df1[['reporting_airport', 'origin_destination',\
        'delay_percent', 'num_flights_delayed']]\
        .groupby('origin_destination').agg(['mean','count']).sort_values\
        (by=('delay_percent','mean'), ascending=False).head(10))

    dla2019 = mask_df1[['reporting_airport', 'origin_destination',\
        'delay_percent', 'num_flights_delayed']]\
        .groupby('origin_destination').agg(['mean','count']).sort_values\
        (by=('delay_percent','mean'), ascending=False).head(10)


    print("=" * 40)
    print("=" * 40)

#Print Below lists 10 flights with best early / ontime performance for all
#airports for 2020
#>>>>> Export to Excel
    mask_df2 = (df2[df2.number_flights_matched > 4])

    print(mask_df2[['reporting_airport', 'origin_destination',\
        'on_time_or_early_percent','num_flights_ontime']]\
        .groupby('origin_destination').agg(['mean','count']).sort_values\
        (by=('on_time_or_early_percent','mean'), ascending=False).head(10))

    otp2020 = mask_df2[['reporting_airport', 'origin_destination',\
        'on_time_or_early_percent','num_flights_ontime']]\
        .groupby('origin_destination').agg(['mean','count']).sort_values\
        (by=('on_time_or_early_percent','mean'), ascending=False).head(10)

    print("=" * 40)
#Print Below lists 10 flights with worst delay performance for all
#airports for 2020
#>>>>> Export to Excel
    print(mask_df2[['reporting_airport', 'origin_destination',\
        'delay_percent', 'num_flights_delayed']]\
        .groupby('origin_destination').agg(['mean','count']).sort_values\
        (by=('delay_percent','mean'), ascending=False).head(10))

    dla2020 = mask_df2[['reporting_airport', 'origin_destination',\
        'delay_percent', 'num_flights_delayed']]\
        .groupby('origin_destination').agg(['mean','count']).sort_values\
        (by=('delay_percent','mean'), ascending=False).head(10)

    print("=" * 40)
    print("=" * 40)

    return otp2019, dla2019, otp2020, dla2020

def headlinefigs(df1, df2):
    """ Prints a few headline figures from the filtered Pandas Dataframe

    Args:
        (df) df1: Data Frame of 2019 data filtered by reporting airport
        (df) df2: Data Frame of 2020 data filtered by reporting airport

    No Returns.
    """

    print("The average % of flights delayed in October 2019 (pre COVID)"\
        "was {}.".format(df1['delay_percent'].agg(['mean'])))

    print("The average % of flights delayed in October 2020 (post COVID)"\
        "was {}.".format(df2['delay_percent'].agg(['mean'])))

    print("The number of flights that were logged in 2019 was {}.".format(\
        (df1['number_flights_matched'] - df1['number_flights_cancelled'])\
        .agg(['sum'])))

    print("The number of flights that were logged in 2020 was {}.".format(\
        (df2['number_flights_matched'] - df2['number_flights_cancelled'])\
        .agg(['sum'])))

    print("=" * 40)

def dlafigs(df1, df2):
    """
    Displays statistics on volume and percentage of flights delayed in 2019
    and 2020

    Args:
        (df) df1: Data Frame of 2019 data filtered by reporting airport
        (df) df2: Data Frame of 2020 data filtered by reporting airport

    Returns:
        (df) dlafigs19: Pandas Dataframe with a breakdown of flights by delay
            duration, number of flights and percent of total for 2019
        (df) dlafigs20: Pandas Dataframe with a breakdown of flights by delay
            duration, number of flights and percent of total for 2020
    """

    act_flights_19 = df1['number_flights_matched'] - df1\
        ['number_flights_cancelled']

    m_15_early_19 = ((df1['flights_more_than_15_minutes_early_percent']\
         / 100) * act_flights_19).round(0).sum()
    to_1_early_19 = ((df1['flights_15_minutes_early_to_1_minute_early_percent']\
        / 100) *act_flights_19).round(0).sum()
    to_15_late_19 = ((df1['flights_0_to_15_minutes_late_percent']\
        / 100) * act_flights_19).round(0).sum()
    to_30_late_19 = ((df1['flights_between_16_and_30_minutes_late_percent']\
        / 100) * act_flights_19).round(0).sum()
    to_60_late_19 = ((df1['flights_between_31_and_60_minutes_late_percent']\
        / 100) * act_flights_19).round(0).sum()
    to_120_late_19 = ((df1['flights_between_61_and_120_minutes_late_percent']\
        / 100) * act_flights_19).round(0).sum()
    to_180_late_19 = ((df1['flights_between_121_and_180_minutes_late_percent']\
        / 100) * act_flights_19).round(0).sum()
    to_360_late_19 = ((df1['flights_between_181_and_360_minutes_late_percent']\
        / 100) * act_flights_19).round(0).sum()
    g_360_late_19 = ((df1['flights_more_than_360_minutes_late_percent']\
        / 100) * act_flights_19).round(0).sum()


    e15pc19 = (df1['flights_more_than_15_minutes_early_percent']).mean()
    e1pc19 = (df1['flights_15_minutes_early_to_1_minute_early_percent']).mean()
    t15pc19 = (df1['flights_0_to_15_minutes_late_percent']).mean()
    t30pc19 = (df1['flights_between_16_and_30_minutes_late_percent']).mean()
    t60pc19 = (df1['flights_between_31_and_60_minutes_late_percent']).mean()
    t120pc19 = (df1['flights_between_61_and_120_minutes_late_percent']).mean()
    t180pc19 = (df1['flights_between_121_and_180_minutes_late_percent']).mean()
    t360pc19 = (df1['flights_between_181_and_360_minutes_late_percent']).mean()
    g360pc19 = (df1['flights_more_than_360_minutes_late_percent']).mean()

    print("The breakdown of flights for 2019 (total num flights) was:")
#>>>>> Export to Excel (somehow)
    print("{} - more than 15 mins early \n{} - 15 mins to 1 min early".format\
        (m_15_early_19, to_1_early_19))
    print("{} - to 15 mins late \n{} - 16 to 30 mins late \n{} - 31 to"\
        "60 mins late".format(to_15_late_19, to_30_late_19, to_60_late_19))
    print("{} - 61 to 120 mins late \n{} - 121 to 180 mins late"\
        .format(to_120_late_19, to_180_late_19))
    print("{} - 181 to 360 mins late \n{} - more than 360 mins late"\
        .format(to_360_late_19, g_360_late_19))

    print("The average % for each delay category in 2019 was:")

    print("{} - more than 15 mins early \n{} - 15 mins to 1 min early".format\
        (e15pc19, e1pc19))
    print("{} - to 15 mins late \n{} - 16 to 30 mins late \n{} - 31 to 60"\
        "mins late".format(t15pc19, t30pc19, t60pc19))
    print("{} - 61 to 120 mins late \n{} - 121 to 180 mins late"\
        .format(t120pc19, t180pc19))
    print("{} - 181 to 360 mins late \n{} - more than 360 mins late"\
        .format(t360pc19, g360pc19))

    dla_breakdown_19 = {
        'Delay Time (mins)' :['> 15 early', '15 - 0 early', \
        '0 - 15 late', '16 - 30 late', '31 - 60 late', '61 - 120 late',\
        '121 - 180 late', '181 - 360 late', '>360 mins late'],
        'number' :[m_15_early_19, to_1_early_19, to_15_late_19, to_30_late_19,\
        to_60_late_19, to_120_late_19, to_180_late_19, to_360_late_19, \
        g_360_late_19],
        'percent' :[e15pc19, e1pc19, t15pc19, t30pc19, t60pc19, t120pc19,\
        t180pc19,t360pc19, g360pc19]
        }

    dlafigs19 = pd.DataFrame(data= dla_breakdown_19)



    print("=" * 40)

    act_flights_20 = df2['number_flights_matched'] -\
        df2['number_flights_cancelled']

    m_15_early_20 = ((df2['flights_more_than_15_minutes_early_percent']\
        / 100) * act_flights_20).round(0).sum()
    to_1_early_20 = ((df2['flights_15_minutes_early_to_1_minute_early_percent']\
        / 100) *act_flights_19).round(0).sum()
    to_15_late_20 = ((df2['flights_0_to_15_minutes_late_percent']  / 100) *\
        act_flights_20).round(0).sum()
    to_30_late_20 = ((df2['flights_between_16_and_30_minutes_late_percent']\
        / 100) * act_flights_20).round(0).sum()
    to_60_late_20 = ((df2['flights_between_31_and_60_minutes_late_percent']\
        / 100) * act_flights_20).round(0).sum()
    to_120_late_20 = ((df2['flights_between_61_and_120_minutes_late_percent']\
        / 100) * act_flights_20).round(0).sum()
    to_180_late_20 = ((df2['flights_between_121_and_180_minutes_late_percent']\
        / 100) * act_flights_20).round(0).sum()
    to_360_late_20 = ((df2['flights_between_181_and_360_minutes_late_percent']\
        / 100) * act_flights_20).round(0).sum()
    g_360_late_20 = ((df2['flights_more_than_360_minutes_late_percent']\
        / 100) * act_flights_20).round(0).sum()

    e15pc20 = (df2['flights_more_than_15_minutes_early_percent']).mean()
    e1pc20 = (df2['flights_15_minutes_early_to_1_minute_early_percent']).mean()
    t15pc20 = (df2['flights_0_to_15_minutes_late_percent']).mean()
    t30pc20 = (df2['flights_between_16_and_30_minutes_late_percent']).mean()
    t60pc20 = (df2['flights_between_31_and_60_minutes_late_percent']).mean()
    t120pc20 = (df2['flights_between_61_and_120_minutes_late_percent']).mean()
    t180pc20 = (df2['flights_between_121_and_180_minutes_late_percent']).mean()
    t360pc20 = (df2['flights_between_181_and_360_minutes_late_percent']).mean()
    g360pc20 = (df2['flights_more_than_360_minutes_late_percent']).mean()


    print("The breakdown of flights for 2020 (total num flights) was:")

    print("{} - more than 15 mins early \n{} - 15 mins to 1 min early".format\
        (m_15_early_20, to_1_early_20))
    print("{} - to 15 mins late \n{} - 16 to 30 mins late \n{} - 31 to 60"\
        " mins late".format(to_15_late_20, to_30_late_19, to_60_late_20))
    print("{} - 61 to 120 mins late \n{} - 121 to 180 mins late"\
        .format(to_120_late_20, to_180_late_20))
    print("{} - 181 to 360 mins late \n{} - more than 360 mins late"\
        .format(to_360_late_20, g_360_late_20))

    dla_breakdown_20 = {
        'Delay Time (mins)' :['> 15 early', '15 - 0 early', \
        '0 - 15 late', '16 - 30 late', '31 - 60 late', '61 - 120 late',\
        '121 - 180 late', '181 - 360 late', '>360 mins late'],
        'number' :[m_15_early_20, to_1_early_20, to_15_late_20, to_30_late_20,\
        to_60_late_20, to_120_late_20, to_180_late_20, to_360_late_20, \
        g_360_late_20],
        'percent' :[e15pc20, e1pc20, t15pc20, t30pc20, t60pc20, t120pc20,\
        t180pc20, t360pc20, g360pc20]
        }

    dlafigs20 = pd.DataFrame(data= dla_breakdown_20)

    print("The average % for each delay category in 2020 was:")

    print("{} - more than 15 mins early \n{} - 15 mins to 1 min early".format\
        (e15pc20, e1pc20))
    print("{} - to 15 mins late \n{} - 16 to 30 mins late \n{} - 31 to 60 mins" \
        " late".format(t15pc20, t30pc20, t60pc20))
    print("{} - 61 to 120 mins late \n{} - 121 to 180 mins late"\
        .format(t120pc20, t180pc20))
    print("{} - 181 to 360 mins late \n{} - more than 360 mins late"\
        .format(t360pc20, g360pc20))

    return dlafigs19, dlafigs20


def excelwrite(otp2019, dla2019, otp2020, dla2020, dlafigs19, dlafigs20):
    """
    Exports data generated to Excel

    Args:
    (df) otp2019: Pandas DataFrame containing 10 best performing routes
        in 2019 organised by on_time_or_early_percent
    (df) dla2019: Padas DataFrame containing 10 worst performing routes in
        2019 organised by on_time_or_early_percent
    (df) otp2020: Pandas DataFrame containing 10 best performing routes
        in 2020 organised by on_time_or_early_percent
    (df) dla2020: Pandas DataFrame containing 10 worst performing routes in
        2020 organised by on_time_or_early_percent
    (df) dlafigs19: Pandas Dataframe with a breakdown of flights by delay
        duration, number of flights and percent of total for 2019
    (df) dlafigs20: Pandas Dataframe with a breakdown of flights by delay
        duration, number of flights and percent of total for 2020
    """

    otp2019.to_excel(writer, sheet_name='otp2019')
    dla2019.to_excel(writer, sheet_name='dla2019')
    otp2020.to_excel(writer, sheet_name='otp2020')
    dla2020.to_excel(writer, sheet_name='dla2020')
    dlafigs19.to_excel(writer, sheet_name= 'dlafigs19')
    dlafigs20.to_excel(writer, sheet_name= 'dlafigs20')

    writer.save()

def main():
    while True:
        dfdetail(df1, df2)
        dftopten(df1, df2)
        headlinefigs(df1, df2)
        dlafigs(df1, df2)
        excelwrite(otp2019, dla2019, otp2020, dla2020, dlafigs19, dlafigs20)


if __name__ == "__main__":
	main()
#TODO: Generate stats for delays - Mean, Median, Mode, LH / SH split
#TODO: Consider data required and create Dataframe containing it. This must be
    #done to export to excel or CSV (to enable graphing). Else consider python
    #module that can create graphs.
#TODO: (Stretch Goal) Consider dashboard / program to allow users to explore
#data - similar to bikeshare.

#Then we need to find out what % for each destiantion was delayed


#Then we need to split by date - use run_date or reporting_period
