# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

import re

def domain_name(url):
    if '/' in url:        
        start_url = url.index('/')
        end_url = url.index('.')
        domain = url[start_url+2:end_url]        
    else:        
        domain = url.split('.')[1]
        
    return domain
