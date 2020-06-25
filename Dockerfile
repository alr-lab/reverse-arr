FROM python:3.8

ENV WD /usr/src/reverse-arr

WORKDIR $WD

COPY . $WD

RUN pip install pytest

CMD python main.py
