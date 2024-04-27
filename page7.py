import ybc_app as a
import ybc_app_ui as u
import os
import time as t
import ybc_box as b


files = os.listdir('music')
option = u.Select(options=files,pos=[200,200])
p = u.Button(text='Play',pos=[200,300])
q = u.Button(text='Quit',pos=[200,400])
def play():
    global files,option,p
    if option.text == '':
        p.text = 'Please choose the music.'
    else:
        a.Music('music/' + option.text)
p.on_click = play
def quit1():
    a.show_page('page2')
q.on_click = quit1