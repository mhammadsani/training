import argparse 
import csv
import calendar
from typing import Tuple



weatherman = {}


def get_month_name(month: int) -> str:
    return calendar.month_name[month][:3]


def read_files(weatherman_files_path: str) -> None:
    """Reads the content in data directory to main dictionary
    
    data directory is the path where data exist and main dictionary is 
    globally available variable which will store data is certain format
    """
    for year in range(1996, 2012):
        weatherman[year] = {}
        for month in range(1, 13):
            file_name = f'lahore_weather_{year}_{get_month_name(month)}.txt'
            try:
               with open(f"{weatherman_files_path}/{file_name}", 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                days_raw_data = [day for day in csv_reader]
                days = [days_raw_data[day][1:] for day in range(2, len(days_raw_data) - 1)]
                weatherman[year][get_month_name(month)] = days
            except FileNotFoundError:
                continue
   
            
def get_annual_report_of_temperature_and_humidity(year: int) -> Tuple:
    """Calculate the annual report (temperature and humidity)
    
    Function has one parameter year of which temperature and humidity
    needs to be calculated and returns a tuple of overall maximum and minumum
    temperatues and overall maximum and minimum humidity for the given specific
    year.
    """
    yearly_data = weatherman[year]
    every_month_max_temp = []
    every_month_min_temp = []
    every_month_max_humidity = []
    every_month_min_humidity = []
    
    for month in range(1, 13):
        try:
            monthly_data = yearly_data[get_month_name(month)] 
            day_important_information = {}
            
            day_important_information["everyday_max_temps"] = []
            day_important_information["everyday_min_temps"] = []
            day_important_information["everyday_max_humidities"] = []
            day_important_information["everyday_min_humidities"] = []
            max_temp_index = 0
            min_temp_index = 2
            max_humidity_index = 6
            min_humidity_index = 8
            positive_infinity = float('+inf')
            negative_infinity = float('-inf')
            for day in range(len(monthly_data)):
                max_temp = monthly_data[day][max_temp_index]
                min_temp = monthly_data[day][min_temp_index]
                max_humidity = monthly_data[day][max_humidity_index] 
                min_humidity = monthly_data[day][min_humidity_index]
                
                day_important_information['everyday_max_temps'].\
                    append(negative_infinity if max_temp == "" else int(max_temp))
                day_important_information['everyday_min_temps'].\
                    append(positive_infinity if min_temp == "" else int(min_temp))    
                day_important_information['everyday_max_humidities'].\
                    append(negative_infinity if max_humidity == "" else int(max_humidity))
                day_important_information['everyday_min_humidities'].\
                    append(positive_infinity if min_humidity == "" else int(min_humidity))
                
            every_month_max_temp.append(max(day_important_information['everyday_max_temps']))
            every_month_min_temp.append(min(day_important_information['everyday_min_temps']))
            every_month_max_humidity.append(max(day_important_information['everyday_max_humidities']))
            every_month_min_humidity.append(min(day_important_information['everyday_min_humidities']))           
        except (KeyError, ValueError):
            continue
        
    return (max(every_month_max_temp), min(every_month_min_temp), \
            max(every_month_max_humidity), min(every_month_min_humidity))


#### Task 2
def get_day_and_max_temperature(daily_max_temp: list) -> Tuple:  # helper function for hottest day of eachy year
    """ Find the maximum temperature and date of that day.
    """
    daily_max = daily_max_temp[0]
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
    yearly_data = weatherman[year]
    every_month_max_temps = []
    for month in range(1, 13):
        try:
            monthly_data = yearly_data[get_month_name(month)] 
            every_day_max_temps = []   
            negative_infinity = float('-inf')
            for day in range(len(monthly_data)):
                temperature = monthly_data[day][0]
                every_day_max_temps.append(int(temperature) if temperature != "" else negative_infinity)
            day_and_max_temp = get_day_and_max_temperature(every_day_max_temps)
            date = (year, month, day_and_max_temp[0], day_and_max_temp[1])
            every_month_max_temps.append(date)
        except KeyError:
            continue
    maximum_temperatue = 3
    hottest_days = sorted(every_month_max_temps, key=lambda x: x[maximum_temperatue], reverse=True)
    hottest_day = 0
    hottest_day_details = hottest_days[hottest_day]
    hottest_day_date = 2
    hottest_day_month = 1
    hottest_day_temperature = 3
    return (f'{hottest_day_details[hottest_day_date]}/{hottest_day_details[hottest_day_month]}/{year}', hottest_day_details[hottest_day_temperature])


def annual_report_of_temperature_and_humidity() -> None:
    print("Year        MAX Temp        MIN Temp        MAX Humidity        MIN Humidity")
    print("--------------------------------------------------------------------------")
    for year in range(1996, 2012):
        weather_values = get_annual_report_of_temperature_and_humidity(year)
        print(f'{year} {str(weather_values[0]).rjust(12)} {str(weather_values[1]).rjust(15)} {str(weather_values[2]).rjust(15)} {str(weather_values[3]).rjust(20)}')
            
            
def hottest_day_of_each_year() -> None:
    print("Year        Date          Temp")
    print("------------------------------")
    for year in range(1996, 2011):
        date, temp = get_hottest_day_of_the_year(year)
        print(f'{str(year)} {date.rjust(15)} {str(temp).rjust(8)}')



def parse_arguments() -> object:
    """Parse the command line arguments into object

    Returns:
        object with report and weatehrman_data_path as attributes
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("report", help="report# 1 for Annual Temperature and 2 for Hottest Day of the year")
    parser.add_argument("weatherman_files_path", help="data_dir")
    args = parser.parse_args()    
    return args


def perform_task(args: object) -> None:
    """Perform the specified task based from tasks

    Args:
        args (object): object having attributes report and weatherman_files_path
    """
    
    tasks = {
    '1': 'annual report', 
    '2': 'hottest day'
    }
    try:
        if tasks[args.report] == 'annual report':
            annual_report_of_temperature_and_humidity()
        elif tasks[args.report] == 'hottest day':
            hottest_day_of_each_year()
    except KeyError:
        print("1 for Annual Temperature and 2 for Hottest Day of the year")


def main() -> None:
    if __name__ == "__main__":
        args = parse_arguments()
        read_files(args.weatherman_files_path)
        perform_task(args)

main()


