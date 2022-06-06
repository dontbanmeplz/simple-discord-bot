import json

class js:
    def __init__(self, file):
        self.file = file
        self.js = json.loads(open(file, "r").read())
    def __getitem__(self,key):
        return self.js[key]
    def __setitem__(self, key, val):
        self.js[key] = val
        json.dump(self.js, open(self.file, "w"))