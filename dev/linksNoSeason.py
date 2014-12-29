import json
import os
import sys
import re
import sys, traceback
from time import sleep

import requests


def systemFilename(name):
    name = name.replace(" ", "-")
    name = re.sub(r'[^\w-]', '', name)
    return name.lower()


filename = sys.argv[1]
cookie = sys.argv[2]
mediaType = sys.argv[3]
try:
    with open(filename) as data_file:
        os.system("clear")
        data = json.load(data_file)
        print "\n=== "+data['title']+" ==="
        links = "http://series.ly/scripts/media/epLinks.php?mediaType="+mediaType+"&idc=" + str(data['idm'])
        cookieRequest = {"PHPSESSID": cookie}

        linkFileString = ""

        counter = 0
        while True:
            r = requests.get(links, cookies=cookieRequest, allow_redirects=False)
            if r.status_code == 200:
                data['links'] = json.loads(r.text)['links']
                print str(r.status_code)+" Downloading "+str(len(data['links']))
                break
            else:
                counter += 0.1
                sleep(counter)
                print "******"+str(r.status_code)+" Overload*******"
        i = 0
        for link in data['links']:
            try:
                linkUrl = "http://series.ly/scripts/media/gotoLink.php?idv="+str(link['idv'])+"&mediaType="+mediaType+"&idm="+str(data['idm'])
                counter2 = 0
                while True:
                    r = requests.get(linkUrl, cookies=cookieRequest, allow_redirects=False)
                    try:
                        link['url'] = r.headers['Location']
                        linkFileString += link['url'] + "\n"
                        if '/f5.html' in link['url']:
                            print "*******Overload*******"
                            pass
                        elif 'ganaPuntos.php' in link['url']:
                            print "*******GANA PUNTOS*******"
                            pass
                        else:
                            print "->"+link['url']
                            break
                        # counter2 += 0.1
                        # sleep(counter2)
                    except KeyError:
                        print "*******"+str(r.status_code)+" KeyError*******"
                        # counter2 += 0.1
                        # sleep(counter2)
                        pass
            except ValueError:
                print "***********LINK ERROR"
        folderName = systemFilename(data['title'])
        folderNameLength = min(50, len(folderName))
        folderName = folderName[:folderNameLength]
        rootFolderName = filename.split('/', 1)[0]
        onlyName = filename.split('/', 1)[1].split('.')[0]
        mkDir = "mkdir -p "+rootFolderName+"/"+folderName+"/"
        os.system(mkDir)
        data_file.close()

    with open(rootFolderName+"/"+folderName+"/data.json", 'w') as outfile:
        json.dump(data, outfile)

    with open(rootFolderName+"/"+folderName+"/links.txt", 'w') as linksoutfile:
        linksoutfile.write(linkFileString)
    rvFile = "rm "+filename
    os.system(rvFile)
    print "###########END"
except ValueError:
    print "***********ERROR"
