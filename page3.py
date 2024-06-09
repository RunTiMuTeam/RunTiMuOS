import ybc_app as a
import ybc_app_ui as u
import os
import time as t
import urllib.request as rq


q = u.Button(text='Quit',pos=[300,50])
ab = u.Button(text='About',pos=[200,100])
uac = u.Button(text='User Account Control Settings',pos=[200,200])
ua = u.Button(text='Users and Groups',pos=[200,300])
sim = u.Button(text='Cellular',pos=[200,400])
language = u.Button(text='Language',pos=[200,500])
su = u.Button(text='Software Update',pos=[200,600])
def suz():
    global su
    rq.urlretrieve('http://download.runtimu.com.cn/runtimuos/update/newbeta.txt','cache/download/new.txt')
    f = open('version/version.txt','r')
    version = f.read()
    f.close()
    f = open('cache/download/new.txt','r')
    new = f.read()
    f.close()
    if new != version:
        su.text = 'Please to download.URL:https://www.runtimu.com.cn/download/runtimuos/'
    else:
        su.text = 'This version is newest!'
su.on_click = suz
def about():
    a.show_page('page4')
ab.on_click = about
def quit1():
    a.show_page('page2')
q.on_click = quit1
def uacsb():
    a.show_page('page8')
uac.on_click = uacsb
def uasb():
    a.show_page('page9')
uasb.on_click = uasb
def osim():
    a.show_page('page10')
sim.on_click = osim
def lz():
    a.show_page('page13')
language.on_click = lz
