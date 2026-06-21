FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY script.py .


EXPOSE 8000


CMD ["python", "script.py"]