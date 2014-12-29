# rsync -auI `find b*  -maxdepth 1 -type d` movies/b/ && rm -R `find b*  -maxdepth 1 -type d`

mkdir 0---final---/
for letter in {a..z} ; do
	mkdir 0---final---/$letter/
	rsync -auI `find $letter*  -maxdepth 1 -type d` 0---final---/$letter/
done