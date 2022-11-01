from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\Jun\\source\\repos\\AutoTrainBooking\\chromedriver.exe") # Webdriver 파일의 경로를 입력
driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do') # 이동을 원하는 페이지 주소 

