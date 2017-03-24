from django.shortcuts import render
from django.http import HttpResponse
import socket
import mimetypes,os

def get_page(request):
    if request.path == "/" or request.path.find("#") >= 0:
        return render(request,"./home/src/pages/index.html",context={"title":"Super Spider"})
    else:
        pages = [i.replace(".html","") for i in os.listdir("./home/templates/home/src/pages")]
        name = request.path.split("/")[1]
        if name in pages:
            return render(request,"./home/src/pages/%s.html" % name,context={"title": name[0].upper() + name[1:] + " | Super Spider","HOST" : request.META["HTTP_HOST"]})
        else:
            return render(request,"./home/src/notfound.html",status=404)
