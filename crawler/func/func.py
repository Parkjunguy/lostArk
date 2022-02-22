# 공용 함수
import os
import time
from seleniumwire import webdriver # ajax  수집 불가능  일반 셀레니움으로 변환

# 환경 분리  => 실서버 환경은 우분투 , 개발 환경은 윈도우  / 서버 pc 준비되면 분리 진행 시작 할것.
if os.environ['ENV'] == 'dev':
    driver_path = 'D:\park_crawler\chromedrvier\chromedriver.exe'
else:
    driver_path = 'D:\park_crawler\chromedrvier\chromedriver.exe'

def loawa_click_sleep():
    time.sleep(3)

# 크롬 driver 옵션 추출 함수
def get_driver_options(is_profile):
    options = webdriver.ChromeOptions()
    # 인자로 구분 필요 프로필 수집인지(스크립트 작동 X), 리스트 수집인지 (스크립트 작동 O)
    if is_profile:
        options.add_argument('headless')
    else:
        pass
    return options

# 크롬 드라이버 실행
def get_driver(is_profile=False):
    options = get_driver_options(is_profile)
    driver = webdriver.Chrome(driver_path, options=options)
    return driver

def get_list(driver):
    import json
    driver.get('https://loawa.com/rank')
    for server in range(2, 10):
        driver.find_element(
            by='xpath',value=f'//*[@id="contents"]/article/form/div/div[1]/div/div[2]/div/label[{server}]'
        ).click()
        loawa_click_sleep()
        for request in driver.requests:
            if 'itemLevel?server=' in request.url:
                print(request.response.body)
