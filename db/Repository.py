import json

DIR_KIND = 'kind.json'
DIR_PARAMETERS = 'parameters.json'
DIR_GROUP = 'group.json'
DIR_SAMPLE = 'sample.json'


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
        text = self.getData(DIR_KIND)

        kinds = []

        for x in text:
            kinds.append(
                Kind(x['uid'], x['name'], bool(x['is_basic']))
            )

        return kinds

    def createKind(self, kind: Kind):
        text = self.getData(DIR_KIND)

        text.append({
            "uid": kind.uid,
            "name": kind.name,
            "is_basic": kind.is_basic
        })

        self.setData(DIR_KIND, text)

    def getAllParams(self):
        text = self.getData(DIR_PARAMETERS)

        parameters = []

        for x in text:
            parameters.append(
                Parameter(x['uid'], x['kind_uid'], x['name'], bool(x['is_critical']))
            )

        return parameters

    def createParam(self, param: Parameter):
        text = self.getData(DIR_PARAMETERS)

        text.append({
            "uid": param.uid,
            "kind_uid": param.kindUid,
            "name": param.name,
            "is_critical": param.is_critical
        })

        self.setData(DIR_PARAMETERS, text)

    def getAllGroup(self):
        text = self.getData(DIR_GROUP)

        groups = []

        for x in text:
            groups.append(
                Group(x['uid'], x['kind_uid'], x['name'], bool(x['is_basic']))
            )

        return groups

    def createGroup(self, group: Group):
        text = self.getData(DIR_GROUP)

        text.append({
            "uid": group.uid,
            "kind_uid": group.kindUid,
            "name": group.name,
            "is_basic": group.is_basic
        })

        self.setData(DIR_GROUP, text)

    def getAllSample(self):
        text = self.getData(DIR_SAMPLE)

        samples = []

        for x in text:
            samples.append(
                Sample(x['uid'], x['group_uid'], x['name'], int(x['grade']))
            )

        return samples

    def createSample(self, group: Sample):
        text = self.getData(DIR_SAMPLE)

        text.append({
            "uid": group.uid,
            "group_uid": group.groupUid,
            "name": group.name,
            "grade": group.grade
        })

        self.setData(DIR_SAMPLE, text)

    def delSample(self, uidSample: str):
        text = self.getAllSample()

        for index, sample in enumerate(text):
            if sample.uid == uidSample:
                del text[index]

        saveData = []

        for s in text:
            saveData.append({
                "uid": s.uid,
                "group_uid": s.groupUid,
                "name": s.name,
                "grade": s.grade
            })

        self.setData(DIR_SAMPLE, saveData)

    def getParametersBySampleUid(self, uid: str):

        allSamples = self.getAllSample()

        groupUid = None

        for sample in allSamples:
            if sample.uid == uid:
                groupUid = sample.groupUid
                break

        if groupUid is None:
            return []

        groups = self.getAllGroup()

        kindUid = None

        for group in groups:
            if group.uid == groupUid:
                kindUid = group.kindUid

        if kindUid is None:
            return []

        parameters = self.getAllParams()

        resultParameters = []

        for parameter in parameters:
            if parameter.kindUid == kindUid:
                resultParameters.append(parameter)

        return resultParameters


    def isParameterCritical(self, parameterUid: str):
        parameters = self.getAllParams()

        for param in parameters:
            if param.uid == parameterUid:
                return param.is_critical

        return False

    def updateGradeSample(self, sampleUid: str, grade: int):
        samples = self.getAllSample()

        currentSample = None

        for sample in samples:
            if sample.uid == sampleUid:
                currentSample = sample
                self.delSample(sample.uid)
                break

        if currentSample is None:
            return

        currentSample.grade = grade

        self.createSample(currentSample)


    def getAllSamplesByKindUid(self, kindUid: str):
        groups = self.getAllGroup()

        currentGroups = []

        for group in groups:
            if group.kindUid == kindUid:
                currentGroups.append(group.uid)

        samples = self.getAllSample()

        resSample = []

        for sample in samples:
            if sample.groupUid in currentGroups:
                resSample.append(sample)

        return resSample


    def getData(self, dirName: str):
        try:
            with open(dirName, 'r', encoding='utf-8') as f:
                text = json.load(f)
        except json.decoder.JSONDecodeError:
            text = []

        return text

    def setData(self, dirName: str, text: list):
        with open(dirName, "w") as file:
            file.write(json.dumps(text))
