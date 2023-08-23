import argparse
from constants import RECOVERED_RATIO, SAFETY_MEASURE_ARG, MOST_EFFICIENT_SAFETY_MEASURES, GRAPHICAL_DISPLAY
def parse_arguments() -> object:
    """Parse the command line arguments into object

    Returns:
        object with report and weatehrman_data_path as attributes
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "covid_files_path", help="data_dir"
        )
    parser.add_argument(
        RECOVERED_RATIO, '--recovered_ratio', help="To find the recovered ratio of country"
        )
    parser.add_argument(
        SAFETY_MEASURE_ARG, '--safety_measure', help="To find average death rate"
        )
    parser.add_argument(
        MOST_EFFICIENT_SAFETY_MEASURES, '--most_efficient_safetey_measures',
        action="store_true", help="To find top 5 efficient safety measures"
        )
    parser.add_argument(
        GRAPHICAL_DISPLAY, '--graphical_display_of_efficient_safety_measures'
        ,action="store_true", help="See a bar plot of most efficient safety measures"
        )
    args = parser.parse_args()    
    return args
