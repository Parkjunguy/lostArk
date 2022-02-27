class Model:
    def __init__(self, **kwargs):
        self.charClass = kwargs['charClass']
        self.charName = kwargs['charName']
        self.charServer = kwargs['charServer']


    def to_dict(self):
        data = dict(x for x in self.__dict__.items())
        return data


def validation(data): # json 검증
    pass

def insert(data):  # DB insert 진행 함수
    pass

def updata(data): #  기존 데이터가 있다면 값 비교후 갱신
    pass
