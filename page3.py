import ybc_app as a
import ybc_app_ui as u
import os
import time as t


q = u.Button(text='Quit',pos=[300,50])
ab = u.Button(text='About',pos=[200,200])
def about():
    a.show_page('page4')
ab.on_click = about
def quit1():
    a.show_page('page2')
q.on_click = quit1