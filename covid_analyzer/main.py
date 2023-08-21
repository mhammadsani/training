import csv 
from constants import CASES_STATS, SAFETY_MEASURES
from covid_data_parser import parse_arguments
import perform_tasks



covid = {}


def read_files(covid_analyzer_file_path: str) -> None:
    """read the files in the given path to covid dictionary

    Args:
        covid_analyzer_file_path (str): path wehre files exist
    """
    
    covid[CASES_STATS] = []
    covid[SAFETY_MEASURES] = []
    with open(f'{covid_analyzer_file_path}/covid_cases_stats.csv') as csv_file:
        covid_cases_stats = csv.reader(csv_file, delimiter=',')
        covid[CASES_STATS] = [covid_data_per_country
                                for covid_data_per_country in covid_cases_stats]
        covid[CASES_STATS] = covid[CASES_STATS][1:len(covid[CASES_STATS]) - 8]
        
    with open(f'{covid_analyzer_file_path}/covid_safety_measures.csv') as csv_file:
        covid_safety_measures = csv.reader(csv_file, delimiter=',')
        covid[SAFETY_MEASURES] = [covid_data_per_country
                                    for covid_data_per_country in covid_safety_measures]
        covid[SAFETY_MEASURES] = covid[SAFETY_MEASURES][1:]


def main():
    if __name__ == "__main__":
        command_line_arguments = parse_arguments()
        read_files(command_line_arguments.covid_files_path)
        perform_tasks.run_tasks(covid, command_line_arguments)
        
        
main()
