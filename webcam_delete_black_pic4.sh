#!/bin/bash
set -m

Delete_black_pictures()
{
	python3 /home/kayttaja/Lataukset/Git/Python_delete_Pictures/delete2.py $i;
	echo $i;
}
COUNTER=0

for z in /home/kayttaja/Kuvat/Webcam3/*.jpg
do
for x in /home/kayttaja/Kuvat/Webcam2/*.jpg
do
for c in /home/kayttaja/Kuvat/Webcam1/*.jpg
do
for v in /home/kayttaja/Kuvat/Webcam/*.jpg
do
#	while [ "$COUNTER" -lt "10" ]; 
#	do
	Delete_black_pictures $z 
        Delete_black_pictures $x 
        Delete_black_pictures $c 
        Delete_black_pictures $v 
	let COUNTER=COUNTER+1 
#	echo $z
#	echo $x
#	echo $c
#	echo $v
#	echo $COUNTER
	if [ "$COUNTER" -gt "10" ]; 
		then	echo "sleep 4"; sleep 4;
		let COUNTER=0
	fi
done
done
done
done
#for i in /home/kayttaja/Kuvat/Webcam3/*.jpg; do python3 /home/kayttaja/Lataukset/Git/Python_delete_Pictures/webcam_delete_prog_ver2.py "$i" ;done
#for i in /home/kayttaja/Kuvat/Webcam2/*.jpg; do python3 /home/kayttaja/Lataukset/Git/Python_delete_Pictures/webcam_delete_prog_ver2.py "$i" ;done 
#for i in /home/kayttaja/Kuvat/Webcam1/*.jpg; do python3 /home/kayttaja/Lataukset/Git/Python_delete_Pictures/webcam_delete_prog_ver2.py "$i" ;done
#for i in /home/kayttaja/Kuvat/Webcam/*.jpg;  do python3 /home/kayttaja/Lataukset/Git/Python_delete_Pictures/webcam_delete_prog_ver2.py "$i" ;done
