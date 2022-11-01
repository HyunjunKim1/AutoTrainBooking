# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\Jun\\source\\repos\\AutoTrainBooking\\chromedriver.exe") # Webdriver 파일의 경로를 입력
driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do') # 이동을 원하는 페이지 주소 
driver.implicitly_wait(15) # 페이지 다 뜰 때 까지 기다림

driver.find_element(By.ID, 'srchDvNm01').send_keys('12345677234') # 회원번호
driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys("1111111111") # 비밀번호