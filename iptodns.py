##############################################################################################################
##### THIS IS A BASIC DNS RESOLVER SCRIPT FOR MINECRAFT AND OTHER SERVERS                                #####
##### PLEASE NOTE, THIS SCRIPT USES THE NOW-DNS SERVICE, AND RESOLVE YOUR IP TO THE SELECTED DNS ADDRESS #####
##############################################################################################################

import subprocess
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("CHANGE THIS TO YOUR MAIL", "CHANGE THIS TO YOUR PASSWORD") # To use this line, please register the now-dns.com, and setup your resolver in here
ip = requests.get('https://api.ipify.org').content.decode('utf8') # This line gets your IPv4 (Note: This won't work with IPv6) address from online, and decode it to UTF-8 text content 

data = {
    "hostname":"CHANGE THIS TO YOUR DNS ADDRESS", # In this line, please use the given address you got
    "myip":ip
}

res = requests.get("https://now-dns.com/update", params = data, auth = auth)
print("The new IP for CHANGE THIS TO YOUR DNS ADDRESS:"+ ip +" ---> " + str(res.status_code))

subprocess.call([r"SUBPROCESSNAMEHERE.exe"]) # In this line you can select one of the suprocess you want to run after the resolved address