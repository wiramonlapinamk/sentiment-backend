FROM python:3.9-bullseye

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir --progress-bar off -r requirement.txt

EXPOSE 8080

CMD ["python","app.py"]