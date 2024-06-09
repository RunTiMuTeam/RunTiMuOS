import ybc_app as a
import ybc_app_ui as u
import os
import time as t


ti = u.Text(text=t.ctime(),pos=[200,200])
f = open('data/language.txt','r')
language = f.read()
f.close()
f = open('data/nm.txt','r')
nm = eval(f.read())
f.close()
l_s = 'Settings'
l_m = 'Music'
l_p = 'Power'
l_m2 = 'Message'
if not nm:
    u.Text(text='Safe Mode',pos=[200,100])
if language == 'zh-CN':
    if nm:
        tip = u.Text(text='目前汉化程序还未制作完毕，请见谅!',pos=[200,100])
    l_s = '设置'
    l_m = '音乐'
    l_p = '电源'
    l_m2 = '信息'
b = u.Button(text=l_s,pos=[200,300])
m = u.Button(text=l_m,pos=[200,400])
p = u.Button(text=l_p,pos=[200,500])
m2 = u.Button(text=l_m2,pos=[200,600])
def message():
    global nm
    if nm:
        a.show_page('page15')
m2.on_click = message
def settings():
    f = open('data/uac.txt','r')
    tf = eval(f.read())
    f.close()
    if tf and nm:
        a.show_page('pageuacs')
    else:
        a.show_page('page3')
b.on_click = settings
def refesh():
    ti.text = t.ctime()
def power():
    a.show_page('page5')
p.on_click = power
def music():
    global nm
    if nm:
        a.show_page('page7')
m.on_click = music
a.set_interval(refesh,1)