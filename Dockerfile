FROM debian
MAINTAINER cl3m3nt
RUN apt-get update
RUN apt-get -y install python3 wget python3-bs4
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py
RUN export LC_ALL='en_US.utf8'
COPY ratpBot /ratpBot
WORKDIR /ratpBot
RUN pip install -r requirements.txt
CMD ["bash", "runbot.sh"]
