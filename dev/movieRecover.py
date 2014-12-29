
completed = open( "movies/completed.txt", "r" )
idsSet = set()
for line in completed:
	idsSet.add(line)

idsRaw = open("movies/ids.txt", "r")
for line in idsRaw:
	idsSet.add(line)

output = open( "movies/idsFinal.txt", "w")
for ids in idsSet:
	output.write(ids)