import ybc_app as a
import ybc_app_ui as u
import os
import time as t


u.Text(text='Version',pos=[100,100])
u.Text(text='3.0',pos=[300,100])
r = u.Button(text='Back',pos=[50,50])
def return1():
    a.show_page('page3')
r.on_click = return1
