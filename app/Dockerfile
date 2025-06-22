# Base image
FROM python:3.14.0b3-alpine3.21

# Install security updates, curl, and gcc for building Python packages
RUN apk update && \
    apk add --no-cache gcc musl-dev curl

# Create a non-root user
RUN adduser -D -h /home/appuser appuser

# Set working directory
WORKDIR /app

# Copy all source code
COPY . .

# Set up Python virtual environment
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir -r requirements.txt

# Switch to non-root user
USER appuser

# Expose app port
EXPOSE 5050

# Health check to monitor the container’s status
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:5050/ || exit 1

# Run the Flask app
CMD ["python", "main.py"]