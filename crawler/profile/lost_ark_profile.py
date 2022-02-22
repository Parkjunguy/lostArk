import time


def profile():
    from crawler.func import func
    import json
    driver = func.get_driver()
    driver.get(f'https://lostark.game.onstove.com/Profile/Character/{"불고기3"}')
    data = driver.page_source
    data = data.split('$.Profile = {')[1].split('</script>')[0]
    result = json.loads(data)
    print(result)

    # 장비 현황 수집 가능 , 수집 내실  현황 체크 필요

    #lui-tab 수집 내실 class name <-  포메팅 필요함
