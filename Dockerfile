FROM python:latest
WORKDIR /app
RUN pip install flask
RUN pip install flask_restful
RUN pip install requests
RUN pip install opencv-python
RUN apt-get install libpng-dev
RUN git clone https://github.com/shantnu/FaceDetect.git .

COPY . .
ENTRYPOINT [ "python3" ]
CMD ["main.py"]
