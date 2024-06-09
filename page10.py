import ybc_app_ui as u
import ybc_app as a


f = open('data/language.txt','r')
language = f.read()
f.close()
l_ns = "Your device doesn't support SIM."
l_esim = 'Set up eSIM'
l_rm = 'Remove eSIM'
l_r = 'Back'
if language == 'zh-CN':
    l_ns = '你的设备不支持实体SIM卡'
    l_esim = '设置eSIM'
    l_rm = '删除eSIM'
    l_r = '返回'
ns = u.Text(text=l_ns,pos=[200,100])
esim = u.Button(text=l_esim,pos=[200,200])
rm = u.Button(text=l_rm,pos=[200,300])
r = u.Button(text=l_r,pos=[50,50])
start = 400
f = open('phone/esim.txt','r')
dictory = eval(f.read())
f.close()
if dictory != {}:
    for i in dictory:
        u.Text(text=dictory[i] + '\n' + i,pos=[200,start])
        start += 50
def return1():
    a.show_page('page3')
r.on_click = return1
def setupesim():
    a.show_page('page12')
esim.on_click = setupesim
def remove1():
    a.show_page('page14')
rm.on_click = remove1
