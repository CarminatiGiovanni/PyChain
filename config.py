from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

PORT = int(config['SERVER']['PORT'])
HOST = config['SERVER']['HOST']
nodes = list(config['nodes'].values())