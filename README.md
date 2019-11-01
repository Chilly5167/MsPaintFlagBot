# MSPaintFlagBot
#### Reddit bot that keeps track of the number of posts in r/mspaintflags and comments that number on each new post.

The reddit account for the bot is u/thelegend3l

It used to be hosted on [pythonanywhere.com](https://www.pythonanywhere.com "pythonanywhere.com") and was set to run once daily.

Now it is automated with crontab to run once an hour on a raspberry pi zero W.

When it runs it checks the 5 newest posts in the subreddit and if any of the posts have not been saved then it comments the current post number.

It uses the accounts saved posts to keep track of posts that it has commented on.

It has a post dedicated to keeping track of the current post number in r/mspaintflags.

Each time it comments on a post it also comments on its own post with the next number it will use the next time it runs.

This means that the bot doesnt have to rely on saved files to keep track and instead uses reddit to store information.

This is my first bot and it has been a pretty cool learning experience.