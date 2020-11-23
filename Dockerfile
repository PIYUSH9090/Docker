FROM python:3.6
COPY . /app
WORKDIR /app
RUN apt update -y
RUN pip3 install -r requirements.txt
RUN apt install -y libgl1-mesa-glx
RUN pip3 install imageai --upgrade
ENTRYPOINT ["python"]
CMD ["FirstDetection.py"]
CMD ["sleep","3000"]