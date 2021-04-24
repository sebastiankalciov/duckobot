import json

def getData(option1, option2 = None):
    """
    
    ## Get data from config.json file.

    """

    data = json.load(open('../../client/config/config.json', "r"))
    if option2 == None:
        req_option = data.get(option1)

    else:

        req_option = data[option1].get(option2)

    return req_option