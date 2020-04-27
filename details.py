#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Where is my access point? Console Script.

Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.


Prototype code reated by Juulia Santala & Jonne Tuomela, Cisco Systems, 2020

Prototype, not to be used in production environment!
"""

###################################################

# Constants

###################################################

# information for the netmiko SSH connection to the WLC
username = "username" #ssh username
password = "password" #ssh password
host = "ip" #ip address of the WLC

########

# Mock up data when demoed without WLC, change latitude and longitude to match your usecase

output = """AP Name             GPS Present   Latitude        Longitude       Altitude        GPS location Age
------------------  -----------   ------------    -------------   -------------   ------------------------

1570-RAP1           YES           60.210521     24.819801   25.10  meters   000 days, 00 h 00 m 19 s
1570-MAP1           YES           60.241581     24.829843   10.00  meters   000 days, 00 h 00 m 12 s
1570-RAP2           YES           60.213171     24.919915   25.10  meters   000 days, 00 h 00 m 19 s
1570-MAP2           YES           60.274212     24.719780   10.00  meters   000 days, 00 h 00 m 12 s"""