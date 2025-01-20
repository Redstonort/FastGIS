import undetected_chromedriver as uc
import pickle
import keyboard
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
a=1
try:
	file = open('UserData.txt','r')
	for line in file:
		if a==1:
			login = line
			a+=1
		else:
			password=line
	file.close()
except FileNotFoundError:

	login = input("Пожалуйста, введите ваш логин: ")
	password = getpass("Пожалуйста, введите ваш пароль (его не видно в целях безопасности): ")
	file = open('UserData.txt','w')
	file.write(login+"\n"+password)
	file.close()
print("пожалуйста, подождите")
driver = uc.Chrome(use_subprocess = True, version_main=131);

driver.get("https://giseo.rkomi.ru/authorize/login-pass")

keyboard.press("enter")

sleep(1)
element = driver.find_element(By.CLASS_NAME,'select2__button');
element.click()

sleep(0.5)

keyboard.write("гимназия Пушкина");

sleep(0.5)
element = driver.find_element(By.CLASS_NAME,'select2-results__option--highlighted');
element.click()

sleep(0.5)
element = driver.find_element(By.CLASS_NAME,'lc-input-login');
element.click()
keyboard.write(login);

sleep(0.5)
element = driver.find_element(By.CLASS_NAME,'logpass__pass');
element.click()
keyboard.write(password);

sleep(0.5)
element = driver.find_element(By.CLASS_NAME,'primary-button');
element.click()

