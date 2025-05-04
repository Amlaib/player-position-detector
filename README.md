# Player Position Detector

This project detects and tracks player positions in video files using Python and OpenCV.

## Features

- Detects moving objects (players) in video.
- Marks players and displays their coordinates.
- Supports different video inputs.
- Includes Docker container for easy deployment.

## Technologies Used

- Python 3.13.0
- OpenCV
- Docker
- Git & GitHub

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the script:

```bash
python src/player_tracker.py
```

## Docker Usage

1. Build the Docker image:

```bash
docker build -t player-position-detector .
```

2. Run the container:

```bash
docker run --rm -it player-position-detector
```

## Author

Oleh Yakovliev