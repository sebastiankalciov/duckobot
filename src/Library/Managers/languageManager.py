import json
default_cores = {'core', 'covid'}

class languageManager():
    def __init__(self, lang):
        self.lang = lang

    def getMessage(self,section,prop):
        data = json.load(open(f'./Library/Config/Text/{self.lang}.json', "r"))
        msg = data.get(section).get(prop)
        return msg

    def addMessage(self, section, msg):

        new_end_at_section = ", " + json.dumps(msg) + "\n"
        print(new_end_at_section)
        with open(f'Config/Text/{self.lang}.json', 'w') as j:
            #json_data = json.load(j)
            index = j.tell()
            print(index)
            j.seek(index)
            j.write(new_end_at_section)
            #print(json_data)
            #print(json_data['core2f2f'])



Language = languageManager('en')
