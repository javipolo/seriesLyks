#!/bin/bash
#max 500
FOLDER="docus"
TYPE=3
mkdir $FOLDER/

for i in {0..500}
do
	url=http://series.ly/scripts/catalogue/index.php\?page=$i\&mediaType=$TYPE
	wget -O $FOLDER/page$i.txt --load-cookies cookie.txt --header="X-Requested-With: XMLHttpRequest" --referer=$url $url
	sleep 0.1
done

rm $FOLDER/ids.txt
for i in $FOLDER/*.txt
do
	grep -o -P "/docus/docu-(\S+)\"" $i >> $FOLDER/ids.txt
	rm $i
done

while read idDirty          
do  
	echo "$idDirty" cut -d '-' -f2 $idDirty | cut -d '"' -f1 | cut -d '-' -f2 >> $FOLDER/idsFinal.txt     
done < $FOLDER/ids.txt

rm $FOLDER/ids.txt
mv $FOLDER/idsFinal.txt $FOLDER/ids.txt

