import subprocess
from multiprocessing import Process
import sys
import requests
import time
import threading as thread
from proxy_requests.proxy_requests import ProxyRequests
import random
import urllib3
import urllib
from requests.utils import unquote
import os
print("Usage NSARSS.py searchterm")

def toes(titty):
    wude = open(yup+"output.txt", 'a')
    try:
        while True:
            cookies = {'c_user': '[cookie]', 'xs': '[cookie]'}
            r = requests.get("https://developers.facebook.com/tools/debug/echo/?q=http://googleweblight.com/?lite_url=https://www.nsa.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType="+titty+"&Site=1282&max=20&s=1&source=wax-m",, allow_redirects=False, cookies=cookies)
            if r.ok:
                buffnet = open('buffnet.txt', 'w')
                print(r.text, file=buffnet)
                r.raise_for_status()
                buffnet.close()
                buffen = open('buffnet.txt', 'r')
                then = subprocess.Popen("grep reach buffnet.txt", stdout=subprocess.PIPE,  stderr = subprocess.PIPE, shell=True)
                thenn = subprocess.Popen("grep 'error occured' buffnet.txt", stdout=subprocess.PIPE,  stderr = subprocess.PIPE, shell=True)
                if then.stdout.readline().decode('utf-8'):
                    print(then)
                    print("\rFile "+str(r.url.rstrip())+" not cached", end="")
                    buffen.close()
                    return 5
                elif thenn.stdout.readline().decode('utf-8'): 
                    print("\rError on facebook", end="")
                    return 6
                    
                else:
                    thun = subprocess.Popen("grep -e "+rer+" buffnet.txt", stdout=subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
                    buffen.close()
                    if thun.stdout.readline().decode('utf-8'):
                        print(r.url+"")
                        print(r.url, file=wude)
                        wude.close()
                        return 4
                    else:
                        print("\rdid not find "+rer+" in "+r.url, end="")
                        return 7
            else:
                print("\rtoo many requests sent to facebook or google", end="")
                return 8
    except Exception as e:
        print("\r"+e, end="")

def taskse(): 
    for i in range(100):
        toes(i)
        time.sleep(10)

if __name__ == '__main__':
    taskse()
