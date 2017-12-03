from django.http import HttpResponse
from datetime import datetime
import string
import random
import shutil
import os

TMP_DIR = "/tmp/"

def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_ctime
    return list(sorted(os.listdir(path), key=mtime))

def get_random_chars(length=5):
    chars = []
    for i in range(length):
        chars.append(random.choice(string.ascii_letters))
    return ''.join(chars)


def date(request):
    return HttpResponse("System time: " + str(datetime.now()))

def create(request):
    try:
        for i in range(10000):
            open(os.path.join(TMP_DIR, get_random_chars(10)), 'a').close()
        return HttpResponse("10000 temporary files created")
    except Exception, e:
        print str(e)
        return HttpResponse("Respone 503: Unable to create 10000 temporary files", status=503)
    
def delete(request):
    try:
        print request.path_info
        n = os.path.basename(request.path_info)
        to_be_deleted = int(n)
        files_list = sorted_ls(TMP_DIR)
        if int(n) > len(files_list):
            to_be_deleted = len(files_list)
        for i in range(to_be_deleted):
            loc = os.path.join(TMP_DIR, files_list[i])
            if os.path.isfile(loc):
                os.remove(loc)
        return HttpResponse(str(to_be_deleted) + " old temporary files deleted")
    except Exception, e:
        print str(e)
        return HttpResponse("Respone 503: Unable to delete " + str(to_be_deleted) + " old temporary files", status=503)  
