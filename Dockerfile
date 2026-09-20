FROM python:3.12.3

WORKDIR /app

# Install system dependencies: ffmpeg, aria2c for video downloading
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    aria2 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install yt-dlp
RUN pip install --no-cache-dir yt-dlp

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run via the supervisor -- keeps both the web health-check server and
# the bot running, and forwards shutdown signals cleanly to both.
CMD ["python3", "run.py"]
