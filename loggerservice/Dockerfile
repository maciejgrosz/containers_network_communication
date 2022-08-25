# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY . .
RUN pip3 install -r requirements.txt

# ENTRYPOINT ["/bin/bash"]
CMD [ "python3", "-m" , "flask", "--app", "loggerservice.py", "run", "--host=0.0.0.0"]
