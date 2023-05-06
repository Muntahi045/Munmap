import os
import time
import requests
import socket 


def munip():
	print("muntahi")
	







print("""[\033[0;36m

  #####                          #     #               
 #     #  ####    ##   #    #    ##   ##  ####  #    # 
 #       #    #  #  #  ##   #    # # # # #    # ##   # 
  #####  #      #    # # #  #    #  #  # #    # # #  # 
       # #      ###### #  # #    #     # #    # #  # # 
 #     # #    # #    # #   ##    #     # #    # #   ## 
  #####   ####  #    # #    #    #     #  ####  #    # 


[ 1 ] Scan 

[ 2 ] get my ip 

[ 3 ] Get ip web

------------------------------------------

""")
muntahi = input("\033[0;34mselect number : ")

if muntahi =="2":
    ip = requests.get("https://api.ipify.org").text
    print (f"\033[0;32m\nYour IP : {ip}")
    host = socket.gethostname()
    hos = socket.gethostbyname(host)
    print (f"\033[0;32m\nYour Host : {hos}")
    os.system("If you want to scanner open tool and select num 1...")
    
if muntahi =="3":
    Domain = input("\033[0;33mEnter Url Web : ")
    ip = socket.gethostbyname(Domain)
    print(ip)
    print("[\033[0;35Want you Scan Open port in this IP (y/n) ?...")
    nb = input("Enter : ")
    if nb =="y":
        os.system("nmap -sT "+ip)
    elif nb =="n":
        time.sleep(0.2)
        print("\nOk...")

if muntahi == "1":
    os.system("clear")    
    print("""\033[0;32m
    
 ######   ######     ###    ##    ## 
##    ## ##    ##   ## ##   ###   ## 
##       ##        ##   ##  ####  ## 
 ######  ##       ##     ## ## ## ## 
      ## ##       ######### ##  #### 
##    ## ##    ## ##     ## ##   ### 
 ######   ######  ##     ## ##    ## 
    
    
    
    
   [ A ] Scan open port in network 
   
   [ B ] Scan devices connected with you
   
   [ C ] Scan open port in you IP 
  
  ------------------------------------------
  
    """)
    i = input("\033[0;34mSelect : ")
    if i =="A":
        o=input("Enter IP Network : ")
        os.system("nmap -sT "+o)
    if i =="B":
        om = input("Enter Network IP : ")
        os.system("nmap -sP "+om+"/24")

    if i=="C":
        ip = input("Enter Ip : ")

        os.system("nmap -sT "+ip)
        time.sleep(5.5)
        os.system("Muntahi")  

