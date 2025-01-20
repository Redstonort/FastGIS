import undetected_chromedriver as uc
import pickle
import keyboard
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
a=1
try:
	file = open('UserDataGU.txt','r')
	for line in file:
		if a==1:
			login = line
			a+=1
		else:
			password=line
	file.close()
except FileNotFoundError:
	login = getpass("Пожалуйста, введите ваш телефон\еmail\СНИЛС(его не видно в целях безопасности): ")
	password = getpass("Пожалуйста, введите ваш пароль (его не видно в целях безопасности): ")
	file = open('UserDataGU.txt','w')
	file.write(login+"\n"+password)
	file.close()
print("пожалуйста, подождите")
driver = uc.Chrome(use_subprocess = True, version_main=131);

driver.get("https://esia.gosuslugi.ru/login/")

keyboard.press("enter")

sleep(1)
element = driver.find_element(By.CLASS_NAME,'mb-20');
element.click()
keyboard.write(login);

sleep(0.5)
element = driver.find_element(By.CLASS_NAME,'mb-8');
element.click()
keyboard.write(password);

sleep(0.5)
element = driver.find_element(By.CLASS_NAME,'plain-button');
element.click()

