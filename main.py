import yaml
import requests as req

with open('test.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    

#print(data['host'].format('01306001'))

req = req.get(data['host'].format('01306001'))
info = req.json()

print(info['logradouro'])

