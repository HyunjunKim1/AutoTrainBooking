# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# Webdriver 파일의 경로를 입력
driver = webdriver.Chrome("C:\\Git\\AutoTrainBooking\\chromedriver.exe")  
# 이동 페이지 경로
driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')

# 페이지 다 뜰 때 까지 기다림
driver.implicitly_wait(15) 


# ID
driver.find_element(By.ID, 'srchDvNm01').send_keys('2081265815') 
# 비번
driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys("cltkgo1649!")

driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
driver.implicitly_wait(5)

# 조회페이지 경로
driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')
driver.implicitly_wait(5)

# 출발지
dep_stn = driver.find_element(By.ID, 'dptRsStnCdNm')
dep_stn.clear() 
dep_stn.send_keys("동탄")

# 도착지
arr_stn = driver.find_element(By.ID, 'arvRsStnCdNm')
arr_stn.clear()
arr_stn.send_keys("부산")

elm_dptDt = driver.find_element(By.ID, "dptDt")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptDt)

# 여기가 기차 선택창
Select(driver.find_element(By.ID,"dptDt")).select_by_value("20221104")

# 출발 시간
elm_dptTm = driver.find_element(By.ID, "dptTm")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptTm)
Select(driver.find_element(By.ID, "dptTm")).select_by_visible_text("18")

# 시간 조회
driver.find_element(By.XPATH,"//input[@value='조회하기']").click()
driver.implicitly_wait(5)

# 
reserved = False

while True:
    for i in range(1, 3): #3개 기차만 확인. 
        # 18시 42분행
        # 18시 57분행
        # 19시 17분행
        standard_seat = driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7)").text

        if "예약하기" in standard_seat:
            print("예약 가능")          
            driver.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a/span").click()
            reserved = True
            break

    if not reserved:
        # 2초 기다리기
        sleep(2)
        
        # 다시 조회하기
        submit = driver.find_element(By.XPATH, "//input[@value='조회하기']")
        driver.execute_script("arguments[0].click();", submit)
        print("새로고침")

        driver.implicitly_wait(10)
        sleep(1)
    else:
        break

##이거 뭔지 모르겠는데 비쥬얼스튜디오로 코딩하면 Selenium 자꾸 꺼져서 추가함;;
#while(True):
#    pass