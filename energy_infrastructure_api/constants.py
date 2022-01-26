#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

VERSION = 'v0.1.0'
URL_PREFIX = '/api/' + VERSION + '/infrastructure'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

config_file = configparser.ConfigParser()
config_file.read(os.path.join(
    BASE_DIR, 'static', 'config.ini'
))

MONGO = dict(
    local=True,
    user=config_file.get('user', 'username'),
    password=config_file.get('user', 'password'),
    domain=config_file.get('server', 'domain'),
    database=config_file.get('server', 'database'),
    port=int(config_file.get('server', 'port')),
)

# Update Mongo URI as needed here

# URI = "mongodb+srv://{}:{}@{}/{}?retryWrites=true&w=majority".format(
#     MONGO['user'], MONGO['password'], MONGO['domain'],
#     MONGO['database'])

# URI = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
URI = "mongodb://localhost:27017/energy_maps_local_db"