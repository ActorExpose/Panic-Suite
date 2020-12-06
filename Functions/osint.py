#!/bin/usr/python3
# -*- coding: utf-8 -*-
import os
import subprocess
import requests
import json
import docx

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
	print (bcolors.GREEN+"[1]"+bcolors.ENDC+bcolors.RED+" Password Breach"+bcolors.ENDC)
	print (bcolors.GREEN+"[2]"+bcolors.ENDC+bcolors.RED+" User Recon"+bcolors.ENDC)
	print (bcolors.GREEN+"[3]"+bcolors.ENDC+bcolors.RED+" IP Info"+bcolors.ENDC)
	print (bcolors.GREEN+"[4]"+bcolors.ENDC+bcolors.RED+" Documents metadata"+bcolors.ENDC)


	print ("\n")

	option = input(bcolors.GREEN+"[OSINT]"+bcolors.ENDC+bcolors.RED+"Panic"+bcolors.ENDC+bcolors.WHITE+":"+bcolors.ENDC+bcolors.BLUE+"~/ "+bcolors.ENDC)
	if(option == "1"):
		PasswordBreach()
	elif(option == "2"):
		UserRecon()
	elif(option == "3"):
		GetIpInfo()
	elif(option == "4"):
		DocumentMetaData()
	else:
		print (bcolors.RED+"\nthis option is not valid!\n"+bcolors.ENDC)

def UserRecon():
	print ("\n")
	username = input(bcolors.GREEN+"[?] Victim username: "+bcolors.ENDC)
	print (bcolors.GREEN+"[*] Check username "+bcolors.BOLD+username+bcolors.ENDC+bcolors.GREEN+" on:"+bcolors.ENDC)

	#Check instagram user
	instagram = subprocess.getoutput('curl -o /dev/null -s -w "%{http_code}\n" https://www.instagram.com/'+username+"/")
	if(instagram == "200"):
		print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] Instagram:"+bcolors.GREEN+" Found!"+bcolors.ENDC+ " --> https://www.instagram.com/"+username+"/")
	else:
		print ("["+bcolors.RED+"-"+bcolors.ENDC+"] Instagram:"+bcolors.RED+" Not found!"+bcolors.ENDC)

	#Check Twitter user
	#debo verificar esta peticion ya que siempre da 200
	twitter = subprocess.getoutput('curl -o /dev/null -s -w "%{http_code}\n" https://twitter.com/'+username+"/")
	if(twitter == "200"):
		print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] Twitter:"+bcolors.GREEN+" Found!"+bcolors.ENDC+ " --> https://twitter.com/"+username+"/")
	else:
		print ("["+bcolors.RED+"-"+bcolors.ENDC+"] Twitter:"+bcolors.RED+" Not found!"+bcolors.ENDC)

	#Check Youtube user
	youtube = subprocess.getoutput('curl -o /dev/null -s -w "%{http_code}\n" https://www.youtube.com/'+username+"/")
	if(youtube == "200"):
		print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] Youtube:"+bcolors.GREEN+" Found!"+bcolors.ENDC+ " --> https://www.youtube.com/"+username+"/")
	else:
		print ("["+bcolors.RED+"-"+bcolors.ENDC+"] Youtube:"+bcolors.RED+" Not found!"+bcolors.ENDC)		

	#Check Reddit user
	reddit = subprocess.getoutput('curl -o /dev/null -s -w "%{http_code}\n" -L --user-agent "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801" https://www.reddit.com/user/'+username+"/ | head -n1")
	if(reddit == "200"):
		print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] Reddit:"+bcolors.GREEN+" Found!"+bcolors.ENDC+ " --> https://www.reddit.com/user/"+username+"/")
	else:
		print ("["+bcolors.RED+"-"+bcolors.ENDC+"] Reddit:"+bcolors.RED+" Not found!"+bcolors.ENDC)

	#Check GitHub user
	github = subprocess.getoutput('curl -o /dev/null -s -w "%{http_code}\n" -L --user-agent "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801" https://github.com/'+username+"/ | head -n1")
	if(github == "200"):
		print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] GitHub:"+bcolors.GREEN+" Found!"+bcolors.ENDC+ " --> https://github.com/"+username+"/")
	else:
		print ("["+bcolors.RED+"-"+bcolors.ENDC+"] GitHub:"+bcolors.RED+" Not found!"+bcolors.ENDC)

	#Check Pinterest user
	pinterest = subprocess.getoutput('curl -o /dev/null -s -w "%{http_code}\n" -L --user-agent "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801" https://www.pinterest.com/'+username+"/ | head -n1")
	if(pinterest == "200"):
		print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] Pinterest:"+bcolors.GREEN+" Found!"+bcolors.ENDC+ " --> https://www.pinterest.com/"+username+"/")
	else:
		print ("["+bcolors.RED+"-"+bcolors.ENDC+"] Pinterest:"+bcolors.RED+" Not found!"+bcolors.ENDC)

	#Check Ebay user
	ebay = subprocess.getoutput('curl -s -i "https://www.ebay.com/usr/'+username+'" -H "Accept-Language: en" -L | grep -o "HTTP/2 404\|404 Not Found\|eBay Profile - error" ; echo $?')
	if(ebay == "1"):
		print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] Ebay:"+bcolors.GREEN+" Found!"+bcolors.ENDC+ " --> https://www.ebay.com/usr/"+username+"/")
	else:
		print ("["+bcolors.RED+"-"+bcolors.ENDC+"] Ebay:"+bcolors.RED+" Not found!"+bcolors.ENDC)		

	print ("\n")

def PasswordBreach():

	print ("\n")
	# Tor proxy
	proxy = '127.0.0.1:9050'
	session = requests.session()
	session.proxies = {'http': 'socks5h://{}'.format(proxy), 'https': 'socks5h://{}'.format(proxy)}

	email = input(bcolors.GREEN+"[?] Victim email: "+bcolors.ENDC)
	domain = "%"
	url = "http://pwndb2am4tzkvold.onion/"

	if("@" in email):
		username = email.split("@")[0]
		domain = email.split("@")[1]
		if(not username):
			username = '%'
	request_data = {'luser': username, 'domain': domain, 'luseropr': 1, 'domainopr': 1, 'submitform': 'em'}
	r = session.post(url, data=request_data)
	if("Array" not in r.text):
		return None
	leaks = r.text.split("Array")[1:]
	emails =[]
	for leak in leaks:
		leaked_email = ''
		domain = ''
		password = ''

		try:
			leaked_email = leak.split("[luser] =>")[1].split("[")[0].strip()
			domain = leak.split("[domain] =>")[1].split("[")[0].strip()
			password = leak.split("[password] =>")[1].split(")")[0].strip()
		except:
			pass
		if (leaked_email):
			emails.append({'username': leaked_email, 'domain': domain, 'password': password})

	emails.pop(0)
	if(emails != []):
		print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+ bcolors.GREEN+"Leaks Found:"+bcolors.ENDC)
		for email in emails:
			username = email.get('username', '')
			domain = email.get('domain', '')
			password = email.get('password', '')
			print("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+username + "@" + domain + bcolors.ENDC +":"+ bcolors.GREEN + password + bcolors.ENDC)
	else:	
		print ("["+bcolors.RED+"-"+bcolors.ENDC+"]"+bcolors.RED+" Leaks not Found"+bcolors.ENDC)

def GetIpInfo():
	print ("\n["+bcolors.GREEN+"!"+bcolors.ENDC+"] "+bcolors.GREEN+bcolors.BOLD+"Retrieve IP Geolocation information."+bcolors.ENDC)
	session = requests.session()
	ip = input(bcolors.GREEN+"[?] IP: "+bcolors.ENDC)
	url = "https://ipinfo.io/"+ip
	r = session.get(url)

	class Info(object):
		def __init__(self, json_def):
			self.__dict__ = json.loads(json_def)

			
	result = Info(r.text)

	coordinates = result.loc.split(",", 1)

	print ("\n["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"Target Ip: "+bcolors.ENDC+result.ip)
	print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"City: "+bcolors.ENDC+result.city)
	print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"Region: "+bcolors.ENDC+result.region)
	print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"Zip Code: "+bcolors.ENDC+result.postal)
	print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"Country: "+bcolors.ENDC+result.country)
	print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"Provider: "+bcolors.ENDC+result.org)
	print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"Approximate Latitude: "+bcolors.ENDC+coordinates[0])
	print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"Approximate Longtitude: "+bcolors.ENDC+coordinates[1])
	print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"Time Zone: "+bcolors.ENDC+result.timezone)
	print ("["+bcolors.GREEN+"+"+bcolors.ENDC+"] "+bcolors.GREEN+"Map View: "+bcolors.ENDC+"http://www.google.com/maps/place/"+coordinates[0]+","+coordinates[1]+"/@"+coordinates[0]+","+coordinates[1]+",16z")
	print ("\n")


def DocumentMetaData():


	file_name = "mydoc.docx"

	document = docx.Document(docx = file_name)
	core_properties = document.core_properties
	print(core_properties.author)
	print(core_properties.created)
	print(core_properties.last_modified_by)
	print(core_properties.last_printed)
	print(core_properties.modified)
	print(core_properties.revision)
	print(core_properties.title)
	print(core_properties.category)
	print(core_properties.comments)
	print(core_properties.identifier)
	print(core_properties.keywords)
	print(core_properties.language)
	print(core_properties.subject)
	print(core_properties.version)
	print(core_properties.keywords)
	print(core_properties.content_status)


