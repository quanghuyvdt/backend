FROM python:3.12-alpine
WORKDIR /app
COPY ./requirements.txt /app
RUN pip3 install --no-cache -r requirements.txt
COPY .  .
CMD ["python", "app.py"]