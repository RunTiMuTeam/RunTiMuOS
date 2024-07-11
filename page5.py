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
    l_r = '重新启动'
    l_b = '回到菜单'
elif language == 'zh-HK':
    l_s = '關機'
    l_r = '重新啟動'
    l_b = '回到菜單'
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
    a.show_page('page0')
    a.go()
r.on_click = restart
def back():
    a.show_page('page2')
b.on_click = back