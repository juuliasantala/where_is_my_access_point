# Where is my access point?
A prototype to get GPS information from Cisco WLC and visualise the Cisco access point location on Google Maps


## Why?
When access point is located in for example moving vehicle, it can be useful to visualise the curren location on map. Google Maps is only one use case: when implemeting programmability in your network and getting information out of your devices, you can utilise that in any 3rd party solution utilising GPS information.

## Features
- Get GPS information from WLC using Netmiko
- Parse CLI response for GPS information
- Create GUI with Google Maps APIs

## Technologies & Frameworks Used
This is Cisco prototype!

Cisco Hardware
- Cisco 5520 WLC
- Cisco Aironet 1572 access point
- AIR-ANT-GPS-1 GPS antenna for 1572

Tools & Frameworks:
- Python3
- Netmiko
- Flask

## Usage
1. Get your Google Maps API token and insert it in index.html
```html
<script async defer src="ADD YOUR GOOGLE MAPS API SOURCE AND KEY HERE" type="text/javascript">
```
2. If you want to use mock up data, choose option A in gps_info.py and comment out Option B
```python
### Option A: Use mock up data
from details import output
```
3. If you want to use live data, choose option B in gps_info.py and comment out option A. Fill in details.py the username, password and ip of your WLC (Netmiko uses SSH to contact the WLC)
```python
### Option B: Use live data
import ssh_connection
output = ssh_connection.get_gps()
```

```python
# information for the netmiko SSH connection to the WLC
username = "username" #ssh username
password = "password" #ssh password
host = "ip" #ip address of the WLC
```

## Authors
- Juulia Santala
- Jonne Tuomela

## License
This project is licensed to you under the terms of the Cisco Sample Code License.
