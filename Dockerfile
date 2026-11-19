# Base Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY req.txt .

# Install dependencies
RUN pip install --no-cache-dir -r req.txt

# Copy application files
COPY app.py .
COPY ["Frontend – templates/", "./templates/"]
COPY ["CSS – static/", "./static/"]

# Create a non-root user
RUN useradd --create-home appuser && \
    chown -R appuser:appuser /app

USER appuser

# Application port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/health', timeout=3)" || exit 1

# Start Flask application
CMD ["python", "app.py"]
