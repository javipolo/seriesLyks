#!/bin/bash
#max 600
FOLDER="series"
TYPE=1
mkdir $FOLDER/

for i in {0..600}
do
	wget -O $FOLDER/page$i.txt --load-cookies cookie.txt http://series.ly/scripts/catalogue/index.php?page=$i\&mediaType=1
	sleep 1
done

rm $FOLDER/ids.txt
for i in $FOLDER/page*.txt
do
	grep -o -P "/series/serie-(\S+)\"" $i >> $FOLDER/ids.txt
	rm $i
done

while read idDirty          
do  
	echo "$idDirty" cut -d '-' -f2 $idDirty | cut -d '"' -f1 | cut -d '-' -f2 >> $FOLDER/idsFinal.txt     
done < $FOLDER/ids.txt

rm $FOLDER/ids.txt
mv $FOLDER/idsFinal.txt $FOLDER/ids.txt