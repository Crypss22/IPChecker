# IPChecker
## About
IPChecker is a python project of mine that queries AbuseIPDB utilizing their API and quickly returns pertinent, valuable information on an IP back to the user. The program is simple and all that is required from the user is a AbuseIPDB API key, and the IP in which they wish to query.

**Information that is returned to the user consists of:**       
* IP
* Abuse Confidence Score
* Total Reports (Past 30 Days)
* Last Reported At
* Country Name
* ISP
* Hostnames
* Domain
* Usage Type

**If information above is not returned to the user, it could not be found in the IP that was queried.**

</br>

> [!NOTE]
> Feedback is encouraged and appreciated.
</br>

<img src="https://imgur.com/pzk7xeZ.png" height="80%" width="80%" alt="IPChecker">


```
import requests

import sys
import os
import time
import re

os.system('cls' or 'clear')
# API to access AbuseIPDB

def create_env():
        home_dir = os.path.expanduser('~')
        env_file_path = os.path.join(home_dir, 'api.env')
    # Write API key to .env     
        with open(env_file_path, 'w') as env_file:
            env_file.write(f'API_KEY={api_key}\n')
            
def check_for_env():
    home_dir = os.path.expanduser('~')
    env_file_path = os.path.join(home_dir, 'api.env')
    
    if os.path.exists(env_file_path):
        #return True
        with open(env_file_path, 'r') as env_file:
            for line in env_file:
                if line.startswith("API_KEY="):
                    api_key = line.strip().split('=')[1]
                    return api_key
    else:
        return False
    
def delete_env():
    home_dir = os.path.expanduser('~')
    env_file_path = os.path.join(home_dir, 'api.env')
    if os.path.exists(env_file_path):
        os.remove(env_file_path)

print('''
╔══╗╔═══╗╔═══╗╔╗          ╔╗         
╚╣╠╝║╔═╗║║╔═╗║║║          ║║         
 ║║ ║╚═╝║║║ ╚╝║╚═╗╔══╗╔══╗║║╔╗╔══╗╔═╗
 ║║ ║╔══╝║║ ╔╗║╔╗║║╔╗║║╔═╝║╚╝╝║╔╗║║╔╝
╔╣╠╗║║   ║╚═╝║║║║║║║═╣║╚═╗║╔╗╗║║═╣║║ 
╚══╝╚╝   ╚═══╝╚╝╚╝╚══╝╚══╝╚╝╚╝╚══╝╚╝
''')
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
            delete_env()
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
       
else:
    print(f'An error occurred. Status code: {r.status_code}')

print('')
input('Press enter to exit..')
```
