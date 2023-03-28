
def filterInt(s:str):
    return int(''.join([i for i in s if str.isdigit(i)]))

import re

def convert_to_number(input_string: str) -> float:
    # Work-around to handle missing data.
    if input_string == '':
        return -1.0
    
    # Define the regular expression pattern to match the input string
    pattern = r'^([\d,]+\.?[\d]+)([kKmMbB]?)\s*(.*)$'
  
    # Use the search method to match the input string against the pattern
    match = re.search(pattern, input_string)
  
    # If the match is not successful, return the input string with the commas removed and converted to a number
    if not match:
        return float(input_string.replace(',', ''))
  
    # If the match is successful, extract the number part and the abbreviation from the match
    number_part, abbreviation, _ = match.groups()
  
    # Convert the number part into an actual number by removing the commas and parsing it as a float
    number = float(number_part.replace(',', ''))
  
    # If the abbreviation is "k" or "K", multiply the number by 1000
    if abbreviation in ['k', 'K']:
        return number * 1000.0
  
    # If the abbreviation is "m" or "M", multiply the number by 1000000
    if abbreviation in ['m', 'M']:
        return number * 1000000.0
  
    # If the abbreviation is "b" or "B", multiply the number by 1000000000
    if abbreviation in ['b', 'B']:
        return number * 1000000000.0
  
    # If there is no abbreviation, return the number as is
    return number
  