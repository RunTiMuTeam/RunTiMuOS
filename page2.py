import ybc_app as a
import ybc_app_ui as u
import os
import time as t


ti = u.Text(text=t.ctime(),pos=[200,200])
r = u.Button(text='Refesh',pos=[200,300])
b = u.Button(text='Settings',pos=[200,400])
m = u.Button(text='Music',pos=[200,500])
p = u.Button(text='Power',pos=[200,600])
def settings():
    a.show_page('page3')
b.on_click = settings
def refesh():
    ti.text = t.ctime()
r.on_click = refesh
def power():
    a.show_page('page5')
p.on_click = power
def music():
    a.show_page('page7')
m.on_click = music