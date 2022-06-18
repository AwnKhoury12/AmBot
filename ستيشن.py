import os
try:
	import aminofix
	import pyfiglet
except:
	os.system("pip install pyfiglet")
	os.system("pip install amino.fix==2.2.7")
	
e = "\033[45;30m_\033[m"
d = "\n\033[1;31m"
i = "\033[1;92m"
g = "sid="

os.system("clear")
print(d+pyfiglet.figlet_format("S I D", font="big"))
Client=aminofix.Client()
print (e*60)
email=input("\033[1;93m\nEmail >> ")
print ("\033[1;91m_"*20)
password=input("\033[1;93m\nPassword >> ")
Client.login(email=email,password=password)
Client.sid=(Client.sid)
os.system("clear")
print(i+g+Client.sid)