# grabbot

This is a simple slackbot that creates an interface to run [youtube-dl](https://rg3.github.io/youtube-dl/) in Slack like it was a command line program. My co-workers don't have admin access to install and use youtube-dl on their computers, so I created this as a work-around.

To get this up-and-running you need to do the following things.

1. Clone the repository to your local computer.
2. Using the Heroku CLI tools, create a new app in the directory of the repository and note the url of where it's hosted.
3. Use your Slack account to create a new outgoing webhook using the URL from before (adding "/request" to the end). The default trigger phrase is 'grabbot download' but you can set this to whatever you want.
4. Also create a new bot user and note the API token for that user.
5. Update line 12 of grabbot.py with the key from your new webhook.
6. Update line 6 of utils.py with the bot user token.
7. Commit those changes and push the resulting files to Heroku.
8. Activate the redis-to-go add-on for the Heroku app you created. 
9. That's it more-or-less

Afterwards, anyone should be able to say `grabbot download <url>` in a public channel and the bot will download any URL supported by Youtube-DL and upload it to the Slack channel where the request was made. 

Keep in mind that as youtube-dl is updated, so too will this bot need to be. If you're using Heroku like me, all that means is changing the version number in requirements.txt

Additionally, using a [Heroku buildpack that supports for ffmpeg](https://github.com/shunjikonishi/heroku-buildpack-ffmpeg) will make your life easier, but it is not required.