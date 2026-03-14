FROM python:3.12-bullseye

WORKDIR /g8bot

COPY . /g8bot

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]