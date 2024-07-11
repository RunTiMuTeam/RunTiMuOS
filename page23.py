import ybc_app as a
import ybc_app_ui as u
import ybc_face as face
import ybc_camera as c


f = open('data/language.txt','r')
language = f.read()
f.close()
l_p = 'Enable Face ID'
l_d = 'Disable Face ID'
l_b = 'Back'
if language == 'zh-CN':
    l_p = '启用面容ID'
    l_d = '禁用面容ID'
    l_b = '返回'
elif language == 'zh-HK':
    l_p = '啟用面容ID'
    l_d = '禁用面容ID'
    l_b = '返回'
q = u.Button(text=l_b,pos=[50,50])
def quit1():
    a.show_page('page3')
q.on_click = quit1
p = u.Button(text=l_p,pos=[200,300])
d = u.Button(text=l_d,pos=[200,400])
def rd():
    f = open('data/f_tf.txt','w')
    f.write('False')
    f.close()
d.on_click = rd
def rp():
    #c.camera('data/cache.jpg')
    f = open('data/f_tf.txt','w')
    f.write('True')
    f.close()
p.on_click = rp
