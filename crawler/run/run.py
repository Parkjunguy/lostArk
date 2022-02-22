import time
from crawler.func import func

# 요기는 시작하는 부분으로만 채워야함
if __name__ == '__main__':
    import json

    driver = func.get_driver(True)
    driver.get(f'https://lostark.game.onstove.com/Profile/Character/{"불고기3"}') # DB 에 저장된 케릭터 꺼내서 공식 페이지 조회
    data = driver.page_source
    data = data.split('<script type="text/javascript">\n')[1].split('</script>')[0].replace('$.Profile = {', '{"Profile":{').replace('};','}}')
    profile = json.loads(data)
    print(profile['Card'])
