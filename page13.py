import ybc_app as a
import ybc_app_ui as u


q = u.Button(text='Quit',pos=[300,50])
eusa = u.Button(text='English(United States)',pos=[200,200])
zhcn = u.Button(text='简体中文(Chinese Simplified)',pos=[200,300])
zhhk = u.Button(text='繁體中文(測試版)(Chinese Traditional(Test))',pos=[200,400])
enuk = u.Button(text='English(United Kingdom)',pos=[200,500])
jp = u.Button(text='日本語(テスト版)(Japanese(test))',pos=[200,600])
def quit1():
    a.show_page('page3')
q.on_click = quit1
def eusaz():
    f = open('data/language.txt','w')
    f.write('en-US')
    f.close()
    a.show_page('page6')
eusa.on_click = eusaz
def zhcnz():
    f = open('data/language.txt','w')
    f.write('zh-CN')
    f.close()
    a.show_page('page6')
zhcn.on_click = zhcnz
def zhhkz():
    f = open('data/language.txt','w')
    f.write('zh-HK')
    f.close()
    a.show_page('page6')
zhhk.on_click = zhhkz
def enukz():
    f = open('data/language.txt','w')
    f.write('en-UK')
    f.close()
    a.show_page('page6')
enuk.on_click = enukz
def jpz():
    f = open('data/language.txt','w')
    f.write('jp')
    f.close()
    a.show_page('page6')
jp.on_click = jpz
