FROM python:3.8

ENV WD /usr/src/reverse-arr

WORKDIR $WD

COPY . $WD

CMD python main.py
