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

# Get GPS information from the CLI response

###################################################
# TWO OPTIONS: Either use mock up data (specified in details.py)
# or get real data using Netmiko on WLC (ssh_connection.py).
# Use only one option and comment out the other.

### Option A: Use mock up data
from details import output

### Option B: Use live data
# import ssh_connection
# output = ssh_connection.get_gps()


def gps():
	wlc_output = output.split("\n")[3:]
	gps_information = []
	for device in wlc_output:
		device = list(filter(None,device.split(" ")))
		device = {
			'name':device[0],
			'gps':device[1],
			'latitude':device[2],
			'longitude':device[3]
		}

		gps_information.append(device)

	return gps_information