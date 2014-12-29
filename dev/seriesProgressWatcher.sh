while true;
do
	clear
	find series/*.json |  wc -l && date "+%F %T" &&
	find series/ -type d -maxdepth 1 | wc -l &&
	sleep 60
done