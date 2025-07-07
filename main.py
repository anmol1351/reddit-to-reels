from reddit_scraper import fetch_top_posts
from narrate import text_to_speech
from video_generator import create_video_with_audio_and_subtitle

def main():
    posts = fetch_top_posts()
    if not posts:
        print("No posts fetched.")
        return

    post = posts[0]
    text = f"{post['title']}. {post['body']}"
    audio_file = 'output.mp3'
    video_file = 'final_reel.mp4'

    print("Generating narration...")
    text_to_speech(text, audio_file)

    print("Creating video...")
    create_video_with_audio_and_subtitle(audio_file, text, video_file)

    print(f"Video created: {video_file}")

if __name__ == "__main__":
    main()