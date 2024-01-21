class JsonParser:
    def __init__(self, json_string):
        self.json_string = json_string
        self.index = 0
        self.current_char = json_string[self.index]

    def __advance(self):
        pass

    def parse(self):
        pass
