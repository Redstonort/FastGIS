import undetected_chromedriver as uc
import pickle
import keyboard
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
import os
import re
from sys import platform

def extract_version_registry(output):
    try:
        google_version = ''
        for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
            if letter != '\n':
                google_version += letter
            else:
                break
        return(google_version.strip())
    except TypeError:
        return

def extract_version_folder():
    for i in range(2):
        path = 'C:\\Program Files' + (' (x86)' if i else '') +'\\Google\\Chrome\\Application'
        if os.path.isdir(path):
            paths = [f.path for f in os.scandir(path) if f.is_dir()]
            for path in paths:
                filename = os.path.basename(path)
                pattern = '\d+\.\d+\.\d+\.\d+'
                match = re.search(pattern, filename)
                if match and match.group():
                    return match.group(0)

    return None

def get_chrome_version():
    version = None
    install_path = None

    try:
        if platform == "linux" or platform == "linux2":
            install_path = "/usr/bin/google-chrome"
        elif platform == "darwin":
            install_path = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
        elif platform == "win32":
            try:
                stream = os.popen('reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome"')
                output = stream.read()
                version = extract_version_registry(output)
            except Exception as ex:
                version = extract_version_folder()
    except Exception as ex:
        print(ex)

    version = os.popen(f"{install_path} --version").read().strip('Google Chrome ').strip() if install_path else version

    return version
version = get_chrome_version()


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
driver = uc.Chrome(use_subprocess=True, version_main = int(version[0]+version[1]+version[2]));

driver.get("https://giseo.rkomi.ru/authorize/login-pass")

keyboard.press("enter")

sleep(1)
element = driver.find_element(By.CLASS_NAME,'select2__button');
element.click()

sleep(0.5)

keyboard.write("гимназия Пушкина");
sleep(0.5)
keyboard.press("enter")

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

