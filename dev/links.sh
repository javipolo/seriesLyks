#!/bin/bash
#max 4000
cookie=$1
pyScript=$2
TYPE=$3
FOLDER=$4
mkdir $FOLDER/

mediaType=5
if [ $TYPE -eq 2 ] ; then mediaType=$TYPE; fi
if [ $TYPE -eq 3 ] ; then mediaType=$TYPE; fi

while true;
do

	touch $FOLDER/completed.txt
	completedIds=`wc -l $FOLDER/completed.txt | cut -f1 -d' '`
	# echo $completedIds
	tail -n "+$completedIds" $FOLDER/ids.txt > $FOLDER/idsTemp.txt
	# rm $FOLDER/completed.txt
	rm $FOLDER/ids.txt
	mv $FOLDER/idsTemp.txt $FOLDER/ids.txt

	find $FOLDER/*.json -size -228c | cut -d '/' -f2 | cut -d '.' -f1 >> $FOLDER/ids.txt 

	while read id           
	do          
		wget -O $FOLDER/$id.json --load-cookies cookie.txt -nv http://series.ly/scripts/media/mediaInfo.php?mediaType=$TYPE\&id_media=$id
		echo $id >> $FOLDER/completed.txt
	done < $FOLDER/ids.txt  

	failed=`find $FOLDER/*.json -size -228c | wc -l| cut -f1 -d' '`
	echo "failed $failed"
	if [ "$failed" -eq 0 ]
	then
		break
	fi
done

for i in $FOLDER/*.json
do
	python $pyScript $i $1 $mediaType
done