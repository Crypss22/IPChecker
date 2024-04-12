import requests
from colorama import Fore, Back, Style

import sys
import os
import time
import re

os.system('cls' or 'clear')

def create_env():
    os.environ['ipchecker'] = api_key

def check_for_env():
    if os.environ.get('ipchecker') == True:
        return True          
    else:
        return False
    

print(Fore.GREEN + '''
╔══╗╔═══╗╔═══╗╔╗          ╔╗         
╚╣╠╝║╔═╗║║╔═╗║║║          ║║         
 ║║ ║╚═╝║║║ ╚╝║╚═╗╔══╗╔══╗║║╔╗╔══╗╔═╗
 ║║ ║╔══╝║║ ╔╗║╔╗║║╔╗║║╔═╝║╚╝╝║╔╗║║╔╝
╔╣╠╗║║   ║╚═╝║║║║║║║═╣║╚═╗║╔╗╗║║═╣║║ 
╚══╝╚╝   ╚═══╝╚╝╚╝╚══╝╚══╝╚╝╚╝╚══╝╚╝
    [BY: CHRISTOPHER FEURTADO]
''')
print(Style.RESET_ALL)


print("All information is provided by AbuseIPDB.")


attempt = 0
api_key = check_for_env()

while True:
    if check_for_env() == False:
        api_key = input("Please enter your AbuseIPDB API key: ")
        clean_input = re.sub('[^0-9a-zA-Z]+', '', api_key)
        if len(api_key) == 80 and api_key == clean_input:
            create_env()
            break
        elif attempt == 2:
            print("Too many attempts.. Exiting program.")
            time.sleep(1)
            sys.exit()
        else:
            print("AbuseIPDB API key not recognized, please try again.")
        print('')
        time.sleep(1)
        attempt += 1
        
    else:
        break
    
ip = input('IP: ')

# URL
url = 'https://api.abuseipdb.com/api/v2/check'
params = {
    "ipAddress":ip,"Verbose":True
    
}

headers = {
    "key" : api_key, 'accept':'application/json'  
}

r = requests.get(url, params=params, headers=headers)
    
if r.status_code == 200:
    print('')
    print(f'Querying AbuseIPDB for {ip}')
    time.sleep(1)
    data = r.json()['data']
    print('')
    
#FIELDS
    #print(data) # PRINTS OUT ALL KEY VALUE PAIRS
    print('IP:', data['ipAddress'])
    print('Abuse Confidence Score:', data['abuseConfidenceScore'])
    print('Total Reports:', data['totalReports'])
    print('Last Reported At:', data['lastReportedAt'])
    
    if 'countryName' in data:
        print('Country:', data['countryName'])
    if 'isp' in data:
        print('ISP:', data['isp'])
    if 'hostnames' in data:
        print('Hostname(s):', data['hostnames'])
    if 'domain' in data:
        print('Domain Name:', data['domain'])
    if 'usageType' in data:
        print('Usage Type:', data['usageType'])



# API DOCUMENTATION STATES THIS ENDPOINT IS IN OPEN BETA. MAY CHANGE WITHOUT NOTICE. NOT WORKING AS OF 4/12/2024.
#   reports = r.json()['data']['reports']   
#   if reports in data:
#       print('Top 3 Reports:')
#       print('')
#   # USER REPORTS
#       categories = {'1':'DNS Compromise', 
#                   '2':'DNS Poisoning', 
#                   '3':'Fraud Orders', 
#                   '4':'DDoS Attack', 
#                   '5':'FTP Brute-Force', 
#                   '6':'Ping of Death', 
#                   '7':'Phishing', 
#                   '8':'Fraud', 
#                   '9':'Open Proxy',
#                   '10':'Web Spam', 
#                   '11':'Email Spam', 
#                   '12':'Blog Spam', 
#                   '13':'VPN IP', 
#                   '14':'Port Scan', 
#                   '15':'Hacking',}

#       1ST REPORT
#       category_match = reports[0]['categories']
#       for match in category_match:
#       category_name = categories.get(str(match))
#
#       print('Reporter Country:', reports[0]['reporterCountryName'])
#       print('Reported At:', reports[0]['reportedAt']) 
#       #print('Categories: ', category_name)
#       print('Comment:', reports[0]['comment'])
#       print('-------------------------------------------------------')

#       # 2ND REPORT
#       print('Reporter Country:', reports[1]['reporterCountryName'])
#       print('Reported At:', reports[1]['reportedAt'])
#       print('Comment:', reports[1]['comment'])
#       print('-------------------------------------------------------')
#
#       # 3RD REPORT
#
#       print('Reporter Country:', reports[2]['reporterCountryName'])
#       print('Reported At:', reports[2]['reportedAt'])
#       print('Comment:', reports[2]['comment'])
#       print('-------------------------------------------------------')
#   else:
#       None
#       
else:
    print(f'An error occurred. Status code: {r.status_code}')

print('')
input('Press enter to exit..')