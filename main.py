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

### LIBRARIES ###

#FLASK used for the framework to connect front-end to back-end
from flask import Flask, render_template

import gps_info

###################################################

### GLOBAL VARIABLES ###

APP = Flask(__name__)

###################################################

### FRONTEND CONNECTION ###
# Functions to create the frontend using FLASK library.

@APP.route('/')
# Load index.html when the webpage is opened.
def index():
	gps = gps_info.gps()
	return render_template('index.html', gps=gps)


###################################################

### RUN THE APPLICATION ##
if __name__ == "__main__":

	APP.run(threaded=True)
