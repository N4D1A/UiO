import re
from typing import Tuple
from requesting_urls import get_html 

## -- Task 3 (IN3110 optional, IN4110 required) -- ##

# create array with all names of months
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

month_names_regex = [
    "[jJ]an(?:uary)?",
    "[fF]eb(?:ruary)?",
    "[mM]ar(?:ch)?",
    "[aA]pr(?:il)?",
    "[mM]ay",
    "[jJ]un(?:e)?",
    "[jJ]ul(?:y)?",
    "[aA]ug(?:ust)?",
    "[sS]ep(?:tember)?",
    "[oO]ct(?:ober)?",
    "[nN]ov(?:ember)?",
    "[dD]ec(?:ember)?",
]

month_names_dict = {
    "jan":"01",
    "feb":"02",
    "mar":"03",
    "apr":"04",
    "may":"05",
    "jun":"06",
    "jul":"07",
    "aug":"08",
    "sep":"09",
    "oct":"10",
    "nov":"11",
    "dec":"12",
}


def get_date_patterns() -> Tuple[str, str, str]:
    """Return strings containing regex pattern for year, month, day
    arguments:
        None
    return:
        year, month, day (tuple): Containing regular expression patterns for each field
    """

    # Regex to capture days, months and years with numbers
    # year should accept a 4-digit number between at least 1000-2029
    year = r"\b(1[0-9][0-9][0-9]|20[0-2][0-9])\b"
    # month should accept month names or month numbers
    all_months_str = '|'.join(month_names_regex) ## considered standardized and unstandardized formats
    month = rf"\b({all_months_str}|[1-9]|0[1-9]|1[0-2])\b" ## considered number formats as well
    # day should be a number, which may or may not be zero-padded
    day = r"\b([1-9]|0[1-9]|[1-2][0-9]|3[0-1])\b"

    return year, month, day


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

    You don't need to use this function,
    but you may find it useful.

    arguments:
        month_name (str) : month name
    returns:
        month_number (str) : month number as zero-padded string
    """
    # If already digit return digit as it is
    if s.isdigit():
        return zero_pad(s) # If digit is one-digit, add 0 before the digit

    # Convert into a number as string
    return month_names_dict[s[:3].lower()]


def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'

    You don't need to use this function,
    but you may find it useful.
    """
    if len(n)==1:
            n = '0'+n
    return n


def find_dates(text: str, output: str = None) -> list:
    """Finds all dates in a text using reg ex

    arguments:
        text (string): A string containing html text from a website
    return:
        results (list): A list with all the dates found
    """
    year, month, day = get_date_patterns()

    # Date on format YYYY/MM/DD - ISO
    ISO = rf"{year}-{month}-{day}"

    # Date on format DD/MM/YYYY
    DMY = rf"{day}\s{month}\s{year}"

    # Date on format MM/DD/YYYY
    MDY = rf"{month}\s{day},\s{year}"

    # Date on format YYYY/MM/DD
    YMD = rf"{year}\s{month}\s{day}"


    # list with all supported formats
    formats = [ISO, DMY, MDY, YMD]

    dates = []

    # find all dates in any format in text
    dates_found = re.findall(rf"{ISO}|{DMY}|{MDY}|{YMD}", text)
    
    for date in dates_found:
        if date[0]: ## for ISO pattern
            dates.append(date[0]+'/'+convert_month(date[1])+'/'+zero_pad(date[2]))
        elif date[3]: ## for DMY pattern
            dates.append(date[5]+'/'+convert_month(date[4])+'/'+zero_pad(date[3]))
        elif date[6]: ## for MDY pattern
            dates.append(date[8]+'/'+convert_month(date[6])+'/'+zero_pad(date[7]))
        elif date[9]: ## for YMD pattern
            dates.append(date[9]+'/'+convert_month(date[10])+'/'+zero_pad(date[11]))

    # Write to file if wanted
    if output:
        # open a txt.file 
        f = open(output,"w+")
        # write data into the file
        for date in dates:
            f.write(date + '\n')
        # close the file instance       
        f.close()

    return dates

