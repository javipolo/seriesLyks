#!/bin/bash
#max 4000
FOLDER="movies"
TYPE=2
mkdir $FOLDER/

for i in {1200..3700}
do
	wget -O $FOLDER/page$i.txt --load-cookies cookie.txt --tries=10 http://series.ly/scripts/catalogue/index.php?page=$i\&mediaType=2
done

rm $FOLDER/ids.txt
for i in $FOLDER/page*.txt
do
	grep -o -P "/pelis/peli-(\S+)\"" $i >> $FOLDER/ids.txt
	rm $i
done

while read idDirty          
do  
	echo "$idDirty" cut -d '-' -f2 $idDirty | cut -d '"' -f1 | cut -d '-' -f2 >> $FOLDER/idsFinal.txt     
done < $FOLDER/ids.txt

rm $FOLDER/ids.txt
mv $FOLDER/idsFinal.txt $FOLDER/ids.txt

