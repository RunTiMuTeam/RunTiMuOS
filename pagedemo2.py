import ybc_app as a
import ybc_app_ui as u


f = open('data/language.txt','r')
language = f.read()
f.close()
l_q = 'Back'
l_a = 'Add eSIM'
l_b = 'Set'
l_m = 'Skip'
if language == 'zh-CN':
    l_q = '返回'
    l_a = '添加eSIM'
    l_b = '设置'
    l_m = '跳过'
q = u.Button(text=l_q,pos=[50,50])
b = u.Button(text=l_b,pos=[200,300])
m = u.Button(text=l_m,pos=[200,400])
def quit1():
    a.show_page('pagedemo1')
q.on_click = quit1
tip = u.Text(text=l_a,pos=[200,100],fontsize=45)
def lb():
    a.show_page('pagedemo3')
b.on_click = lb
def lm():
    a.show_page('pagedemo4')
m.on_click = lm
