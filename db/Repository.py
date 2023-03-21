import json

DIR_KIND = '/home/user/projects/python/db/files/kind.json'
DIR_PARAMETERS = '/home/user/projects/python/db/files/parameters.json'

class Repository:
    def getAllKinds(self):
        with open(DIR_KIND, 'r', encoding='utf-8') as f:
            text = json.load(f)

        kinds = []

        for x in text:
            kinds.append(
                Kind(x['uid'], x['name'], bool(x['is_basic']))
            )

        return kinds

    def createKind(self, kind):
        with open(DIR_KIND, 'r', encoding='utf-8') as f:
            text = json.load(f)

        text.append({
            "uid": kind.uid,
            "name": kind.name,
            "is_basic": kind.is_basic
        })

        with open(DIR_KIND, "w") as file:
            file.write(json.dumps(text))

class Kind:
    def __init__(self, uid: str, name: str, is_basic: bool):
        self.uid = uid
        self.name = name
        self.is_basic = is_basic
