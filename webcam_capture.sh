/usr/bin/fswebcam -r 1280x720  -F 3  --jpeg 100 --deinterlace -d /dev/video0 -i 0 -D 3 /home/kayttaja/Kuvat/Webcam/$(date +%Y-%m-%d_%H-%M)_W1.jpg
/usr/bin/fswebcam -r 640x480   -F 3  --jpeg 100 --deinterlace -d /dev/video2 -i 0 -D 3 /home/kayttaja/Kuvat/Webcam1/$(date +%Y-%m-%d_%H-%M)_W2.jpg
/usr/bin/fswebcam -r 352x288   -F 3  --jpeg 100 --deinterlace -d /dev/video3 -i 0 -D 3 /home/kayttaja/Kuvat/Webcam2/$(date +%Y-%m-%d_%H-%M)_W3.jpg
/usr/bin/fswebcam -r 640x480   -F 3  --jpeg 100 --deinterlace -d /dev/video4 -i 0 -D 3 /home/kayttaja/Kuvat/Webcam3/$(date +%Y-%m-%d_%H-%M)_W4.jpg
/usr/bin/fswebcam -r 1920x1080 -F 3  --jpeg 100 --deinterlace -d /dev/video5 -i 0 -D 3 /home/kayttaja/Kuvat/Webcam4/$(date +%Y-%m-%d_%H-%M)_W5.jpg
