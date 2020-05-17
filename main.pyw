import time
from datetime import datetime as dt

# hosts_temp=r"hosts"

#for windows users
hosts_path="C:\Windows\System32\drivers\etc\hosts"

#-----------------------------------------------
#for mac/linux users
#hosts_path="/etc/hosts"
#---------------------------------------------

#dont change this , it's the local host address
redirect="127.0.0.1"

#enter your desired website in website_list 
website_list=["your desired website 1","your desired website 2 ","your desired website 3"]


#Here in line number 25 
#9 represents 9:00 AM and 17 represents 5:00 PM 
#follow 24hrs clock format and change to your liking.


while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
	
		with open(hosts_path,'r+') as file:
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website+"\n" )
	
	
	else:
		with open(hosts_path,'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
		print("P")
	time.sleep(2)