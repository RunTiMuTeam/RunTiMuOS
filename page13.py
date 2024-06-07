import ybc_app as a
import ybc_app_ui as u


q = u.Button(text='Quit',pos=[300,50])
eusa = u.Button(text='English(United States)',pos=[200,200])
zhcn = u.Button(text='简体中文(测试版)(Chinese Simplified(Test))',pos=[200,300])
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
