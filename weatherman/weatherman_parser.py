import argparse
import csv
from constants import ANNUAL_REPORT_TASK,  HOTTEST_DAY_TASK, TASKS
from report_generator import annual_report_of_temperature_and_humidity, hottest_day_of_each_year
from utils import get_month_name


weatherman = {}


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


def read_files(weatherman_files_path: str) -> None:
    """Reads the content in data directory to weatherman

    Args:
        weatherman_files_path (str): path where weatherman data is present
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
   

def run_task(args: object) -> None:
    """Perform the specified task based from tasks

    Args:
        args (object): object having attributes report and weatherman_files_path
    """

    try:
        if args.report == TASKS[ANNUAL_REPORT_TASK]:
            annual_report_of_temperature_and_humidity()
        elif args.report == TASKS[HOTTEST_DAY_TASK]:
            hottest_day_of_each_year()
    except KeyError:
        print("1 for Annual Temperature and 2 for Hottest Day of the year")
