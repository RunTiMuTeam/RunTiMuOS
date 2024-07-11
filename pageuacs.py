import ybc_app as a
import ybc_app_ui as u
import ybc_face as face


f = open('data/language.txt','r')
language = f.read()
f.close()
l_y = 'Yes'
l_n = 'No'
l_p2 = 'Procedure:'
l_uac = 'User Account Control'
l_que = 'Do you want to allow this procedure to \nmake changes to your devices?'
l_pub = 'Verified publisher:'
l_use = 'Use Face ID'
if language == 'zh-CN':
    l_y = '是'
    l_n = '否'
    l_p2 = '程序：'
    l_uac = '用户账户控制'
    l_que = '你允许这个程序去更改该设备的设置？'
    l_pub = '已验证的开发者：'
    l_use = '使用面容ID'
elif language == 'zh-HK':
    l_y = '是'
    l_n = '否'
    l_p2 = '程式：'
    l_uac = '用戶帳戶控制'
    l_que = '你允許這個程式去更改該裝置的設定？'
    l_pub = '已驗證的開發者：'
    l_use = '使用面容ID'
elif language == 'jp':
    l_y = 'はい'
    l_n = 'いいえ'
    l_p2 = 'プログラム：'
    l_uac = 'ユーザーアカウント制御'
    l_que = 'このプログラムでデバイスの設定を変更できますか?'
    l_pub = '検証済み開発者：'
    l_use = '顔IDの使用'
f = open('data/uac_p.txt','r')
p = f.read()
f.close()
f = open('data/uac_pa.txt','r')
pa = f.read()
f.close()
f = open('data/uac_npa.txt','r')
npa = f.read()
f.close()
f = open('data/uac_pub.txt','r')
pubt = f.read()
f.close()
u.Text(text=l_uac,pos=[100,50])
u.Text(text=l_que,pos=[175,150])
p2 = u.Text(text=l_p2 + p,pos=[200,450])
y = u.Button(text=l_y,pos=[200,500])
n = u.Button(text=l_n,pos=[200,600])
pub = u.Text(text=l_pub + pubt,pos=[200,350])
def yb():
    f = open('data/uac_pa.txt','r')
    pa = f.read()
    f.close()
    f = open('data/f_tf.txt','r')
    y2 = eval(f.read())
    f.close()
    if y2:
        d = face.compare('data/cache.jpg','cache/cache2.jpg')
        #debug:print(d)
        if d >= 97:
            a.show_page(pa)
        else:
            a.show_page('page24')
    else:
        a.show_page(pa)
y.on_click = yb
def nb():
    f = open('data/uac_npa.txt','r')
    npa = f.read()
    f.close()
    a.show_page(npa)
n.on_click = nb
def refresh():
    global yb,nb,p2,y,n,pa,npa,pub,y
    f = open('data/uac_p.txt','r')
    p = f.read()
    f.close()
    f = open('data/uac_pa.txt','r')
    pa = f.read()
    f.close()
    f = open('data/uac_npa.txt','r')
    npa = f.read()
    f.close()
    f = open('data/uac_pub.txt','r')
    pubt = f.read()
    f.close()
    f = open('data/f_tf.txt','r')
    y2 = eval(f.read())
    f.close()
    if y2:
        y.text = l_use
    else:
        y.text = l_y
    pub.text = l_pub + pubt
    p2.text = l_p2 + p
a.set_interval(refresh,1)