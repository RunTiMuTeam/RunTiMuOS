import ybc_app as a
import ybc_app_ui as u
import os
import time as t


f = open('data/language.txt','r')
language = f.read()
f.close()
l_s = 'Shut Down'
l_r = 'Restart'
l_b = 'Back To Menu'
if language == 'zh-CN':
    l_s = '关机'
    l_r = '重启'
    l_b = '回到菜单'
s = u.Button(text=l_s,pos=[200,200])
r = u.Button(text=l_r,pos=[200,300])
b = u.Button(text=l_b,pos=[200,400])
def shutdown():
    f = open('data/sr.txt','w')
    f.write('s')
    f.close()
    a.show_page('page6')
s.on_click = shutdown
def restart():
    a.show_page('page2')
r.on_click = restart
def back():
    a.show_page('page2')
b.on_click = back