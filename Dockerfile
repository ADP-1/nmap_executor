FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install nmap
RUN apt-get update && apt-get install -y nmap && apt-get clean

COPY . .

ENV PORT 5000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:${PORT}", "--workers", "4"]
