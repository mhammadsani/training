from constants import SAFETY_MEASURE, EFFICIENCY
import matplotlib.pyplot as plt
import utils

def graphical_display_of_efficient_safety_measures(covid) -> None:
    """plot a bar graph for top 5 most efficient safety measures with efficieny value
    """
    
    most_efficient_safety_measures = utils.get_most_efficient_safety_measures(covid)
    safety_measures = [efficient_safety_measure[SAFETY_MEASURE]
                       for efficient_safety_measure in most_efficient_safety_measures]
    efficiencies = [efficient_safety_measure[EFFICIENCY]
                    for efficient_safety_measure in most_efficient_safety_measures]
    plt.figure('Top 5 Safety measures with Efficiencies', figsize=(10, 6))
    plt.xlabel("Efficiency Vaue")
    plt.ylabel('Safety Measure')
    plt.barh(safety_measures, efficiencies)
    plt.tight_layout() 
    plt.show()




def run_tasks(covid, command_line_arguments: object):
    """Run the specific or all the tasks related to covid analysys
       depending upon the attibutes values of the provided command 
       line argument object

    Args:
        command_line_arguments (object): contains the command line values 
        provided by the user as attributes
    """
    
    if (country:=command_line_arguments.recovered_ratio) is not None:
        recovered_ratio = ("Country data not available" 
                           if utils.get_ratio_of_recovered_patients(covid, country) == 0 
                           else utils.get_ratio_of_recovered_patients(covid, country))
        print(f'Recovered/total ratio: {recovered_ratio}')
    if (safety_measure:=command_line_arguments.safety_measure) is not None:
        countries, death_percentage = utils.get_average_death_rate(covid, safety_measure)
        print(f'{death_percentage}% death average found in {countries} countries. ')
    if command_line_arguments.most_efficient_safetey_measures == True:
        most_efficient_safety_measures =  utils.get_most_efficient_safety_measures(covid)
        for safety_measures_with_efficieny in most_efficient_safety_measures:
            print(f'{safety_measures_with_efficieny[SAFETY_MEASURE]}: {safety_measures_with_efficieny[EFFICIENCY]}')
    if command_line_arguments.graphical_display_of_efficient_safety_measures == True:
        graphical_display_of_efficient_safety_measures(covid)
