FROM python:3.7

WORKDIR /src
ADD . /src

RUN pip install -r requirements.txt

CMD [ "python3", "-u", "bitfinex.py" ]
