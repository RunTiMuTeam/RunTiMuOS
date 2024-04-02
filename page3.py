import ybc_app as a
import ybc_app_ui as u
import os
import time as t


q = u.Button(text='Quit',pos=[300,50])
ab = u.Button(text='About',pos=[200,200])
uac = u.Button(text='User Account Control Settings',pos=[200,300])
ua = u.Button(text='Users and Groups',pos=[200,400])
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
