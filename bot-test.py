import requests
import csv,codecs, cStringIO
kk="google AltaVista Express rafula GrabNet Teleport Twengabot bing bingbot Googlebot WebPictures HMView NetSpider VoidEYE htmlparser yandex Slurp ExtractorPro HTTrack Vampire Collector libwww msnbot BlackWidow EyeNetIE Stripper NetZIP WebAuto Python Bot FlashGet Sucker Octopus WebCopier perl ChinaClaw GetRight Indy Offline WebFetch urllib Custo GetWeb! InterGET PageGrabber WebGo scan DISCo Go!Zilla Ninja Foto WebLeacher Curl Download Go-Ahead-Got-It JetCar pavuk WebReaper email Demon GrabNet Spider pcBrowser WebSauger PycURL eCatch Grafula larbin RealDownload eXtractor Pyth EirGrabber HMView LeechFTP ReGet Quester PyQ EmailSiphon Go!Zilla Downloader SiteSnagger WebStripper WebCollector EmailWolf Go-Ahead-Got-It tool SmartDownload WebZIP WebCopy SuperHTTP Navroad SuperBot Wget webcraw Surfbot NearSite WebSpider Widow WebWhacker NetAnts Zeus tAkeOut WWWOFFLE"
tt=kk.split(" ")
# insert your site name here
# site = " your site"  and uncomment  it
for i in range(0,len(tt)):
    bot={'user-agent':'Mozilla/5.0 (compatible; '+tt[i]+'; +http://www.google.com/fdghdfg.htm)'}
    k=requests.get(site,headers=bot)
    print k.status_code,tt[i]
    open("out.txt","a").write(str(k.status_code)+ "\t" +tt[i]+"\n")
