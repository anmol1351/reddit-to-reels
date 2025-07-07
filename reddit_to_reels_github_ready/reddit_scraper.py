import praw

def fetch_top_posts(subreddit='wholesomememes', limit=5):
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                         client_secret='YOUR_CLIENT_SECRET',
                         user_agent='reddit_to_reels_bot')
    posts = reddit.subreddit(subreddit).top('day', limit=limit)
    results = []
    for post in posts:
        if not post.stickied and post.selftext:
            results.append({'title': post.title, 'body': post.selftext})
    return results