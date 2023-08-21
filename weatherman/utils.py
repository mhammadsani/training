import calendar
from typing import Tuple
import weatherman_parser
from constants import (max_temp_index, min_temp_index, 
                       max_humidity_index, min_humidity_index,
                       positive_infinity, negative_infinity, 
                       hottest_day, hottest_day_date_idx, hottest_day_month_idx,
                       hottest_day_temperature_idx, montly_hottest_day, montly_hottest_temp
                       )


get_month_name = lambda month: calendar.month_name[month][:3]


def get_annual_report_of_temperature_and_humidity(year: int) -> Tuple:
    """Returns the annual report (temperature and humidity)

    Args:
        year (int):year of which you want annual report

    Returns:
        Tuple: containing every month maximum temperature,
               minimum temperature, maximum humidity and 
               minimum humidity 
    """
    
    yearly_data = weatherman_parser.weatherman[year]
    monthly_weather_data = {
        'max temperatures': [],
        'min temperatures': [],
        'max humidities': [],
        'min humidities': []
    }
    
    for month in range(1, 13):
        try:
            monthly_data = yearly_data[get_month_name(month)] 
            daily_data = {
                'max temperatures': [],
                'min temperatures': [],
                'max humidities': [],
                'min humidities': []
            }

            for day in range(len(monthly_data)):
                max_temp = monthly_data[day][max_temp_index]
                min_temp = monthly_data[day][min_temp_index]
                max_humidity = monthly_data[day][max_humidity_index] 
                min_humidity = monthly_data[day][min_humidity_index]
                
                daily_data['max temperatures'].append(
                           negative_infinity 
                           if max_temp == "" 
                           else int(max_temp))
                daily_data['min temperatures'].append(
                           positive_infinity 
                           if min_temp == "" 
                           else int(min_temp))    
                daily_data['max humidities'].append(
                           negative_infinity 
                           if max_humidity == "" 
                           else int(max_humidity))
                daily_data['min humidities'].append(
                           positive_infinity 
                           if min_humidity == "" 
                           else int(min_humidity))
                
            monthly_weather_data['max temperatures'].append(
                max(daily_data['max temperatures'])
                )
            monthly_weather_data['min temperatures'].append(
                min(daily_data['min temperatures'])
                )
            monthly_weather_data['max humidities'].append(
                max(daily_data['max humidities'])
                )
            monthly_weather_data['min humidities'].append(
                min(daily_data['min humidities'])
                )           
        except (KeyError):
            continue
        
    return (max(monthly_weather_data['max temperatures']), min(monthly_weather_data['min temperatures']),
            max(monthly_weather_data['max humidities']), min(monthly_weather_data['min humidities']))


def get_day_and_max_temperature(daily_max_temp: list) -> Tuple:
    """Returns the maximum temperature and date of that day.

    Args:
        daily_max_temp (list): a list consisting of maximum temperatures
                               of every day for a month

    Returns:
        Tuple: containing maximum temperature of month and date
    """
    daily_max = daily_max_temp[max_temp_index]
    day = 1
    for day_idx in range(len(daily_max_temp)):
        if daily_max_temp[day_idx] > daily_max:
            day = day_idx + 1
            daily_max = daily_max_temp[day_idx]
    return (day, daily_max)


def get_hottest_day_of_the_year(year: int) -> Tuple:
    """Find the hottest day of the year

    Args:
        year (int): year of which hottest day needs to be find out

    Returns:
        Tuple: containing the hottest day exact date and temperature on that day
    """
    yearly_data = weatherman_parser.weatherman[year]
    every_month_max_temps = []
    for month in range(1, 13):
        try:
            monthly_data = yearly_data[get_month_name(month)] 
            every_day_max_temps = []   
            negative_infinity = float('-inf')
            for day in range(len(monthly_data)):
                temperature = monthly_data[day][max_temp_index]
                every_day_max_temps.append(
                    int(temperature) if temperature != "" else negative_infinity
                    )
            day_and_max_temp = get_day_and_max_temperature(every_day_max_temps)
            date = (year, month, day_and_max_temp[montly_hottest_day], day_and_max_temp[montly_hottest_temp])
            every_month_max_temps.append(date)
        except KeyError:
            continue
    maximum_temperatue = 3
    hottest_days = sorted(every_month_max_temps,
                          key=lambda x: x[maximum_temperatue],
                          reverse=True)
    hottest_day_details = hottest_days[hottest_day]
    hottest_day_date = hottest_day_details[hottest_day_date_idx]
    hottest_day_month = hottest_day_details[hottest_day_month_idx]
    hottest_day_temperature = hottest_day_details[hottest_day_temperature_idx]
    return (
        f'{hottest_day_date}/{hottest_day_month}/{year}', hottest_day_temperature
        )
