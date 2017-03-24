from django.shortcuts import render
from django.http import HttpResponse
import json
import superspider.scraper
import urllib.parse

class mainWebApp(object):
    def __init__(self):
        pass
    def get_summary(self,request):
        meta = dict([tuple(a.split("=")) for a in request.META["QUERY_STRING"].split("&")])
        url = urllib.parse.unquote(meta["url"])
        d = superspider.scraper.scrape(url,silent=True)
        for p in range(len(d["data"])):
            d["data"][p][0] = ",".join(d["data"][p][0])
        z = {}
        for a,b in d["data"]:
            z[a] = b
        data = {
            "content" : z,
            "url" : url,
            "time" : d["time"],
            "Stype" : d["type"]
        }
        return render(request,"./app/src/results.html",context=data)

def index(request):
    return render(request,"./app/src/app.html")
def get_summary(request):
    app_instance = mainWebApp()
    return app_instance.get_summary(request)
