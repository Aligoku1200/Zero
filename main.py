import aminoli,time,requests
from telegram import Bot
Ç=aminoli.Client()
TT="8227089815:AAEAWDTBkzNtTfuf0PfFZvh-wEFAKSihU2w"
TC="8100160592"
E="xzv@usbc.be"
P="GOKU12"
Z=Bot(token=TT)
Ç.login(E,P)
L=Ç.get_from_code("http://aminoapps.com/p/4m47igw")
C=L.comId
O=L.objectId
X0=L.objectType
U=[]
z=0
S=aminoli.SubClient(comId=C,profile=Ç.profile)
while True:
	try:
		X1=S.get_all_users(start=0,size=10)
		X2=X1.profile.userId
		for X3 in X2:
			X4=S.get_wall_comments(userId=X3,sorting="oldest",start=0,size=100)
			X5=X4.author.userId
			if X3 in U:
				print(f" — Pass List")
				pass
			else:
				if O in X5:
					U.append(X3)
					z=z+1
					print(f" {z} - Pass")
					pass
				elif X5==[]:
					z=z+1
					print(f" {z} - Done")
					X7=Ç.get_from_id(objectId=X3,objectType=X0,comId=C).shortUrl
					X8=f"{X7}"
					url = f"https://api.telegram.org/bot{TT}/sendMessage"
					params = {"chat_id": TC,"text": X8,"parse_mode": "HTML"}
					response = requests.post(url, params=params)
					U.append(X3)
				elif O not in X5:
					if X5!=[]:
						U.append(X3)
						z=z+1
						print(f" {z} - Already")
						pass
	except:
		pass
	time.sleep(500)
				
