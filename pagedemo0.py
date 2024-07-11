import ybc_app as a
import ybc_app_ui as u


eusa = u.Button(text='English(United States)',pos=[200,200])
zhcn = u.Button(text='简体中文(Chinese Simplified)',pos=[200,300])
zhhk = u.Button(text='繁體中文(測試版)(Chinese Traditional(Test))',pos=[200,400])
off = u.Button(text='Shut down',pos=[200,500])
'''
def quit1():
    a.show_page('page3')
q.on_click = quit1
'''
def eusaz():
    f = open('data/language.txt','w')
    f.write('en-US')
    f.close()
    a.show_page('pagedemo1')
eusa.on_click = eusaz
def zhcnz():
    f = open('data/language.txt','w')
    f.write('zh-CN')
    f.close()
    a.show_page('pagedemo1')
zhcn.on_click = zhcnz
off.on_click = quit
def zhhkz():
    f = open('data/language.txt','w')
    f.write('zh-HK')
    f.close()
    a.show_page('pagedemo1')
zhhk.on_click = zhhkz
