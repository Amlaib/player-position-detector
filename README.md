# Player Position Detector

A Python-based player tracking system for football/soccer video analysis. Fully containerized using Docker.

## Features

- Detects and tracks moving players in football/soccer videos.
- Consistent object IDs across frames.
- CSV export of player positions.
- Plots player movement paths.
- Generates player position heatmaps.
- Exports annotated tracking video.
- Runs natively or in Docker containers.

## Technologies

- Python 3.12+
- OpenCV
- Matplotlib
- Seaborn
- Docker

## How to Run (Without Docker)

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Place your input video as `videos/input.mp4`.

3. Run player tracking:

    ```bash
    python src/player_tracker.py
    ```

4. Plot movement paths:

    ```bash
    python src/plot_player_positions.py
    ```

5. Generate heatmap:

    ```bash
    python src/plot_player_heatmap.py
    ```

## How to Run (With Docker)

1. Pull the image:

    ```bash
    docker pull amlaib/player-position-detector:latest
    ```

2. Run player tracking (replace `/path/to/local/folder` with your local folder):

    ```bash
    docker run --rm -it -v /path/to/local/folder:/app amlaib/player-position-detector:latest
    ```

3. Run plotting scripts inside the container:

    ```bash
    docker run --rm -it -v /path/to/local/folder:/app amlaib/player-position-detector:latest python src/plot_player_positions.py
    docker run --rm -it -v /path/to/local/folder:/app amlaib/player-position-detector:latest python src/plot_player_heatmap.py
    ```

## Project Structure

```bash
player-position-detector/
├── videos/
│ └── input.mp4
├── src/
│ ├── player_tracker.py
│ ├── plot_player_positions.py
│ └── plot_player_heatmap.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

## Author

Oleh Yakovliev