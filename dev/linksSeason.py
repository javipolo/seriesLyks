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
mediaType = str(5)

with open(filename) as data_file:
    data = json.load(data_file)
    os.system("clear")
    print "=== " + data['title'] + " ==="

    folderName = systemFilename(data['title'])
    folderNameLength = min(50, len(folderName))
    folderName = folderName[:folderNameLength]
    rootFolderName = filename.split('/', 1)[0]
    onlyName = filename.split('/', 1)[1].split('.')[0]
    os.system("mkdir -p " + rootFolderName + "/" + folderName + "/")
    try:
        for i in data['episodes']:
            print "=== Season " + str(i) + " ==="
            season = data['episodes'][i]
            seasonPath = rootFolderName + "/" + folderName + "/season" + i + "/"
            os.system("mkdir -p " + seasonPath)

            for episode in season:
                print "=== " + data['title'] + " === Episode " + str(episode['num']) + " ==="
                links = "http://series.ly/scripts/media/epLinks.php?mediaType=" + mediaType + "&idc=" + str(
                    episode['idc'])
                cookieRequest = {"PHPSESSID": cookie}
                try:
                    counter = 0
                    while True:
                        r = requests.get(links, cookies=cookieRequest, allow_redirects=False)
                        if r.status_code == 200:
                            episode['links'] = json.loads(r.text)['links']
                            break
                        else:
                            # counter += 1
                            # sleep(counter)
                            print "******"+str(r.status_code)+" Overload*******"
                    linkFileString = ""
                    episodePath = seasonPath + "episode" + str(episode['num']) + ".txt"
                    os.system("touch " + episodePath)
                    print "Downloading "+str(len(episode['links']))
                    for link in episode['links']:
                        linkUrl = "http://series.ly/scripts/media/gotoLink.php?idv=" + str(
                            link['idv']) + "&mediaType=" + mediaType + "&idm=" + str(data['idm'])
                        counter2 = 0
                        while True:
                            r = requests.get(linkUrl, cookies=cookieRequest, allow_redirects=False)
                            try:
                                link['url'] = r.headers['Location']
                                linkFileString += link['url'] + "\n"
                                if '/f5.html' in link['url']:
                                    print link['url']
                                    print "*******Overload*******"
                                    pass
                                elif 'ganaPuntos.php' in link['url']:
                                    print "*******GANA PUNTOS*******"
                                    pass
                                else:
                                    print link['url']
                                    break
                                # counter2 += 0.1
                                # sleep( counter2 )

                            except KeyError:
                                print "*******"+str(r.status_code)+" KeyError*******"
                                # counter2 += 0.1
                                # sleep(counter2)
                                pass
                    with open(episodePath, 'w') as linksoutfile:
                        linksoutfile.write(linkFileString)
                except ValueError:
                    print "*******ERROR EPISODE******* "

        os.system("rm " + filename)
    except KeyError:
        print "*******ERROR*******"
    data_file.close()
with open(rootFolderName + "/" + folderName + "/data.json", 'w') as outfile:
    json.dump(data, outfile)

