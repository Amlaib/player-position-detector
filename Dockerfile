# Use official Python image
FROM python:3.12

# Install libGL for OpenCV support
RUN apt-get update && apt-get install -y libgl1-mesa-glx

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