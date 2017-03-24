from django.shortcuts import render
from django.http import HttpResponse
import json, sys
import urllib.error
import superspider.scraper
#
## util functions
#
def messageResponse(msg,status=200):
    r = {
        "message" : msg,
        "status_code": status
    }
    return HttpResponse(json.dumps(r,indent=4),content_type="application/json",status=status)
#
## Actual "application". Not the interface
#
def summarize(url):
    try:
        o = superspider.scraper.scrape(url,silent=True)
    except urllib.error.URLError as error:
        if str(error).lower().find("SSL: UNKNOWN_PROTOCOL".lower()) >= 0:
            return messageResponse("Unknown SSL protocal. Human version: try switching [https://] to [http://], or vice versa.",status=525)
        else:
            return messageResponse("The server has hit an unanticipated error. Please share your error with the system administrator, so it can be patched for the future.",status=520)
    else:
        j = {
            "passages" : o["data"],
            "generated_time" : o["time"],
            "structure" : o["type"]
        }
        return HttpResponse(json.dumps(j,indent=4),content_type="application/json",status=200)
#
## Response functions
#
def summary(request):
    parsed = request.path.split("/")
    if request.META["QUERY_STRING"] != "":
        print([tuple(a.split("=")) for a in request.META["QUERY_STRING"].split("&")])
        queries = dict([tuple(a.split("=")) for a in request.META["QUERY_STRING"].split("&")])
        try:
            queries["url"]
        except KeyError:
            return messageResponse("Missing [url] QUERY_STRING variable.",status=412)
        else:
            return summarize(queries["url"])
        return HttpResponse("<pre>%s</pre>" % queries["url"])
    else:
        return messageResponse("Missing QUERY_STRING.",status=412)
def notfound(request):
    return messageResponse("%s is not a valid request path." % request.path,status=404)
