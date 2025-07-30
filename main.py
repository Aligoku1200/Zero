import os
os.system("pip install amino.li")
import aminoli as A
Ç=A.Client()
E="zxvo@digdig.org"
P="MiRA##"
E1="xzv@usbc.be"
P1="GOKU12"
Ç.login(E1,P1)
L=Ç.get_from_code("http://aminoapps.com/p/v3r9m7")
C=L.comId
O=L.objectId
S=A.SubClient(comId=C,profile=Ç.profile)
S.join_chat(O)
S.send_message(chatId=O,message="99")
print(999999999999999)
