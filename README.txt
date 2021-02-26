This project will aim to discover if there is any difference in the impact of
weather related events before the COVID pandemic and during. This is to
support the creation of a blog post or linkedin status and show off a little
of my new python skills.

The delay statistics are pulled from:
https://www.caa.co.uk/Data-and-analysis/UK-aviation-market/Flight-reliability/Datasets/UK-flight-punctuality-data/

I have chosen October 19 and October 20 as these are the most recent months
with data that have significant weather impacts during them, each having one
or more significant named winter storms, and significant poor weather. The
weather data comes from the U.K. Met Office.

The program will:
1/Discover if there is any difference in the total number of delays between the
two months
2/See whether the delays were of a greater duration.
3/Display the results in an easy to interpret form for the user.
4/Be able to use any data in the correct format to compare months and keep a
track on trends set during the COVID pandemic.
5/Source code etc will be uploaded to GitHub, so others can comment & help.

Ultimately it may be necessary to export some of the data to excel to create
visualisations.

Other functions may be added to assist the user.

==================================================

TODO list:

#TODO: Sort Destinations by early / late % needs to filter by number of
#flights being operated there - ideally at least 12 to give a good spread over
#the whole month.
#TODO: Clean Data (Remove duplicates)
#TODO: Generate stats for delays - Mean, Median, Mode, LH / SH split
#TODO: Consider data required and create Dataframe containing it. This must be
    #done to export to excel or CSV (to enable graphing). Else consider python
    #module that can create graphs. 
#TODO: (Stretch Goal) Consider dashboard / program to allow users to explore
#data - similar to bikeshare.
