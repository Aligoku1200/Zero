import os
os.system("pip install amino.fix==2.3.6")
import aminofix
Ç=aminofix.Client()
Ç.login(
"zxvo@digdig.org",
"MiRA##")
L=Ç.get_from_code("http://aminoapps.com/p/v3r9m7")
C=L.comId
O=L.objectId
S=aminofix.SubClient(comId=C,profile=Ç.profile)
S.send_message(chatId=O,message="99")
print(999999999999999)
