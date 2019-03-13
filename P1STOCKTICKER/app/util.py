import requests
import hashlib
import json
import os

ENDPOINT = "https://api.iextrading.com/1.0"
CALL = "/stock/{symbol}/chart"
SYMBOLS="https://api.iextrading.com/1.0/ref-data/symbols"

salt = "its a secret to everyone"


def get_chart(symbol):
    response = requests.get(ENDPOINT + CALL.format(symbol=symbol))
    if response.status_code == 200:
        return response.json()
    else:
        raise requests.ConnectionError('http status: ' + format(response.status_code))

def file_json(jsondata,symbol):
    data = json.dumps(jsondata)
    filename=str(symbol)+"_chart.json"
    with open(filename,'w') as myfile:
        myfile.write(data)

    return filename



