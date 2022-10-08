# dockerfile for fastapi enpoint
FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
COPY /data /app/data
COPY /helpers /app/helpers
COPY /src /app/src
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]



