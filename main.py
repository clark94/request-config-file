import requests as req
from configparser import ConfigParser

cnf = ConfigParser()
cnf.read('config.ini')

#print(cnf['url']['host'].format('01306001'))

req = req.get(cnf['url']['host'].format('01306001'))

data = req.json()

print('Endereco:' + data['logradouro'])

#getYourAdress('01306001')