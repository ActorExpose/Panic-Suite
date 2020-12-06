#!/bin/usr/python3
# -*- coding: utf-8 -*-
import os
import io
import headers
from Functions import osint # def de OSINT
from Functions import setkit # def de Social engineering

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

def main():

	print (bcolors.GREEN+"[+]"+bcolors.ENDC+" Tool Created by"+bcolors.BLUE+" @Chungo_0"+bcolors.ENDC)
	print(bcolors.GREEN+"[+]"+bcolors.ENDC+bcolors.BLUE+" Choose type of attack..."+bcolors.ENDC)
	print (bcolors.RED+"""

	[1] OSINT\n
	[2] Social engineering

	"""+bcolors.ENDC)

	option = input(bcolors.RED+"Panic"+bcolors.ENDC+bcolors.WHITE+":"+bcolors.ENDC+bcolors.BLUE+"~/ "+bcolors.ENDC)
	if(option == "1"):
		osint.Options()

	elif(option == "2"):
		setkit.Options()
	else:
		print (bcolors.RED+"\nthis option is not valid!\n"+bcolors.ENDC)




if __name__ == "__main__":

	headers = headers.Header()
	print (headers)
	main()