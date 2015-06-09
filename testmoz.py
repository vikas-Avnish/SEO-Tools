from Crypto.Hash import SHA, HMAC
import hashlib
import hmac
import time,base64,urllib,urllib2,requests
import json
import csv
import re
with open('output.csv','a') as csvfile:
        fieldnames = ['site', 'da','pa']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
def write(i,j,k):
    with open('output.csv','a') as csvfile:
        fieldnames = ['site', 'da','pa']
        #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'site': i, 'da': j,'pa':k})
access_id="mozscape-2881bd3045"
key="b4a57ea036640cd1f79411d510db0492"
statfile="input.csv"
def strip(a):                                           
   return  re.sub(r'\s+', ' ', a).lstrip().rstrip().replace(" ","+")
def getmozdata(l):
	print l
	expires = int(time.time() + 3000)
	toSign  = '%s\n%i' % (access_id, expires)
	hashkey=base64.b64encode(hmac.new(key, toSign, hashlib.sha1).digest())
	mozurl='http://lsapi.seomoz.com/linkscape/url-metrics/'+l+'?Cols=144115291691993125'+'&AccessID=mozscape-2881bd3045&Expires='+str(expires)+'&Signature='+hashkey
	print mozurl
	getdata=requests.get(mozurl)
	k=json.loads(getdata.content)
	status=getdata.status_code
	if(status==401):
		getmozdata(l)
		time.sleep(10)
	else:
		time.sleep(10)
		pa= k[u'upa']
		da=k[u'pda']
		print k
		write(keys,da,pa)
		#time.sleep(10)
	

with open(statfile) as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
	keys=strip(row['URL']).lower()
	getmozdata(keys)
	#write(keys,da)
	#time.sleep(10)
