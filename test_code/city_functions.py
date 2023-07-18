""" To write a function that return a neatly formatted single string """
def city_name(city_name, country_name, population=''):
    # return a neatly formatted location
    if population:
        formatted_location = f"{city_name}, {country_name}-{population} 5000000"
    else:
        formatted_location = f"{city_name}, {country_name}"
    return formatted_location.title()
