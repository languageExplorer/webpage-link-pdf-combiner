import re

def filter_strings(substring, string_list):

    # Filter the list based on the substring and sort by the number before .html
    filtered_list = [s for s in string_list if substring in s]
    return sorted(filtered_list, key=lambda url: int(re.search(r'(\d+)\.html$', url).group(1)))
