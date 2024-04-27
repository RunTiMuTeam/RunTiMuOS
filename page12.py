import ybc_app_ui as u
import ybc_app as a
import urllib.request as rq
import ybc_box as b


c = u.Button(text='Cancel',pos=[300,50])
u.Text(text='Activate eSIM',pos=[200,200],fontsize=40)
u.Text(text='An eSIM from RunTiMu Mobile is\nready to be activated on this device.',pos=[200,250])
ab = u.Button(text='Continue',pos=[200,625])
#ddh = u.Textarea(placeholder='Please enter your esim ticket number.',pos=[200,400])
def cancel():
    a.show_page('page10')
c.on_click = cancel
n = 0
def wait():
    global n,wait
    n += 1
    if n == 2:
        a.clear_interval(wait)
def activate():
    global ab,ddh
    ab.text = 'Downloading Configuration...'
    rq.urlretrieve('http://esim.runtimu.com.cn/numbers.txt','cache/download/numbers.txt')
    f = open('cache/download/numbers.txt','r')
    esim_dictory = eval(f.read())
    f.close()
    ab.text = 'Activating...'
    esim = a.get('esim')
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
            a.show_page('page10')
        else:
            ab.text('This eSIM is added！')
    else:
        ab.text("This eSIM don't in RunTiMu Mobile!")
ab.on_click = activate