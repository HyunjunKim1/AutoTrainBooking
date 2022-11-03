# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Webdriver 파일의 경로를 입력
driver = webdriver.Chrome("C:\\Git\\AutoTrainBooking\\chromedriver.exe")  
# 이동을 원하는 페이지 주소 
driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')

# 페이지 다 뜰 때 까지 기다림
driver.implicitly_wait(15) 


# 회원번호
driver.find_element(By.ID, 'srchDvNm01').send_keys('2081265815') 
 # 비밀번호
driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys("cltkgo1649!")

driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
driver.implicitly_wait(5)

# 기차 조회 페이지로 이동
driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')
driver.implicitly_wait(5)

# 출발지 입력
dep_stn = driver.find_element(By.ID, 'dptRsStnCdNm')
dep_stn.clear() 
dep_stn.send_keys("동탄")

# 도착지 입력
arr_stn = driver.find_element(By.ID, 'arvRsStnCdNm')
arr_stn.clear()
arr_stn.send_keys("부산")

# 날짜 드롭다운 리스트 보이게
elm_dptDt = driver.find_element(By.ID, "dptDt")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptDt)

while(True):
    pass