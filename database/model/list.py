import datetime
from conf.connect import Connect
from pymongo import errors

conn = Connect()
db = conn.connections()

class Model:
    LIST = db.list

    def __init__(self, **kwargs):
        self.charClass = kwargs['charClass']
        self.charName = kwargs['charName']
        self.charLevel = kwargs['charLevel']
        self.charServer = kwargs['charServer']

    def to_dict(self):
        data = dict(x for x in self.__dict__.items())
        return data

    def validation(self):
        # TODO jsonschema  모듈 사용하여 검증 필요함
        pass


def insert(data):
    try:
        data['insert_time'] = datetime.datetime.utcnow()
        data['need_update'] = True
        Model.LIST.insert_one(data)
        print(f'{data["charName"]}수집 중...')
    except errors.DuplicateKeyError as e:
        raise errors.DuplicateKeyError(e)


def update(data, upsert): #  기존 데이터가 있다면 값 비교후 갱신
    original_data = Model.LIST.find_one({'charName': data['charName']})
    if data['charLevel'] != original_data['charLevel']:
        data['update_time'] = datetime.datetime.utcnow()
        data['need_update'] = True
        Model.LIST.update_one({'charName':data['charName']}, {'$set': data}, upsert)
    else:
        print('변경사항이 없으므로 pass')


