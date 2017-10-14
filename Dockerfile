FROM python
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/study-hard
WORKDIR /opt/study-hard

ADD requirements.txt /opt/study-hard
RUN pip install -r requirements.txt
COPY . /opt/study-hard

EXPOSE 80
