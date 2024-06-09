import ybc_app_ui as u
import ybc_app as a
import urllib.request as rq
import ybc_box as b


f = open('data/language.txt','r')
language = f.read()
f.close()
l_c = 'Cancel'
l_t1 = 'Activate eSIM'
l_t2 = 'An eSIM from RunTiMu Mobile is\nready to be activated on this device.'
l_ph1 = 'Please enter your esim ticket number.'
l_ab = 'Continue'
l_ab2 = 'Downloading Configuration...'
l_ab3 = 'Activating...'
l_ab4 = 'Setup eSIM Done.'
l_ab5 = 'This eSIM is added!'
l_ab6 = "This eSIM don't in RunTiMu Mobile!"
if language == 'zh-CN':
    l_c = '取消'
    l_t1 = '激活eSIM'
    l_t2 = '一个来自RunTiMu Mobile的eSIM\n已经准备好添加到你的设备了。'
    l_ph1 = '请输入付款后显示的激活码'
    l_ab = '继续'
    l_ab2 = '正在下载配置...'
    l_ab3 = '激活中...'
    l_ab4 = '设置eSIM完成'
    l_ab5 = '这个eSIM已被添加'
    l_ab6 = '该eSIM可能不来自RunTiMu Mobile'
c = u.Button(text=l_c,pos=[300,50])
u.Text(text=l_t1,pos=[200,200],fontsize=40)
u.Text(text=l_t2,pos=[200,300])
ddh1 = u.Textarea(placeholder=l_ph1,pos=[200,450])
ab = u.Button(text=l_ab,pos=[200,625])
#ddh = u.Textarea(placeholder='Please enter your esim ticket number.',pos=[200,400])
def cancel():
    a.show_page('pagedemo2')
c.on_click = cancel
n = 0
def wait():
    global n,wait
    n += 1
    if n == 2:
        a.clear_interval(wait)
def activate():
    global ab,ddh,ddh1,l_ab2,l_ab3,l_ab4,l_ab5,l_ab6
    ab.text = l_ab2
    rq.urlretrieve('http://esim.runtimu.com.cn/numbers.txt','cache/download/numbers.txt')
    f = open('cache/download/numbers.txt','r')
    esim_dictory = eval(f.read())
    f.close()
    ab.text = l_ab3
    rq.urlretrieve('http://esim.runtimu.com.cn/numbers.txt','cache/download/numbers.txt')
    esim = ddh1.text
    #esim = ddh.text
    #print(esim)
    flag = False
    for i in esim_dictory:
        if i == esim:
            flag = True
    if flag:
        flag2 = True
        f = open('phone/esim.txt','r')
        d = eval(f.read())
        f.close()
        for i in d:
            if esim_dictory[esim] == i:
                flag2 = False
        if flag2:
            d[esim_dictory[esim]] = 'RunTiMu Mobile'
            f = open('phone/esim.txt','w')
            f.write(str(d))
            f.close()
            ab.text = l_ab4
            f = open('data/sr.txt','w')
            f.write('s')
            f.close()
            f = open('data/newesim.txt','w')
            f.write('True')
            f.close()
            a.show_page('pagedemo4')
        else:
            ab.text = l_ab5
    else:
        ab.text = l_ab6
ab.on_click = activate