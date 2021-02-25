import json

def getData(option):

    data = json.load(open('./Library/Config/config.json', "r"))
    req_option = data.get(option)
    
    return req_option