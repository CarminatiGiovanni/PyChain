from configparser import ConfigParser
import os
config = ConfigParser()

config.read(os.path.join(os.path.dirname(__file__),'..','config.ini'))

PORT = int(config['SERVER']['PORT'])
HOST = config['SERVER']['HOST']
nodes = list(config['nodes'].values())

static_folder = "static"
template_folder = "template"
