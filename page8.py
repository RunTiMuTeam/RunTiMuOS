import ybc_app as a
import ybc_app_ui as u


f = open('data/language.txt','r')
language = f.read()
f.close()
l_q = 'Quit'
l_b = 'Disable User Account Control(Not Recommended)'
l_m = 'Enable User Account Control'
if language == 'zh-CN':
    l_q = '退出'
    l_b = '禁用用户账户控制(不建议)'
    l_m = '启用用户账户控制'
q = u.Button(text=l_q,pos=[300,50])
b = u.Button(text=l_b,pos=[200,300])
m = u.Button(text=l_m,pos=[200,400])
def bz():
    f = open('data/uac.txt','w')
    f.write('False')
    f.close()
b.on_click = bz
def mz():
    f = open('data/uac.txt','w')
    f.write('True')
    f.close()
m.on_click = mz
def quit1():
    a.show_page('page3')
q.on_click = quit1
