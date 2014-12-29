import json
import sys

filename = sys.argv[1]
with open(filename) as data_file:
    data = json.load(data_file)

i = 0
for season in data['episodes']:
    # print data['episodes'][str(i)]
    for episode in data['episodes'][str(i)]:
        print "http://series.ly/scripts/media/epLinks.php?mediaType=5&idc="+ str(episode['idc'])
    i+=1