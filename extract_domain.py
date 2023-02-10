# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

import re

def domain_name(url):

    pattern = "(\w+\.)"
    result = re.findall(pattern, url)

    if 'www' in result[0]:
        domain = result[1][:-1]   
    else:        
        domain = result[0][:-1]
        
    return domain
