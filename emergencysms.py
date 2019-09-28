import MySQLdb
import time
from twilio.rest import Client
tempcount=0
hrcount=0
# Find these values at https://twilio.com/user/account
account_sid = "ACceab8766bd386775134b522156411c03"
auth_token = "68d2826656c3ce645d27d3bd912a53ba"
client = Client(account_sid, auth_token)
while 1:
 db = MySQLdb.connect(host="192.168.69.4",port=3306,user="sush",passwd="sush1",db="health")

 cursor=db.cursor()
 cursor.execute("select id,pid,hr,temp from stats")
 results=cursor.fetchall()
 for re in results:
    continue
 print re[0]
 #print"lo"
 if(tempcount>10):
    
    print "yoyo"
    message = client.api.account.messages.create(
    to="+918762357332",
    from_="+17609194510",
    body="patient"+str(re[1])+" temperature alert",)

    tempcount=0
 if(hrcount>10):
    print "koko"
    message = client.api.account.messages.create(
    to="+918762357332",
    from_="+17609194510",
    body="patient"+str(re[1])+" heart rate alert",)

    hrcount=0
 #print"lu"
 if(re[2]>=100):
    tempcount=tempcount+1
 if(re[3]>=100):
    hrcount=hrcount+1
 time.sleep(1.5)   
   


