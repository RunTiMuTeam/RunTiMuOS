import ybc_app as a
import ybc_app_ui as u
import os
import time as t
import urllib.request as rq


f = open('data/nm.txt','r')
nm = eval(f.read())
f.close()
f = open('data/language.txt','r')
language = f.read()
f.close()
l_q = 'Quit'
l_ab = 'About'
l_uac = 'User Account Control Settings'
l_ua = 'Users and Groups'
l_sim = 'Cellular'
l_language = 'Language'
l_su = 'Software Update'
l_sb = 'SandBox'
l_r = 'Erase all'
if language == 'zh-CN':
    l_q = '退出'
    l_ab = '关于本机'
    l_uac = '用户账户控制设置'
    l_ua = '用户与组'
    l_sim = '蜂窝网络'
    l_language = '语言'
    l_sb = '沙盒'
    l_r = '抹掉所有内容与设置'
q = u.Button(text=l_q,pos=[300,50])
ab = u.Button(text=l_ab,pos=[200,100])
uac = u.Button(text=l_uac,pos=[200,150])
ua = u.Button(text=l_ua,pos=[200,200])
sim = u.Button(text=l_sim,pos=[200,250])
language = u.Button(text=l_language,pos=[200,300])
su = u.Button(text='Software Update',pos=[200,350])
sb = u.Button(text=l_sb,pos=[200,400])
rb = u.Button(text=l_r,pos=[200,450])
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
    global nm
    if nm:
        a.show_page('page8')
if nm:
    uac.on_click = uacsb
def uasb():
    global nm
    if nm:
        a.show_page('page9')
if nm:
    uasb.on_click = uasb
def osim():
    global nm
    if nm:
        a.show_page('page10')
if nm:
    sim.on_click = osim
def lz():
    global nm
    if nm:
        a.show_page('page13')
if nm:
    language.on_click = lz
def sbs():
    global nm
    if nm:
        a.show_page('page16')
if nm:
    sb.on_click = sbs
def load_ua():
    a.show_page('page17')
ua.on_click = load_ua
def rbz():
    a.show_page('page20')
rb.on_click = rbz
