#상수 처리될 값들 모아둘것.
class ServerList:
    server_list = ['니나브', '루페온', '실리안', '아만', '아브렐슈드', '카단', '카마인', '카제로스']


class DevelopmentConfig:
    DB_HOST = 'localHost'
    PORT =27017


# TODO 실서버 PC 셋팅 완료후 mongoDB 계정 설정 및 아래 설정값 변경 필수
class ProductionConfig:
    DB_HOST = 'localHost'
    PORT =27017
