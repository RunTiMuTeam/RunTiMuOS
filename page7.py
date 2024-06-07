import ybc_app as a
import ybc_app_ui as u
import os
import time as t
import ybc_box as b


f = open('data/language.txt','r')
language = f.read()
f.close()
l_p = 'Play'
l_q = 'Quit'
l_p2 = 'Please choose the music.'
if language == 'zh-CN':
    l_p = '播放'
    l_q = '退出'
    l_p2 = '请选择音乐!'
files = os.listdir('music')
option = u.Select(options=files,pos=[200,200])
p = u.Button(text=l_p,pos=[200,300])
q = u.Button(text=l_q,pos=[200,400])
def play():
    global files,option,p
    if option.text == '':
        p.text = l_p2
    else:
        a.Music('music/' + option.text)
p.on_click = play
def quit1():
    a.show_page('page2')
q.on_click = quit1