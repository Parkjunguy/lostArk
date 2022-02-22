def loawa_list():
    from database.model import list
    from crawler.func import func
    from conf.config import ServerList
    import time

    # 요기서 멀티프로세싱 진행 이후에  함수 호출 여러번 해야됨  비동기 처리 필요 ?
    # 코루틴 사용 확인 할것.
    driver = func.get_driver() # 페이지 접근 및 작동 확인 완료
    driver.get('https://loawa.com/rank')
    for server in range(2, ServerList.server_list+2):
        driver.find_element(
            by='xpath',value=f'//*[@id="contents"]/article/form/div/div[1]/div/div[2]/div/label[{server}]'
        ).click()
        time.sleep(3)
        for rank in range(1, 21):
            data = driver.find_element(by='xpath',value=f'//*[@id="contents"]/article/table/tbody/tr[{rank}]').text.split('\n')
            if ' ' in data[0]:
                data[0] = data[0].split(' ')[1]
            if ' ' in data[1]:
                data[1] = data[1].split(' ')
            user_model = list.Model(
                charClass = data[0],
                charName = data[1][0],
                charServer = data[1][1]
            )
            print(user_model.to_dict())
