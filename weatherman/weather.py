import argparse 
import csv


main_dic = {}
number_to_months = {
    1: 'Jan', 
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}


def file_reading(data_directory) -> None:
    """Reads the content in data directory to main dictionary
    
    data directory is the path where data exist and main dictionary is 
    globally available variable which will store data is certain format
    """
    for year in range(1996, 2012):
        main_dic[year] = {}
        for month_number in range(1, 13):
            file_name = f'lahore_weather_{year}_{number_to_months[month_number]}.txt'
            try:
               with open(f"{data_directory}/{file_name}", 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    file_data = []
                    for row in csv_reader:
                        file_data.append(row)
                    
                    all_days = []
                    for row in range(2, len(file_data)- 1):
                        day = file_data[row][1:]
                        all_days.append(day)
                    
                    main_dic[year][number_to_months[month_number]] = all_days
            
            except FileNotFoundError:  # as some files do not exist like 1996 Jan
                continue
   
            
def annual_report_of_temperature_and_humidity_helper(year: int) -> tuple:
    """Calculate the annual report (temperature and humidity)
    
    Function has one parameter year of which temperature and humidity
    needs to be calculated and returns a tuple of overall maximum and minumum
    temperatues and overall maximum and minimum humidity for the given specific
    year.
    """
    year_data = main_dic[year]
    every_month_max_temp = []
    every_month_min_temp = []
    every_month_max_humidity = []
    every_month_min_humidity = []
    
    for month_number in range(1, 13):
        try:
            monthly_data = year_data[number_to_months[month_number]] 
            every_day_max_temp = []
            every_day_min_temp = []
            every_day_max_humidity = []
            every_day_min_humidity = []   
            
            for day in range(len(monthly_data)):
                max_temp = monthly_data[day][0]  # index 0 has max temp
                min_temp = monthly_data[day][2]  # index 2 has min temp
                max_humidity = monthly_data[day][6] 
                min_humidity = monthly_data[day][8]
                
                if max_temp == "":  # some values are missing
                    every_day_max_temp.append(float('-inf'))
                else:
                    every_day_max_temp.append(int(max_temp))
                
                if min_temp == "":
                    every_day_min_temp.append(float('+inf'))
                else:
                    every_day_min_temp.append(int(min_temp)) 
                    
                if max_humidity == "":
                    every_day_max_humidity.append(float('-inf'))
                else:
                    every_day_max_humidity.append(int(max_humidity))
                    
                if min_humidity == "":
                    every_day_max_humidity.append(float('-inf'))
                else:
                    every_day_min_humidity.append(int(min_humidity))
                
            every_month_max_temp.append(max(every_day_max_temp))
            every_month_min_temp.append(min(every_day_min_temp))
            every_month_max_humidity.append(max(every_day_max_humidity))
            every_month_min_humidity.append(max(every_day_min_humidity))
                    
        except (KeyError, ValueError):
            continue
        
    return (max(every_month_max_temp), min(every_month_min_temp), max(every_month_max_humidity), min(every_month_min_humidity))


#### Task 2
def custom_max(daily_max_temp: list) -> tuple:  # helper function for hottest day of eachy year
    """ Find the maximum temperature and date of that day.
    
    Custom max takes list of daily temperatures of a month and 
    returns the maximum temperature with the date as a tuple.
    """
    daily_max = daily_max_temp[0]
    date = 1
    for day_idx in range(len(daily_max_temp)):
        if daily_max_temp[day_idx] > daily_max:
            date = day_idx + 1
            daily_max = daily_max_temp[day_idx]
    return (date, daily_max)


def hottest_day_of_each_year_helper(year: int) -> tuple:
    """Works as the helper to find the hottest day of the year provided

    Args:
        year (int): year you want to find the hottest day

    Returns:
        tuple: year, data of the hottest day and temperature of hottest day
    """
    year_data = main_dic[year]
    every_month_max = []
    for month_number in range(1, 13):
        try:
            monthly_data = year_data[number_to_months[month_number]] 
            every_day_max_temp = []   
            for day in range(len(monthly_data)):
                temp = monthly_data[day][0]
                if temp == "":
                    every_day_max_temp.append(float('-inf'))
                else:
                    every_day_max_temp.append(int(temp))
                    
            # every_month_max.append(max(every_day_max_temp))
            # print(every_day_max_temp)
            date_and_max_temp = custom_max(every_day_max_temp)
            full_date_with_year = (year, month_number, date_and_max_temp[0], date_and_max_temp[1])
            every_month_max.append(full_date_with_year)
            
            # print(f"Every Day Max Temp for {number_to_months[month_number]} is {every_day_max_temp}")
        except KeyError:
            continue
             
    result = sorted(every_month_max, key=lambda x: x[3], reverse=True)
    result = result[0]  # accessing the hishest temperature and date
    return (result[0], f'{result[2]}/{result[1]}/{result[0]}', result[3])


def annual_report_of_temperature_and_humidity():
    """Display the annual report of temperature and humidity of the data"""
    print("Year        MAX Temp        MIN Temp        MAX Humidity        MIN Humidity")
    print("--------------------------------------------------------------------------")
    for year in range(1996, 2012):
        weather_values = annual_report_of_temperature_and_humidity_helper(year)
        
        print(f'{year} {str(weather_values[0]).rjust(12)} {str(weather_values[1]).rjust(15)} {str(weather_values[2]).rjust(15)} {str(weather_values[3]).rjust(20)}')
            
            
def hottest_day_of_each_year():
    """Display hottest day of each year"""
    print("Year        Date          Temp")
    print("------------------------------")
    for year in range(1996, 2012):
        year, date, temp = hottest_day_of_each_year_helper(year)
        print(f'{str(year)} {date.rjust(15)} {str(temp).rjust(8)}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("report", help="report# 1 for Annual Temperature and 2 for Hottest Day of the year")
    parser.add_argument("data_directory", help="data_dir")
    args = parser.parse_args()
    
    file_reading(args.data_directory)
    
    if int(args.report) == 1:
        annual_report_of_temperature_and_humidity()
    elif int(args.report) == 2:
        hottest_day_of_each_year()
    