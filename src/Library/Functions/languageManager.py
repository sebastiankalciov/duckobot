import json
default_cores = {'core', 'covid'}
class languageManager():
    def __init__(self, lang):
        self.lang = lang

    def getMessage(self,section,fraza):
        #self.section = default_cores[0]

        with open(f'Data/Text/{self.lang}.json', 'r') as j: #Deschide fisierul lang.json in modul read doar pentru a fi citit.

            json_data = json.load(j)
            msg = json_data[f'{section}'][f'{fraza}']
        return msg

    def addMessage(self, section, msg):
        #self.section = default_cores[0]

        new_end_at_section = ", " + json.dumps(msg) + "\n"
        print(new_end_at_section)
        with open(f'Data/Text/{self.lang}.json', 'w') as j:
            #json_data = json.load(j)
            index = j.tell()
            print(index)
            j.seek(index)
            j.write(new_end_at_section)
            #print(json_data)
            #print(json_data['core2f2f'])



Language = languageManager('ro')
