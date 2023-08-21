from constants import (
    COUNTRY_NAME_IDX_IN_COVID_STATS, TOTAL_PATIENTS, TOTAL_RECOVERED_PATIENTS, COUNTRY_NAME_IDX_IN_COVID_SAFETY_MEASURES,
    SAFETY_MEASURES, IMPLEMENTED_SAFETY_MEASURES, TOTAL_DEATHS, EMPTY_STRING, TOTAL_CASES, ZERO, EFFICIENCY
    )

def get_ratio_of_recovered_patients(covid, country: str) -> int: 
    """Return the ratio of recovered patients of a country

    Args:
        country (str): country name (case sensitive)
 
    Returns:
        int: 0 if the country's name or data do not exist, otherwise returns the ratio
    """
    COUNTRY_NAME_IDX_IN_COVID_STATS = 0
    for covid_cases_details_per_country in covid['cases_stats']:
        if covid_cases_details_per_country[COUNTRY_NAME_IDX_IN_COVID_STATS] == country:
            try:
                return round(
                    int(covid_cases_details_per_country[TOTAL_RECOVERED_PATIENTS])
                    / int(covid_cases_details_per_country[TOTAL_PATIENTS]), 2
                    )
            except ValueError:
                return ZERO
    else:
        return ZERO
    
    

def get_countries_following_the_safety_measure(covid, safety_measure: str) -> list:
    """Returns the list of countries that follows given safety measure

    Args:
        safety_measure (str): a measure country has implemented

    Returns:
        list: countries list 
    """
    
    country_following_the_safety_measures = []
    for covid_safety_measures_details_per_country in covid[SAFETY_MEASURES]:
        if covid_safety_measures_details_per_country[IMPLEMENTED_SAFETY_MEASURES] == safety_measure and \
            (country:=covid_safety_measures_details_per_country[COUNTRY_NAME_IDX_IN_COVID_SAFETY_MEASURES]) not in country_following_the_safety_measures:
                country_following_the_safety_measures.append(country)
    return country_following_the_safety_measures



def get_average_death_rate(covid, safety_measure: str) -> tuple:
    """Returns the average death ratio against a safety measure
    calculated as total deaths that occurs in the specific countries which have taken economic measures) 
    divided by overall  deaths in the globe. The result is multiplied by 100.

    Args:
        safety_measure (str): the safety measure against which 
        the average death rate needs to be calculated

    Returns:
        tuple: containing the total number of countries that has implemented the safety measure and 
               average death rate
    """
    
    countries_following_the_safety_measure =  get_countries_following_the_safety_measure(covid, safety_measure)
    total_deaths_in_country_following_the_measures = 0
    total_deaths_around_the_globe = 0
    for covid_cases_details_per_country in covid['cases_stats']:
        if covid_cases_details_per_country[COUNTRY_NAME_IDX_IN_COVID_STATS] in countries_following_the_safety_measure:
            if (deaths:=covid_cases_details_per_country[TOTAL_DEATHS]) != EMPTY_STRING:
                total_deaths_in_country_following_the_measures += int(deaths)
                
        if (deaths:=covid_cases_details_per_country[TOTAL_DEATHS]) != EMPTY_STRING:
            total_deaths_around_the_globe += int(deaths)

    return (len(countries_following_the_safety_measure),
           round((total_deaths_in_country_following_the_measures / total_deaths_around_the_globe) * 100, 2))
           
           
           
def get_efficiency(covid, countries_follwoing_the_safety_measures: list) -> int:
    """Returns the efficiency against safety measure calculated as 
        total recovered cases of all countries taken the measure 
        divided by total cases of all countries taken the measure

    Args:
        countries_follwoing_the_safety_measures (list): list of countries that follow safety measure

    Returns:
        int: efficiency value
    """

    total_recovered_cases_of_all_countries = 0
    total_cases_of_all_countries = 0
    for covid_stats_detail_per_country in covid['cases_stats']:
        country_name = covid_stats_detail_per_country[COUNTRY_NAME_IDX_IN_COVID_STATS]
        if (country_name != "") and (country_name in countries_follwoing_the_safety_measures):
            if (covid_stats_detail_per_country[TOTAL_CASES] != EMPTY_STRING and
                covid_stats_detail_per_country[TOTAL_RECOVERED_PATIENTS] != EMPTY_STRING and
                covid_stats_detail_per_country[TOTAL_RECOVERED_PATIENTS] != 0):
                total_cases_of_all_countries += int(covid_stats_detail_per_country[TOTAL_CASES])
                total_recovered_cases_of_all_countries += int(covid_stats_detail_per_country[TOTAL_RECOVERED_PATIENTS])
                
    if total_cases_of_all_countries == ZERO:
        return ZERO
    
    return round(total_recovered_cases_of_all_countries/total_cases_of_all_countries, 2)


def get_most_efficient_safety_measures(covid) -> list:
    """find most efficient safey measures with efficiency value

    Returns:
        list: top 5 most efficient measures with efficiency value
    """
    efficiencies_against_safety_measure = []
    unique_safety_measures = \
        list(
            set([safety_measure_details[IMPLEMENTED_SAFETY_MEASURES]
                for safety_measure_details in covid[SAFETY_MEASURES]]
                )
            )
    for safety_measure in unique_safety_measures:
        countries_following_the_safety_measure = get_countries_following_the_safety_measure(covid, safety_measure)
        efficiency_for_specific_measure = get_efficiency(covid, countries_following_the_safety_measure)
        efficiencies_against_safety_measure.append((safety_measure, efficiency_for_specific_measure))
    efficiencies_against_safety_measure = sorted(efficiencies_against_safety_measure, key=lambda x: x[EFFICIENCY], reverse=True)
    return efficiencies_against_safety_measure[:5]
