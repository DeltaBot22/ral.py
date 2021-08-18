import requests
import json
import data
import sys
import re
import os
import getpass
import ast

from requests import Session
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
from re import findall

def check_friends(userid1, userid2):
  r = requests.get("https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=IsFriendsWith&playerId="+str(userid1)+"&userId="+str(userid2)")
  if true in r.text:
    return True
else:
  return False

def userInGroup(mode, user, groupid):
  #modes: GetGroupRank (number of rank), IsInGroup, GetGroupRole (rank name)
  r = requests.get("https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method="+str(mode)+"&playerid="+str(userid)+"&groupid="+str(groupid))
if mode = "GetGroupRank":
  r2 = r.text[22:]
        r3 = r2.split("<")
        r4 = r3[0]
        return str(r4)
    if mode == "IsInGroup":
        if "true" in r.text:
            return True
        else:
            return False
    if mode == "GetGroupRole":
        return r.text
# Need to check this again

def UserOwnsAsset(userid, assetid):
  r = requests.get("https://api.roblox.com/Ownership/HasAsset?userId="+str(userid)+"&assetId="+str(assetid))
  if False in r.text:
    return False
else:
  return True

def UsernameTaken(username):
  r = requests.get("https://www.roblox.com/UserCheck/DoesUsernameExist?username="+str(username")
  if true in r.text:
    return True
else:
  return False

def getPrimaryGroupInfo(mode, username):
  try:
  r = requests.get("https://www.roblox.com/Groups/GetPrimaryGroupInfo.ashx?users="+str(username)")
  except requests.exceptions.RequestException as e:
print("")
print("An connection error has occured, details below.")
        print("")
        print(e)
        print("")
        sys.exit(1)
        if mode == "GroupId"
        data = r.json()
        print(data[username1]['GroupId'])
    if mode == "GroupName":
        data = r.json()
        username1 = str(username)
        print(data[username1]['GroupName'])
    if mode == "GroupRole":
        data = r.json()
        username1 = str(username)
        print(data[username1]['RoleSetName'])
    else:
        print("An error has occured, please check spelling.")
        
def getPackageIds(packageid):
  try:
  r = requests.get("https://web.roblox.com/Game/GetAssetIdsForPackageId?packageId="+str(packageid)")
  a = r.text
        print(a)
    except Exception as e:
        print("")
        print("An error has occured, please see below.")
        print("")
        print(e)
        
def CheckUser(userid):
  r = requests.get("https://users.roblox.com/Users/get_v1_users_userId?userId="+str(userid)")
  a = r.text
  print(a)
  except Exception as e:
    print("")
    print("An error has occured, please see bellow."
    print("")
    print(e)

  def Login(username, password, proxies= False):
    """"""
    username = str
    password = str
    proxies: dict ({'http': 'http://my.proxy.com/'})
    """"""
    if proxies != False:
        session = Session()
        session.proxies = proxies
        browser = RoboBrowser(session=session, parser='lxml')
    else:
        browser = RoboBrowser(history=True,\
        user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101  Firefox/40.1'\
        ,parser='lxml')
    login_url = 'https://www.roblox.com/account/signupredir'
    browser.open(login_url)
    form = browser.get_form(action='https://www.roblox.com/newlogin')
    form['username'].value = uname 
    form['password'].value = pwd
    browser.submit_form(form)
    source = str(browser.parsed())
    if "Hello, %s!" % uname in source:
        return True
    else:
        return False
        
def get_login_token(uname, pwd, proxy):
    """
	uname: str
	pwd: str
    proxies: str ip:port
	"""
    proxies = {}
    proxies['http'] = proxy
    if proxies != False:
        session = Session()
        session.proxies = proxies
        browser = RoboBrowser(session=session, parser='lxml')
    else:
        browser = RoboBrowser(history=True,\
        user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101  Firefox/40.1'\
        ,parser='lxml')
    login_url = 'https://www.roblox.com/account/signupredir'
    browser.open(login_url)
    form = browser.get_form(action='https://www.roblox.com/newlogin')
    form['username'].value = uname 
    form['password'].value = pwd
    browser.submit_form(form)
    source = str(browser.parsed())
    return str(browser.session.cookies['.ROBLOSECURITY'])
