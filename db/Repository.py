import json

DIR_KIND = '/home/user/projects/python/db/files/kind.json'
DIR_PARAMETERS = '/home/user/projects/python/db/files/parameters.json'
DIR_GROUP = '/home/user/projects/python/db/files/group.json'
DIR_SAMPLE = '/home/user/projects/python/db/files/sample.json'


class Kind:
    def __init__(self, uid: str, name: str, is_basic: bool):
        self.uid = uid
        self.name = name
        self.is_basic = is_basic


class Parameter:
    def __init__(self, uid: str, kindUid: str, name: str, is_critical: bool):
        self.uid = uid
        self.kindUid = kindUid
        self.name = name
        self.is_critical = is_critical


class Group:
    def __init__(self, uid: str, kindUid: str, name: str, is_basic: bool):
        self.uid = uid
        self.kindUid = kindUid
        self.name = name
        self.is_basic = is_basic

class Sample:
    def __init__(self, uid: str, groupUid: str, name: str, grade: int):
        self.uid = uid
        self.groupUid = groupUid
        self.name = name
        self.grade = grade

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

    def createKind(self, kind: Kind):
        with open(DIR_KIND, 'r', encoding='utf-8') as f:
            text = json.load(f)

        text.append({
            "uid": kind.uid,
            "name": kind.name,
            "is_basic": kind.is_basic
        })

        with open(DIR_KIND, "w") as file:
            file.write(json.dumps(text))

    def getAllParams(self):
        with open(DIR_PARAMETERS, 'r', encoding='utf-8') as f:
            text = json.load(f)

        parameters = []

        for x in text:
            parameters.append(
                Parameter(x['uid'], x['kind_uid'], x['name'], bool(x['is_critical']))
            )

        return parameters

    def createParam(self, param: Parameter):
        with open(DIR_PARAMETERS, 'r', encoding='utf-8') as f:
            text = json.load(f)

        text.append({
            "uid": param.uid,
            "kind_uid": param.kindUid,
            "name": param.name,
            "is_critical": param.is_critical
        })

        with open(DIR_PARAMETERS, "w") as file:
            file.write(json.dumps(text))

    def getAllGroup(self):
        with open(DIR_GROUP, 'r', encoding='utf-8') as f:
            text = json.load(f)

        groups = []

        for x in text:
            groups.append(
                Group(x['uid'], x['kind_uid'], x['name'], bool(x['is_basic']))
            )

        return groups

    def createGroup(self, group: Group):
        with open(DIR_GROUP, 'r', encoding='utf-8') as f:
            text = json.load(f)

        text.append({
            "uid": group.uid,
            "kind_uid": group.kindUid,
            "name": group.name,
            "is_basic": group.is_basic
        })

        with open(DIR_GROUP, "w") as file:
            file.write(json.dumps(text))

    def getAllSample(self):
        with open(DIR_SAMPLE, 'r', encoding='utf-8') as f:
            text = json.load(f)

        samples = []

        for x in text:
            samples.append(
                Sample(x['uid'], x['group_uid'], x['name'], int(x['grade']))
            )

        return samples

    def createSample(self, group: Sample):
        with open(DIR_SAMPLE, 'r', encoding='utf-8') as f:
            text = json.load(f)

        text.append({
            "uid": group.uid,
            "group_uid": group.groupUid,
            "name": group.name,
            "grade": group.grade
        })

        with open(DIR_SAMPLE, "w") as file:
            file.write(json.dumps(text))
