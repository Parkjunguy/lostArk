from crawler.func import func
import json

def profile():
    # 프로필 수집 데이터 목록 : 카드 세트옵션, 장비 , 스킬 보석, 스킬
    driver = func.get_driver(True)  # 드라이버는 밖에서 인자로 받아서 진행
    driver.get(f'https://lostark.game.onstove.com/Profile/Character/{"돌아온깜수니"}') # DB 에 저장된 케릭터 꺼내서 공식 페이지 조회
    data = driver.page_source
    data = data.split('<script type="text/javascript">\n')[1].split('</script>')[0].replace('$.Profile = {', '{"Profile":{').replace('};','}}')
    profile = json.loads(data)


    cardSet = profile['Profile']['CardSet']['CardSetEffect_000']
    del cardSet['EffectIndex']
    print(cardSet)  # 카드 셋옵
    print('='*50)

    engrave = profile['Profile']['Engrave']
    key_name_list = list(engrave.keys())   # 키 이름이 매번 변경되어서  키값을 체크 후에접근해야함
    engrave_data = list()
    for index in key_name_list:
        data = dict(
            name = engrave[index]['Element_000']['value'],
            value = int(engrave[index]['Element_001']['value']['leftText'].replace('>', '<').split('<')[6].replace('각인 활성 포인트 +', ''))
        )
        engrave_data.append(data)
    print(engrave_data) # 끼고있는 각인서

    # print(profile['Profile']['GemSkillEffect']) # 보석 리스트 필요함


    # print(profile['Profile']['Skill']) #

profile()
