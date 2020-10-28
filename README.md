1) All the file you have to put in the 1 folder 
    1 - Dockerfile
    2 - FirstDetection.py 
    3 - image1.jpeg
    4 - README.md
    5 - requirements.txt
    6 - resnet50_coco_best_v2.0.1.h5 (you were familiar with that file beacause you were done this program without    docker )

2) Then you have to build the image for your container with this command(location of terminal is that folder which contain all this 6 files) .. $ sudo docker build -t objectdetection(imagename) . 


3) It will take some time(keep patient), After complete the process you have to make container and login to the container with only 1 command  which is .. $ sudo docker run -it --entrypoint=/bin/bash objectdetection(imagename)

4) Then it will take you into the container so you will see like that .. root@(container id):/app# 

5) You have to give command for look what is in the container now so you use this command .. #ls 
so  you will that all the 6 files which is in your folder.

6) Then you have to run your program there ,so you will run the program like this .. #python FirstDetection.py


7) So it will give output in the container so you can see that with this command .. #ls

8) You will see that image1A.jpeg was added in that files list which is 7th file.   
 
