import praw
from praw.models import MoreComments
reddit = praw.Reddit(
    client_id="KU76U36XnTO059URKYzzvw",
    client_secret="NTaia7Qa6ibQPW7c8JB3mYjrZaanuA",
    user_agent="my user agent by u/equivalent-prior-778",
)

comment_list = []

subreddit = reddit.subreddit('wallstreetbets')
# for submission in subreddit.hot(limit=5):
#     print(submission.title)
#     print('------------------------------------------')
#     print(submission.comments.list())
#     print('')

def get_post_id():
    titles = []
    subreddit = reddit.subreddit('wallstreetbets')
    for submission in subreddit.hot(limit=5):
        titles.append([submission.title, submission.id])
    return(titles)

data = get_post_id()

submission = reddit.submission(data[0][1])

comment_list = []

for comment in submission.comments:
    if isinstance(comment, MoreComments):
        continue
    comment_list.append(comment.body)


print(comment_list)