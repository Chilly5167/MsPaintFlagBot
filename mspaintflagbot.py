#! python3
# mspaintflagbot.py - Reddit bot that keeps track of the number of posts
# in r/mspaintflags and comments that number on each new post.
# the account is thelegend3l


import praw
import time


# Create the Reddit instance.
reddit = praw.Reddit('MSPaintFlagBot')


# Assign the variable myself as the bots own account.
myself = reddit.redditor('thelegend3l')


# Iterates through the bots posts and saves them in my_post.
# The bot always only has one post.
for posts in myself.submissions.new():
    my_post = posts


# The post numbers are stored in comments in the bots orignal post,
# so it reads the latest comment and stores the number as an integer.
post_number = my_post.comments[-1].body
post_number = int(post_number)


# Accesses the subreddit r/mspaintflags
subreddit = reddit.subreddit('mspaintflags')


# Gets the 5 newest posts in r/mspaintflags and stores each one in posts
# It is inserted at the beggining to ensure that oldest posts are
# used first.
posts = []
for post in subreddit.new(limit=5):
    posts.insert(0, post)


# For each of the 5 posts this code runs.
# BTW I used submission instead of post so it is easier to distinguish.
for submission in posts:
    print(submission.title)

    # A loop that trys to comment and if it cant because of a ratelimit
    # error it will wait until it can try again until it has commented
    result = None
    while result is None:
    
        # The posts that the bot has already replied to are saved to the bot's
        # account. If the submission has not been saved...
        if submission.id not in myself.saved():
            
            # Replies to the current post using the post number
            try:
                submission.reply('Post number {} in r/mspaintflags'.format(post_number))
                print("Bot replying to : {} using number {}".format(submission.title, post_number))

                # Saves the current submission to the bot's account
                submission.save()
                print('{} has been saved.'.format(submission.title))

                # Updates the post number and replies to the bots post that keeps
                # track of post numbers
                post_number += 1
                my_post.reply('{}'.format(post_number))

                result = submission.title
                
            # If the ratelimit has been exceded
            except praw.exceptions.APIException as error:
                print('There was an error with the bot: {}'.format(error))
                error = list(str(error))
                # checks for the number in the error message
                # which tells the program how many minutes to wait
                for item in error:
                    if item.isdecimal():
                        minutes = int(item)
                seconds = minutes * 60
                more_seconds = seconds + 60
                # Waits how long is reccommended from the error + 1 minute to be safe
                print('The bot should wait {} minutes which is {} seconds but this bot '
                      'will wait for {} seconds'.format(minutes, seconds, more_seconds))
                # Looping alows you to keyboard interupt the program
                for second in range(more_seconds):
                    time.sleep(1)
        else:
            result = submission.title
