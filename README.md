# IPChecker v2
<img src="https://forthebadge.com/images/badges/made-with-python.png" height="15%" width="15%">

## About
IPChecker, a python program that queries AbuseIPDB utilizing their API and quickly returns pertinent, valuable information on an IP back to the user. The program is simple and all that is required from the user is an AbuseIPDB API key, and the IP in which they wish to query.

### Requirements
* Dependencies: ```colorama``` ```requests``` ```keyring```
> Ensure requirements are met before use of program.

### Updates:
#### Version 1.0
* The user's API key is temporarily stored as an environment variable and only persists as long as the session.

#### Version 2.0 (4/16/2024)
* Introduces the keyring library, implementing a more seamless and secure user experience.


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

<img src="https://imgur.com/0PXWWCG.png" height=1000 width=1000 alt="IPChecker">

**Certain aspects of the API such as returning reports made by users on the alleged use-case of the IP are in beta mode and are subject to not function properly. Due to this, the code does exist within the program, but is commented out.**
