import argparse

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
