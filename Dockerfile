# Use official Python image
FROM python:3.13

# Set working directory inside container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create videos folder if not present
RUN mkdir -p videos

# Default command (user can override this)
CMD ["python", "src/player_tracker.py"]