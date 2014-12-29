while true;
do
	clear
	wc -l movies/ids.txt && find movies/*.json | wc -l && find movies/*.json -size -228c | wc -l && date "+%F %T"
	sleep 10
done