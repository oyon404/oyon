#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """ 
░─── 
░

░█████╗░██╗░░░██╗░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝██╔══██╗████╗░██║
██║░░██║░╚████╔╝░██║░░██║██╔██╗██║
██║░░██║░░╚██╔╝░░██║░░██║██║╚████║
╚█████╔╝░░░██║░░░╚█████╔╝██║░╚███║
░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝


                                
                                
░░██╗██╗░█████╗░░░██╗██╗
░██╔╝██║██╔══██╗░██╔╝██║
██╔╝░██║██║░░██║██╔╝░██║
███████║██║░░██║███████║
╚════██║╚█████╔╝╚════██║
░░░░░╚═╝░╚════╝░░░░░░╚═╝
                                                 
               WhatsApp : Unkonown
                        OYON
                     ▇◤▔▔▔▔▔▔▔◥▇
                     ▇▏◥▇◣┊◢▇◤▕▇
                     ▇▏▃▆▅▎▅▆▃▕▇
                     ▇▏╱▔▕▎▔▔╲▕▇
                     ▇◣◣▃▅▎▅▃◢◢▇
                     ▇▇◣◥▅▅▅◤◢▇▇
                     ▇▇▇◣╲▇╱◢▇▇▇
                     ▇▇▇▇◣▇◢▇▇▇▇

        ђ๏Pє Y๏Ц MąY Gє┼ ๏Ц┼ЙЦMßєrєđ ącc๏ЦЙ┼ş 
       P๏şşIßLY şYЙcђr๏ЙI乙єđ ßY ┼ђIş GI┼ђЦß . 
          ♥️♥️♥️ ßєş┼ ๏F LЦcK  ♥️♥️♥️
      ♥️♥️ rąM乙ąЙ MЦßąrąK ┼๏ єVєrY ß๏đY  ♥️♥️
\033[1;91m=======================================
\033[1;96mAuthor  \033[1;93m: \033[1;92mOYON KHAN
\033[1;96mInstagram \033[1;93m: \033[1:mNai
\033[1;96mFacebook  \033[1;93m: \033[1:mOYON KHAN
\033[1;96mPronhub \033[1;93m: \033[1;92mNai
\033[1;91m======================================="""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\033[1;96m ============================================================="
print  """\033[1;91m
 ░




░█████╗░██╗░░░██╗░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝██╔══██╗████╗░██║
██║░░██║░╚████╔╝░██║░░██║██╔██╗██║
██║░░██║░░╚██╔╝░░██║░░██║██║╚████║
╚█████╔╝░░░██║░░░╚█████╔╝██║░╚███║
░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝


                               
                                
░░██╗██╗░█████╗░░░██╗██╗
░██╔╝██║██╔══██╗░██╔╝██║
██╔╝░██║██║░░██║██╔╝░██║
███████║██║░░██║███████║
╚════██║╚█████╔╝╚════██║
░░░░░╚═╝░╚════╝░░░░░░╚═╝
                        OYON
                     ▇◤▔▔▔▔▔▔▔◥▇
                     ▇▏◥▇◣┊◢▇◤▕▇
                     ▇▏▃▆▅▎▅▆▃▕▇
                     ▇▏╱▔▕▎▔▔╲▕▇
                     ▇◣◣▃▅▎▅▃◢◢▇
                     ▇▇◣◥▅▅▅◤◢▇▇
                     ▇▇▇◣╲▇╱◢▇▇▇
                     ▇▇▇▇◣▇◢▇▇▇▇
                   WhatsApp : +973 3630 5572
\033[1;96mAuthor  \033[1;93m: \033[1;92mOYON KHAN
\033[1;96mInstagram \033[1;93m: \033[1;92mNai
\033[1;96mFacebook  \033[1;93m: \033[1;92mOYON KHAN
\033[1;96mPronhub \033[1;93m: \033[1;92mNai
\033[1;91m======================================="""
print " \x1b[1;93m============================================================="

CorrectUsername = "OYON"
CorrectPassword = "BIKI"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged By Oyon" + username
            loop = 'false'
        else:
            print "Baler Password"
            os.system('xdg-open https://youtube.com/channel/UCZL_Wjboqc4BOSSdHz7SjIQ?sub_confirmation=1 ')
    else:
        print "Wrong Username"
        os.system('xdg-open  https://youtube.com/channel/UCZL_Wjboqc4BOSSdHz7SjIQ?sub_confirmation=1 ')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[☆] \x1b[1;93mLOGIN WITH FACEBOOK \x1b[1;96m[☆]' )
		id = raw_input('\033[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('h
