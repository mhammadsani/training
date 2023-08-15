import csv 


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

main_dic = {}
def file_reading():
    for year in range(1996, 2012):
        main_dic[year] = {}
        for month_number in range(1, 13):
            file_name = f'lahore_weather_{year}_{number_to_months[month_number]}.txt'
            try:
               with open(f"weatherdata/{file_name}", 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                file_data = []
                for row in csv_reader:
                    file_data.append(row)
                
                all_days = []
                for row in range(2, len(file_data)- 1):
                    day = file_data[row][1:]
                    all_days.append(day)
                
                main_dic[year][number_to_months[month_number]] = all_days
            
            except FileNotFoundError:
                continue
      

file_reading()  


def every_year_max_temperature(year):
    year_data = main_dic[year]
    every_month_max = []
    for month_number in range(1, 13):
        try:
            monthly_data = year_data[number_to_months[month_number]] 
            every_day_max_temp = []   
            for day in range(len(monthly_data)):
                every_day_max_temp.append(monthly_data[day][0])
            every_month_max.append(max(every_day_max_temp))
        except KeyError:
            continue
    return max(every_month_max)


def annual_report_of_temperature_and_humidity(year):
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
                
                ## max temperature 
                if max_temp == "":
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





print("Year        MAX Temp        MIN Temp        MAX Humidity        MIN Humidity")
print("--------------------------------------------------------------------------")
for year in range(1996, 2012):
    weather_values = annual_report_of_temperature_and_humidity(year)
    # print(weather_values)
    
    print(f'{year} {str(weather_values[0]).rjust(12)} {str(weather_values[1]).rjust(15)} {str(weather_values[2]).rjust(15)} {str(weather_values[3]).rjust(20)}')
            










def every_year_max_temperature(year):
    year_data = main_dic[year]
    every_month_max = []
    for month_number in range(1, 13):
        try:
            monthly_data = year_data[number_to_months[month_number]] 
            every_day_max_temp = []   
            for day in range(len(monthly_data)):
                every_day_max_temp.append(monthly_data[day][0])
            every_month_max.append(max(every_day_max_temp))
        except KeyError:
            continue
    return max(every_month_max)

    # print(max(every_month_max))
    
    
    
def every_year_min_temperature(year):
    year_data = main_dic[year]
    every_month_min = []
    for month_number in range(1, 13):
        try:
            monthly_data = year_data[number_to_months[month_number]] 
            every_day_min_temp = []   
            for day in range(len(monthly_data)):
                min_temp = monthly_data[day][2]
                if min_temp == "":
                    continue
                every_day_min_temp.append(int(min_temp))
                every_month_min.append(min(every_day_min_temp))
        except KeyError:
            continue
    
    return min(every_month_min)

    # print(min(every_month_min))
    


def every_year_min_humidity(year):
    year_data = main_dic[year]
    every_month_min = []
    for month_number in range(1, 13):
        try:
            monthly_data = year_data[number_to_months[month_number]] 
            every_day_min_humidity = []   
            for day in range(len(monthly_data)):
                min_temp = monthly_data[day][8]
                if min_temp == "":
                    continue
                every_day_min_humidity.append(int(min_temp))
                every_month_min.append(min(every_day_min_humidity))
        except KeyError:
            continue
        
    return min(every_month_min)

    # print(min(every_month_min))
   

def every_year_max_humidity(year):
    year_data = main_dic[year]
    every_month_max = []
    for month_number in range(1, 13):
        try:
            monthly_data = year_data[number_to_months[month_number]] 
            every_day_max_humidity = []   
            for day in range(len(monthly_data)):
                every_day_max_humidity.append(monthly_data[day][6])
            every_month_max.append(max(every_day_max_humidity))
        except KeyError:
            continue

    return max(every_month_max)
    # print(max(every_month_max))


# every_year_min_humidity(1996)
# every_year_max_humidity(1996)



# every_year_min_temperature(1996)
# every_year_max_temperature(1996)

# every_year_min_temperature(2000)
# every_year_max_temperature(2000)




# every_year_max_temperature(2000)


# print("Year        MAX Temp        MIN Temp        MAX Humidity        MIN Humidity")
# print("--------------------------------------------------------------------------")
# for year in range(1996, 2012):
#     print(f'{year} {str(every_year_max_temperature(year)).rjust(12)} {str(every_year_max_temperature(year)).rjust(15)} {str(every_year_max_humidity(year)).rjust(15)} {str(every_year_min_humidity(year)).rjust(20)}')
            

def custom_max(daily_max_temp):
    daily_max = daily_max_temp[0]
    date = 1
    for day_idx in range(len(daily_max_temp)):
        if daily_max_temp[day_idx] > daily_max:
            date = day_idx + 1
            daily_max = daily_max_temp[day_idx]
    return (date, daily_max)


daily_max_temp = [35, 32, 32, 34, 35, 36, 37, 37, 37, 33, 32, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 0, 0, 0, 0, 36, 0, 0, 0, 0]

# print(custom_max(daily_max_temp))


def hottest_day_of_each_year(year):
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
            date_and_max_temp = custom_max(every_day_max_temp)
            full_date_with_year = (year, month_number, date_and_max_temp[0], date_and_max_temp[1])
            every_month_max.append(full_date_with_year)
            
            # print(f"Every Day Max Temp for {number_to_months[month_number]} is {every_day_max_temp}")
        except KeyError:
            continue
        
        
        
        
    result = sorted(every_month_max, key=lambda x: x[3], reverse=True)
    result = result[0]
    return (result[0], f'{result[2]}/{result[1]}/{result[0]}', result[3])



# print(hottest_day_of_each_year(2005))

print("Year        Date          Temp")
print("------------------------------")
for year in range(1996, 2011):
    year, date, temp = hottest_day_of_each_year(year)
    print(f'{str(year)} {date.rjust(15)} {str(temp).rjust(8)}')