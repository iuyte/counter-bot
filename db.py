import re
import pickle

class DB(object):
    id = ""
    def init(self, id):
            self.id = str(id)

    def load(self):
        with open("db/messages.p", mode="rb") as DB:
            return DB.load()


    def getIndexById(self, messageid):
        data = load()
        for d in range(len(data)):
            if data[d].id is messageid:
                return d
        return None

    def save(self, message, messageid=""):
        o = load()
        if id is "":
            o = o.append(message)
        else:
            o[getIndexById(messageid)].content += message.content
        with open("db/messages.p", mode="wb") as DB:
            pickle.dump(DB, o)

    def search(self, regex, userid=""):
        data = load()
        matches = []
        if userid is "":
            for d in data:
                if bool(re.search(regex, d.content)) and str(d.author.id) is not self.botid:
                    matches.append(str(d.id))
        else:
            for d in data:
                if bool(re.search(regex, d.content)) and str(d.author.id) is userid:
                    matches.append(str(d.id))
        return matches

    def count(self, key, userid=""):
        return len(search(regex, userid))
