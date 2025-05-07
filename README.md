# Player Position Detector

This project detects and tracks player positions in video files using Python and OpenCV.  
It supports exporting player coordinates, visualizing movement paths, generating heatmaps, and creating annotated tracking videos.

## Features

- Detects moving players in football/soccer video footage.
- Marks and tracks players across frames with consistent IDs.
- Saves player positions to CSV for analysis.
- Plots player movement paths.
- Generates player heatmaps.
- Exports tracking video with overlay rectangles and IDs.
- Docker-ready for easy deployment.

## Technologies Used

- Python 3.13.0
- OpenCV
- Matplotlib
- Seaborn
- Docker

## How to Run

### 1. Install dependencies:

```bash
pip install -r requirements.txt
```
### 2. Place your input video:
Add an MP4 video named input.mp4 inside the videos directory.

### 3. Run player tracking:

```bash
python src/player_tracker.py
```

Outputs:
player_positions.csv
player_tracking_output.mp4

### 4. Plot player movement paths:

```bash
python src/plot_player_positions.py
```

Output:
player_movements.png

### 5. Generate player heatmap:

```bash
python src/plot_player_heatmap.py
```

Output:
player_heatmap.png

## Docker Usage

1. Build the Docker image:

```bash
docker build -t player-position-detector .
```

2. Run the container:

```bash
docker run --rm -it player-position-detector
```

## Project Structure

```bash
player-position-detector/
├── videos/
│   └── input.mp4
├── src/
│   ├── player_tracker.py
│   ├── plot_player_positions.py
│   └── plot_player_heatmap.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

## Author

Oleh Yakovliev