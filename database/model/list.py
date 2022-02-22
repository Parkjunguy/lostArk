class Model:
    def __init__(self, **kwargs):
        self.charClass = kwargs['charClass']
        self.charName = kwargs['charName']
        self.charServer = kwargs['charServer']


    def to_dict(self):
        data = dict(x for x in self.__dict__.items())
        return data

def insert(data):
    pass

def updata(data):
    pass
