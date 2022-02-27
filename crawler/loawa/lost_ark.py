from pymongo import errors
from database.model import list
from crawler.func import func
from conf.config import ServerList


def loawa_get_list():

    driver = func.get_driver()
    driver.get('https://loawa.com/rank')
    for server in range(2, len(ServerList.server_list)+2):
        driver.find_element(
            by='xpath',value=f'//*[@id="contents"]/article/form/div/div[1]/div/div[2]/div/label[{server}]'
        ).click()
        func.short_sleep()
        result = dict()
        for rank in range(1, 21):
            try:
                data = driver.find_element(by='xpath',value=f'//*[@id="contents"]/article/table/tbody/tr[{rank}]').text.split('\n')
                if ' ' in data[0]:
                    data[0] = data[0].split(' ')[1]
                if ' ' in data[1]:
                    data[1] = data[1].split(' ')
                user_model = list.Model(
                    charClass = data[0],
                    charName = data[1][0],
                    charLevel = float(data[2].split(' ')[0].replace(',','')),
                    charServer = data[1][1]
                )
                result = user_model.to_dict()
                list.insert(user_model.to_dict())
            except errors.DuplicateKeyError:
                list.update(result,True)
            except IndexError:
                print('인덱스 에러 발생 확인 요망')


