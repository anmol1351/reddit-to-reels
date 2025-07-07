# Reddit to Reels

An automated tool that converts top posts from Reddit into short video reels using AI voice and gameplay backgrounds.

## Features
- Pulls top daily posts from `r/WholesomeMemes`
- Converts them to voice using Google TTS
- Generates video with background gameplay and subtitles

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` in `reddit_scraper.py` with your Reddit API credentials.

### 3. Add a real `gameplay_loop.mp4` in the `assets/` folder.

### 4. Run the project
```bash
python main.py
```

### Output
Final video will be saved as `final_reel.mp4`.

## Deployment
You can deploy this to Render or any cloud provider that supports Python with scheduled jobs.