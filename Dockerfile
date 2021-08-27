# FROM ubuntu:16.04
# # RUN apt-get update &&  apt-get upgrade -y
# # RUN apt-get install python3
# # RUN python -m pip install --upgrade pip
# RUN apt-get update -y
# RUN apt-get install -y python 
# RUN apt-get install -y python-pip python-dev

FROM python:latest
RUN apt-get update -y && apt-get install -y build-essential


COPY requirements.txt /app/back/requirements.txt
COPY run.py /app/run.py
COPY ./back /app/back
WORKDIR /app/back
RUN pip install -r requirements.txt 


# EXPOSE 5000
WORKDIR /app
# ENTRYPOINT [ "python" ]

# CMD [ "run.py" ]
CMD [ "gunicorn", "--bind=0.0.0.0", "back:app" ]