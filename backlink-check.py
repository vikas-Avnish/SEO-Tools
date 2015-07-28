mheaders =  {'user-agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'}
dheaders={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}
import requests
import ssl
import csv,codecs, cStringIO
import re
import time,random
import webbrowser
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from bs4 import BeautifulSoup as bs
from urllib import urlencode
srcfile="craftvillabacklinks.csv"
def strip(a):                                           
   return  re.sub(r'\s+', ' ', a).lstrip().rstrip()
with open('abcout.csv','a') as csvfile:
        fieldnames = ['Domain','Src','Number of Links','Title','Anchor Text','Target URL','Follow Type','Sorround Text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
def write(a,b,c,d,e,f,g,h):
    with open('abcout.csv','a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Domain':a,'Src':b,'Number of Links':h,'Title':c,'Anchor Text':d,'Target URL':e,'Follow Type':f,'Sorround Text':g})
def getinfo(i):
    j=requests.get(i,headers=dheaders)
    j=bs(j.content)
    domain=re.match("http[s]?[://][\w.-_]+",i).group()
    #print domain
    try:
        title=j.find('title').getText()
        #print "\t" +title
        l=j.findAll("a",href=re.compile("craftsvilla.com"))
        #print len(l)
        num=len(l)
        if len(l)>0:
            try:
                num=len(l)
                for m in l:
                    link=m.attrs['href']
                    anchor=strip(m.getText())
                    sorround_text=strip(m.parent.text)
                    #print i,"  >> ",m.attrs['href'],strip(m.getText()),strip(m.parent.text)
                    try:
                        try:
                            #print m.attrs['rel']
                            follow=m.attrs['rel']
                        except:
                            #print "Dofollow possibly"
                            follow="Dofollow"
                    except:
                        print "could not fetch information"
                    print (domain,i,title,anchor,link,follow,sorround_text,num)
                    write (domain,i,title,anchor,link,follow,sorround_text,num)
            except:
                print "more"
            
        else:
            print "No links"
        
    except:
        print "do more"
with open("craftvillabacklinks.csv") as csvs:
    reader=csv.DictReader(csvs)
    index=[]
    for s in reader:
        index.append(s["source_url"])
        #getinfo(s["Links"])
for i in range(int(sys.argv[1]),int(sys.argv[2])):
        try:
		getinfo(index[i])
	except:
		open("craftreportfailed.txt","a").write(str(i)+"\t")
	open("craftreport.txt","a").write(str(i)+"\t")
