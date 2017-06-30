import re
import pickle

class DB():
    id = ""
    dbpath = ""
    ignore = ""
    data = []

    def __init__(self, id, dbpath, ignore):
            self.id = str(id)
            self.dbpath = dbpath
            self.ignore = ignore
            self.data = []

    def load(self):
        data = []
        with open(self.dbpath, mode="rb") as DB:
            data = pickle.load(DB)
        self.data = data

    def getIndexById(self, messageid):
        data = self.data
        for d in range(len(data)):
            if data[d].id is messageid:
                return d
        return None

    def save(self, message, messageid=""):
        o = self.data
        if o is None:
            o = [message]
        if messageid is "":
            o.append(message)
        else:
            try:
                o[self.getIndexById(messageid)].content += message.content
            except:
                o.append(message)
        with open(self.dbpath, mode="wb") as DB:
            pickle.dump(o, DB)
        self.data = o

    def search(self, regex, userid=""):
        data = self.data
        matches = []
        if userid is "":
            for d in data:
                if bool(re.search(regex, d.content)) and str(d.author.id) is not self.id and not d.content.startswith(self.ignore):
                    matches.append(str(d.id))
        else:
            for d in data:
                if bool(re.search(regex, d.content)) and str(d.author.id) is userid and not d.content.startswith(self.ignore):
                    matches.append(str(d.id))
        return matches

    def count(self, regex, userid=""):
        return len(self.search(regex, userid))

