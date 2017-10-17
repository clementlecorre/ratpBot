FROM python:3-alpine
LABEL maintainer="clement@le-corre.eu"
ENV API_TOKEN=changeme
COPY ratpBot /ratpBot
WORKDIR /ratpBot
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["bot.py"]
