import ybc_app as a
import ybc_app_ui as u
import os
import time as t


u.Text('RunTiMu',pos=[190,300],fontsize=45)
#step = 0
f = open('version/new.txt')
new = f.read()
f.close()
f = open('version/version.txt')
version = f.read()
f.close()
if new == version:
    state = True
else:
    state = False
    u.Text('Warning!Boot Error!',pos=[200,550])
files_list = os.listdir('phone')
if 'model.txt' not in files_list:
    state = False
    u.Text("Can't know your device model.",pos=[200,650])
def nextpage():
    a.clear_interval(nextpage)
    a.show_page('page2')
'''
def step1():
    global step
    step += 1
def step2():
    global step,state
    if step == 1:
        f = open('version/setup.txt','r')
        tf = f.read()
        f.close()
    elif step == 2:
        w = u.Text('Verifying Boot...',pos=[200,400])
        f = open('version/new.txt')
        new = f.read()
        f.close()
        f = open('version/version.txt')
        version = f.read()
        f.close()
        if new == version:
            state = True
        else:
            state = False
            u.Text('Warning!Boot Error!',pos=[200,550])
    elif step == 3 and state == True:
        g = u.Text('Starting Driver...',pos=[200,425])
    elif step == 4 and state == True:
        u.Text('Verifying RunTiMuOS...',pos=[200,450])
    elif step == 5 and state == True:
        u.Text('Enabling Application...',pos=[200,475])
    elif step == 6 and state == True:
        u.Text('Enabling SIP...',pos=[200,500])
    elif step == 7 and state == True:
        u.Text('Starting Service...',pos=[200,525])
    elif step == 8 and state == True:
        u.Text('Opening Desktop...',pos=[200,550])
        u.Text('Done.',pos=[200,575])
        s = u.Button(text='Start',pos=[200,625])
        def start():
            a.show_page('page2')
        s.on_click = start
a.set_interval(step1,3)
a.set_interval(step2,3)
'''
if state:
    a.set_interval(nextpage,3)