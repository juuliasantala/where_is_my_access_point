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

# Get GPS information from WLC with netmiko library

###################################################

from netmiko import ConnectHandler
from details import host, username, password

def get_gps():
	wlc = {
		'device_type': 'cisco_wlc',
		'host': host,
		'username': username,
		'password':password,
		}

	connect = ConnectHandler(**wlc)

	return connect.send_command("show ap gps location summary")
