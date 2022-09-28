FROM python:3.8-buster
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY app.py /app
EXPOSE 5000
ENV PYTHONPATH /app
ENTRYPOINT python app.py
