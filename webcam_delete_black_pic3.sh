#!/bin/bash
set -m

Delete_black_pictures()
{
	python3 /home/kayttaja/Lataukset/Git/Python_delete_Pictures/webcam_delete_prog_ver2.py $i;
	#echo $data;
}
COUNTER=0

for i in /home/kayttaja/Kuvat/Webcam3/*.jpg
do
#	while [ "$COUNTER" -lt "10" ]; 
#	do
	Delete_black_pictures $i &  
	let COUNTER=COUNTER+1 
	echo $i
#	echo $COUNTER
	if [ "$COUNTER" -gt "10" ]; 
		then	echo "sleep 10"; sleep 10;
		let COUNTER=0
	fi
done
	

COUNTER=0

for i in /home/kayttaja/Kuvat/Webcam2/*.jpg
do
#       while [ "$COUNTER" -lt "10" ]; 
#       do
        Delete_black_pictures $i &
        let COUNTER=COUNTER+1
        echo $i
#       echo $COUNTER
        if [ "$COUNTER" -gt "10" ];
                then    echo "sleep 10"; sleep 10;
                let COUNTER=0
        fi
done

COUNTER=0

for i in /home/kayttaja/Kuvat/Webcam1/*.jpg
do
#       while [ "$COUNTER" -lt "10" ]; 
#       do
        Delete_black_pictures $i &
        let COUNTER=COUNTER+1
        echo $i
#       echo $COUNTER
        if [ "$COUNTER" -gt "10" ];
                then    echo "sleep 10"; sleep 10;
                let COUNTER=0
        fi
done

COUNTER=0

for i in /home/kayttaja/Kuvat/Webcam/*.jpg
do
#       while [ "$COUNTER" -lt "10" ]; 
#       do
        Delete_black_pictures $i &
        let COUNTER=COUNTER+1
        echo $i
#       echo $COUNTER
        if [ "$COUNTER" -gt "10" ];
                then    echo "sleep 10"; sleep 10;
                let COUNTER=0
        fi
done

#for i in /home/kayttaja/Kuvat/Webcam3/*.jpg; do python3 /home/kayttaja/Lataukset/Git/Python_delete_Pictures/webcam_delete_prog_ver2.py "$i" ;done
#for i in /home/kayttaja/Kuvat/Webcam2/*.jpg; do python3 /home/kayttaja/Lataukset/Git/Python_delete_Pictures/webcam_delete_prog_ver2.py "$i" ;done 
#for i in /home/kayttaja/Kuvat/Webcam1/*.jpg; do python3 /home/kayttaja/Lataukset/Git/Python_delete_Pictures/webcam_delete_prog_ver2.py "$i" ;done
#for i in /home/kayttaja/Kuvat/Webcam/*.jpg;  do python3 /home/kayttaja/Lataukset/Git/Python_delete_Pictures/webcam_delete_prog_ver2.py "$i" ;done
