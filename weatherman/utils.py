import calendar
from typing import Tuple
from constants import (
    MAX_TEMP_INDEX, MIN_TEMP_INDEX,MAX_HUMIDITY_INDEX, MIN_HUMIDITY_INDEX, POSITIVE_INFINITY, NEGATIVE_INFINITY, 
    HOTTEST_DAY, HOTTEST_DAY_DATE_INDEX, HOTTEST_DAY_MONTH_IDX, HOTTEST_DAY_TEMPERATURE_INDEX,MONTHLY_HOTTEST_TEMP,
    EMPTY, MAX_TEMPERATUES, MIN_HUMUDITIES, MAX_HUMIDITIES, MIN_TEMPERATURES, YEARLY_MAXIMUM_TEMPERATURE, 
    MONTHLY_HOTTEST_DAY
                       )
import weatherman_parser


get_month_name = lambda month: calendar.month_name[month][:3]


def get_annual_report_of_temperature_and_humidity(year: int) -> Tuple:
    """Returns the annual report (yearly max, min temperatures and humidities)

    Args:
        year (int):year of which you want annual report

    Returns:
        Tuple: containing every month maximum temperature,
               minimum temperature, maximum humidity and 
               minimum humidity 
    """
    
    yearly_data = weatherman_parser.weatherman[year]
    monthly_weather_data = {
        MAX_TEMPERATUES: [],
        MIN_TEMPERATURES: [],
        MAX_HUMIDITIES: [],
        MIN_HUMUDITIES: []
    }
    
    for month in range(1, 13):
        try:
            monthly_data = yearly_data[get_month_name(month)] 
            daily_data = {
                MAX_TEMPERATUES: [],
                MIN_TEMPERATURES: [],
                MAX_HUMIDITIES: [],
                MIN_HUMUDITIES: []
            }

            for day in range(len(monthly_data)):
                max_temp = monthly_data[day][MAX_TEMP_INDEX]
                min_temp = monthly_data[day][MIN_TEMP_INDEX]
                max_humidity = monthly_data[day][MAX_HUMIDITY_INDEX] 
                min_humidity = monthly_data[day][MIN_HUMIDITY_INDEX]
                
                daily_data[MAX_TEMPERATUES].append(
                           NEGATIVE_INFINITY 
                           if max_temp == EMPTY 
                           else int(max_temp))
                daily_data[MIN_TEMPERATURES].append(
                           POSITIVE_INFINITY 
                           if min_temp == EMPTY
                           else int(min_temp))    
                daily_data[MAX_HUMIDITIES].append(
                           NEGATIVE_INFINITY 
                           if max_humidity == EMPTY 
                           else int(max_humidity))
                daily_data[MIN_HUMUDITIES].append(
                           POSITIVE_INFINITY 
                           if min_humidity == EMPTY
                           else int(min_humidity))
                
            monthly_weather_data[MAX_TEMPERATUES].append(
                max(daily_data[MAX_TEMPERATUES])
                )
            monthly_weather_data[MIN_TEMPERATURES].append(
                min(daily_data[MIN_TEMPERATURES])
                )
            monthly_weather_data[MAX_HUMIDITIES].append(
                max(daily_data[MAX_HUMIDITIES])
                )
            monthly_weather_data[MIN_HUMUDITIES].append(
                min(daily_data[MIN_HUMUDITIES])
                )           
        except (KeyError):
            continue
        
    return (max(monthly_weather_data[MAX_TEMPERATUES]), min(monthly_weather_data[MIN_TEMPERATURES]),
            max(monthly_weather_data[MAX_HUMIDITIES]), min(monthly_weather_data[MIN_HUMUDITIES]))


def get_day_and_max_temperature(daily_max_temp: list) -> Tuple:
    """Returns the maximum temperature with date of the day

    Args:
        daily_max_temp (list): a list consisting of maximum temperatures
                               of every day for a month

    Returns:
        Tuple: containing maximum temperature of month and date
    """
    daily_max = daily_max_temp[MAX_TEMP_INDEX]
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
    monthly_max_temperatures = []
    for month in range(1, 13):
        try:
            monthly_data = yearly_data[get_month_name(month)] 
            daily_max_temperatures = []  
            for day in range(len(monthly_data)):
                temperature = monthly_data[day][MAX_TEMP_INDEX]
                daily_max_temperatures.append(
                    int(temperature) if temperature != EMPTY else NEGATIVE_INFINITY
                    )
            day_and_max_temp = get_day_and_max_temperature(daily_max_temperatures)
            date = (year, month, day_and_max_temp[MONTHLY_HOTTEST_DAY], day_and_max_temp[MONTHLY_HOTTEST_TEMP])
            monthly_max_temperatures.append(date)
        except KeyError:
            continue
    hottest_days = sorted(
        monthly_max_temperatures, key=lambda x: x[YEARLY_MAXIMUM_TEMPERATURE],reverse=True
        )
    hottest_day_date = hottest_days[HOTTEST_DAY][HOTTEST_DAY_DATE_INDEX]
    hottest_day_month = hottest_days[HOTTEST_DAY][HOTTEST_DAY_MONTH_IDX]
    hottest_day_temperature = hottest_days[HOTTEST_DAY][HOTTEST_DAY_TEMPERATURE_INDEX]
    return (
        f'{hottest_day_date}/{hottest_day_month}/{year}', hottest_day_temperature
        )
