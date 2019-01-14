import os, sys, json
import requests

url = 'http://0.0.0.0:3333/rsync'
process = 'rsync.exe'
run = 'True'

data = {'process' : process, 'run' : run}

post = requests.post(url, data)