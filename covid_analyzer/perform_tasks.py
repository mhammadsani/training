from constants import SAFETY_MEASURE, EFFICIENCY
import utils


def run_tasks(covid_data, command_line_arguments: object):
    """Run the specific or all the tasks related to covid_data analysys
       depending upon the attibutes values of the provided command 
       line argument object

    Args:
        command_line_arguments (object): contains the command line values 
        provided by the user as attributes
    """
    
    if (country:=command_line_arguments.recovered_ratio) is not None:
        utils.get_ratio_of_recovered_patients(covid_data, country)
    if (safety_measure:=command_line_arguments.safety_measure) is not None:
        utils.get_average_death_rate(covid_data, safety_measure)
    if command_line_arguments.most_efficient_safetey_measures == True:
        most_efficient_safety_measures =  utils.get_most_efficient_safety_measures(covid_data)
        for safety_measures_with_efficieny in most_efficient_safety_measures:
            print(f'{safety_measures_with_efficieny[SAFETY_MEASURE]}: {safety_measures_with_efficieny[EFFICIENCY]}')
    if command_line_arguments.graphical_display_of_efficient_safety_measures == True:
        utils.graphical_display_of_efficient_safety_measures(covid_data)
