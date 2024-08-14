import argparse
import configparser
# import requests
import json
import os
import sys
import pathlib
 

class DBConnection :
    config_path = pathlib.Path(__file__).parent.parent.parent.absolute() / "settings.ini"
    config  = configparser.ConfigParser()
    config.read(config_path)
    connectionstring =  config['Default']['ConnectionString']
    portnumber = int(config['Default']['PortNumber'])
    database = config['Default']['Database']

class OllamaAPI:
    config_path = pathlib.Path(__file__).parent.parent.parent.absolute() / "settings.ini"
    config  = configparser.ConfigParser()
    config.read(config_path)
    url =  config['Default']['OllamaAPIUrl']
