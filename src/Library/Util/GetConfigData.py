import json

def getData(option1, option2 = None):

    data = json.load(open('./Library/Config/config.json', "r"))
    if option2 == None:

        req_option = data.get(option1)
    
    else:
        req_option = data[option1].get(option2)

    return req_option