email=$1
password=$2
wget --load-cookies cookie.txt --save-cookies cookie.txt --post-data='lg_login=$email&lg_pass=$password&paso1ok=Entrar' http://series.ly/scripts/login/login.php

cookieName='PHPSESSID'
while read line           
do          
	set -- $line
  	echo "$6 -> $7"
  	if [ "PHPSESSID" == "$6" ] ; then cookie=$7; fi

done < cookie.txt  
rm login.php

echo "Cookie: $cookie"

# DONE
# bash docus.sh
# bash series.sh
# bash tv.sh
# bash movies.sh

# # The heavy part
# bash links.sh $cookie linksSeason.py 4 tvShows # DONE
# bash links.sh $cookie linksNoSeason.py 3 docus
bash links.sh $cookie linksSeason.py 1 series #GOING
# bash links.sh $cookie linksNoSeason.py 2 movies