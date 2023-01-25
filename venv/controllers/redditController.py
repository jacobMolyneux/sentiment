import praw

reddit = praw.Reddit(
    client_id="KU76U36XnTO059URKYzzvw",
    client_secret="NTaia7Qa6ibQPW7c8JB3mYjrZaanuA",
    user_agent="my user agent by u/equivalent-prior-778",
)

subreddit = reddit.subreddit('wallstreetbets')
for submission in subreddit.hot(limit=5):
    print(submission.title)
    print('------------------------------------------')
    print(submission.comments.list())
    print('')
