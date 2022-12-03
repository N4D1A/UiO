#!/usr/bin/env python3
"""
Fetch data from https://www.hvakosterstrommen.no/strompris-api
and visualize it.

Assignment 5
"""

import datetime

import altair as alt
import pandas as pd
import requests
import requests_cache
import json

# install an HTTP request cache
# to avoid unnecessary repeat requests for the same data
# this will create the file http_cache.sqlite
requests_cache.install_cache()


# task 5.1:
def fetch_day_prices(date: datetime.date = None, location: str = "NO1") -> pd.DataFrame:
    """Fetch one day of data for one location from hvakosterstrommen.no API
    Arguments:
        date (datetime.date): date to fetch. if not given, the current date when the function is called
        location (set): location to fetch.
    Returns:
        df (DataFrame) : DataFrame with columns NOK_per_kWh(float) and time_start(datetime)
        ## df (dataframe) : data frame converted from data fetched from hvakosterstrommen.no API. ## 지우기!!
    """
    if date is None:
        date = datetime.date.today()
    
    assert date >= datetime.date(2022,10,2), "The date should be after October 2, 2022"

    url = f"https://www.hvakosterstrommen.no/api/v1/prices/{date.strftime('%Y')}/{date.strftime('%m')}-{date.strftime('%d')}_{location}.json"
    df = pd.DataFrame.from_dict(requests.get(url).json())
    df['time_start'] = pd.to_datetime(df['time_start'], utc=True).dt.tz_convert("Europe/Oslo")
    
    return df[['NOK_per_kWh', 'time_start']]


# LOCATION_CODES maps codes ("NO1") to names ("Oslo")
LOCATION_CODES = {
    "NO1":"Oslo",
    "NO2":"Kristiansand",
    "NO3":"Trondheim",
    "NO4":"Tromsø",
    "NO5":"Bergen",
}

# task 1:
def fetch_prices(
    end_date: datetime.date = None,
    days: int = 7,
    locations=tuple(LOCATION_CODES.keys()),
) -> pd.DataFrame:
    """Fetch prices for multiple days and locations into a single DataFrame
    Arguments:
        end_date (datetime.date): the last day of the period to fetch data
        days (int): time period to fetch data (days)
        locations (tuple): tuple of region codes of Norway
    Returns:
        df (DataFrame) : DataFrame with columns NOK_per_kWh(float), time_start(datetime), 
                        location_code(str), and location(str)
    """
    if end_date is None:
        end_date = datetime.date.today()

    df_list = []
    for i in range(days): 
    ## if you want to fetch 'days + end_date', use: for i in range(days+1)
    ## I used that as mentioned in assignment, but I got error from the test, so I changed it
        date = end_date - datetime.timedelta(days=i)
        for location in locations:
            df = fetch_day_prices(date, location)
            df['location_code'] = location
            df['location'] = LOCATION_CODES[location]
            df_list.append(df)
    
    return pd.concat(df_list).sort_values(by=['time_start'])


# task 5.1:
def plot_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot energy prices over time
    Arguments:
        df (DataFrame) : DataFrame with columns NOK_per_kWh(float), time_start(datetime), 
                        location_code(str), and location(str)
    Returns:
        chart (altair.Chart) : Multiple time series line charts with 
                                period as x-axis, price in NOK as y-axis, 
                                and each region as its own line
    """
    chart = alt.Chart(df).mark_line().encode(
            x =  alt.X('time_start:T', axis=alt.Axis(format ="%d %b %H")), # x-axis
            y = 'NOK_per_kWh:Q', # y-axis (price in NOK)
            color = 'location', # each location should get its own line
            strokeDash = 'location',
            )

    return chart


# Task 5.4

def plot_daily_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot the daily average price

    x-axis should be time_start (day resolution)
    y-axis should be price in NOK

    You may use any mark.

    Make sure to document arguments and return value...
    """
    ...


# Task 5.6

ACTIVITIES = {
    # activity name: energy cost in kW
    ...
}


def plot_activity_prices(
    df: pd.DataFrame, activity: str = "shower", minutes: float = 10
) -> alt.Chart:
    """
    Plot price for one activity by name,
    given a data frame of prices, and its duration in minutes.

    Make sure to document arguments and return value...
    """

    ...


def main():
    """Allow running this module as a script for testing."""
    df = fetch_prices()
    chart = plot_prices(df)
    # showing the chart without requiring jupyter notebook or vs code for example
    # requires altair viewer: `pip install altair_viewer`
    chart.show()
    

if __name__ == "__main__":
    main()
