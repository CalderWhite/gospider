from django.shortcuts import render
from django.http import HttpResponse
import os

class api:
    def response(request):
        SECTION_PATH = "./docs/templates/docs/api/sections"
        nav_paths = []
        section_paths = []
        for path in reversed(os.listdir(SECTION_PATH)):
            nav_paths.append(SECTION_PATH[SECTION_PATH.find("templates")+len("templates/"):] + "/" + path + "/nav.html")
            section_paths.append(SECTION_PATH[SECTION_PATH.find("templates")+len("templates/"):] + "/" + path + "/section.html")
        data = {
            "title" : "Docs | Api",
            "nav_paths" : nav_paths,
            "section_paths" : section_paths,
            "HOST" : request.META["HTTP_HOST"]
        }
        return render(request,"docs/api/index.html",context=data)
    def index(request):
        pp = request.path.split("/")[1:]
        if len(pp) < 3:
            return api.response(request)
        if pp[2] == "/" or request.path.find("#") >= 0 or pp[2] == "":
            return api.response(request)
        else:
            return HttpResponse(request.path + " is invalid.",content_type="text/plain")
