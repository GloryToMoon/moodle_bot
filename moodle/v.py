#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traceback


hello='Здравствуйте'
bie='До свидания'


opts = Options()
opts.set_headless()
assert opts.headless

#############
login='login'    #
password='pass' #
#############

group=230
grapth=['08:00','09:40','11:50','13:40','15:20','17:00','18:40']
grapth_e=['09:30', '11:10','13:20','15:10','16:50','18:30','20:10']
#grapth=['08:00','09:10','10:20','11:30','12:24','13:50','15:400']
#grapth_e=['09:00', '10:10','11:20','12:30','13:40','14:50','16:00']

grapth_sat=['08:00','09:40','11:30','13:10','14:50','16:30']
grapth_sat_e=['09:30','11:10','13:00','14:40','16:20','18:00']
day = int(time.strftime("%w"))
file = open(str(group) + '/'+ str(day),'r')
rasp=file.read().split('\n')
file.close()
rasp.pop()
if len(rasp)>len(rasp):
	while len(rasp)!=len(grapth):
		rasp.pop()
	while len(rasp)!=len(grapth_sat):
		rasp.pop()


while True:
	if time.strftime("%w") != day:
		day = int(time.strftime("%w"))
		file = open(str(group) + '/'+ str(day),'r')
		rasp=file.read().split('\n')
		file.close()
		rasp.pop()
		if len(rasp)>len(rasp):
			while len(rasp)!=len(grapth):
				rasp.pop()
			while len(rasp)!=len(grapth_sat):
				rasp.pop()

	if day<6 :
		for i in range(0, len(rasp)):
			if rasp[i] != '-' and grapth[i]==time.strftime("%H:%M"):
				try:
					driver = webdriver.Firefox(options=opts)
					wait = WebDriverWait(driver, 1000)
					driver.get("https://dom.mck-ktits.ru/mod/chat/view.php?id="+rasp[i])
					wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="username"]'))).send_keys(login)
					wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]'))).send_keys(password)
					wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary btn-block mt-3"]'))).click()
					requiredHtml = driver.page_source
					soup = BeautifulSoup(requiredHtml, 'html5lib')
					chat_name = soup.find_all("h1")[0].text
					driver.close()

					driver = webdriver.Firefox(options=opts)
					wait = WebDriverWait(driver, 1000)
					driver.get("https://dom.mck-ktits.ru/mod/chat/view.php?id="+rasp[i])
					wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="username"]'))).send_keys(login)
					wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]'))).send_keys(password)
					wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary btn-block mt-3"]'))).click()

					driver.find_element_by_link_text("Войти в чат").click()
					if rasp[i]!=rasp[i-1] or i==0:
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="input-message"]'))).send_keys(hello.decode('utf-8'))
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="button-send"]'))).click()

					print ('[' + time.strftime("%A %H:%M") + '] Отметился на '.decode('utf-8')+ str(i+1) + ' паре в чате '.decode('utf-8') + chat_name)
					while time.strftime("%H:%M") != grapth_e[i]:
						time.sleep(1)

					if i+1==len(rasp):
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="input-message"]'))).send_keys(bie.decode('utf-8'))
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="button-send"]'))).click()
					elif rasp[i]!=rasp[i+1]:
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="input-message"]'))).send_keys(bie.decode('utf-8'))
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="button-send"]'))).click()
					driver.close()
				except KeyboardInterrupt:
					print ('\nExit...')
					exit(0)
				except:
					print ('\n\n\nCRITICAL ERROR\n PLEASE CONTACT https://vk.com/b3zbab\n' + str(traceback.format_exc()+'\n\n\n'))
					time.sleep(60)

	elif day==6:
		for i in range(0, len(rasp)):
			if grapth_sat[i] != '-' and grapth_sat[i]==time.strftime("%H:%M"):
				try:
					driver = webdriver.Firefox(options=opts)
					wait = WebDriverWait(driver, 1000)
					driver.get("https://dom.mck-ktits.ru/mod/chat/view.php?id="+rasp[i])
					wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="username"]'))).send_keys(login)
					wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]'))).send_keys(password)
					wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary btn-block mt-3"]'))).click()
					requiredHtml = driver.page_source
					soup = BeautifulSoup(requiredHtml, 'html5lib')
					chat_name = soup.find_all("h1")[0].text
					driver.close()

					driver = webdriver.Firefox(options=opts)
					wait = WebDriverWait(driver, 1000)
					driver.get("https://dom.mck-ktits.ru/mod/chat/view.php?id="+rasp[i])
					wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="username"]'))).send_keys(login)
					wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]'))).send_keys(password)
					wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary btn-block mt-3"]'))).click()

					driver.find_element_by_link_text("Войти в чат").click()
					if rasp[i]!=rasp[i-1] or i==0:
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="input-message"]'))).send_keys(hello.decode('utf-8'))
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="button-send"]'))).click()

					print ('[' + time.strftime("%A %H:%M") + '] Отметился на '.decode('utf-8')+ str(i+1) + ' паре в чате '.decode('utf-8') + chat_name)
					while time.strftime("%H:%M") != grapth_sat_e[i]:
						time.sleep(1)

					if i+1==len(rasp):
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="input-message"]'))).send_keys(bie.decode('utf-8'))
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="button-send"]'))).click()
					elif rasp[i]!=rasp[i+1]:
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="input-message"]'))).send_keys(bie.decode('utf-8'))
						wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="button-send"]'))).click()
					driver.close()
				except KeyboardInterrupt:
					print ('\nExit...')
					exit(0)
				except:
					print ('\n\n\nCRITICAL ERROR\n PLEASE CONTACT https://vk.com/b3zbab\n' + str(traceback.format_exc()+'\n\n\n'))
					time.sleep(60)
	try:
		time.sleep(1)
	except KeyboardInterrupt:
		print ('\nExit...')
		exit(0)
