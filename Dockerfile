FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app/ ./app/

# Create data directory
RUN mkdir -p data

# Environment variables (override in production)
ENV PYTHONPATH=/app
ENV APP_ENV=production

CMD ["python", "-m", "app.main"]
