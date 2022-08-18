FROM python:3.10.6-alpine

WORKDIR /app

COPY ./requirements.txt /etc/requirements.txt
COPY app /app
COPY main.py /main.py

RUN pip install --no-cache-dir -r /etc/requirements.txt

ENV FLASK_APP=/main.py
ENV FLASK_ENV=development

CMD [ "python", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]