import json
default_cores = {'core', 'covid'}

class languageManager():
    """## Language Manager of duckobot\n MIT License"""
    def __init__(self, lang):
        self.lang = lang

    def getMessage(self,section,prop):
        """### Get the msg from a section of a command.

        Parameters
        ----------
        section:  :class: `string`
                  The section you are looking for.

        prop:  :class: `string`
                The msg you are looking for.


        Returns
        -------
        `Language.getMessage(section, prop)`

            Returns the msg assigned to ``no_arg`` or ``None`` if not found.
        """

        data = json.load(open(f'./Library/Config/Text/{self.lang}.json', "r", encoding="utf-8", errors="replace"))
        msg = data.get(section).get(prop)
        if msg == None:
            return "None"
        return msg


    def addMessage(self, section, msg):

        new_end_at_section = ", " + json.dumps(msg) + "\n"
        print(new_end_at_section)
        with open(f'./Library/Config/Text/{self.lang}.json', 'w') as j:
            #json_data = json.load(j)
            index = j.tell()
            print(index)
            j.seek(index)
            j.write(new_end_at_section)



Language = languageManager('en')
