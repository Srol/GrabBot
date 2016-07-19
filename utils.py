from slacker import Slacker
import youtube_dl
import sys
import os

slack = Slacker("insert Slack API token here")

class MyLogger(object):
	def debug(self, msg):
		print msg

	def warning(self, msg):
		print msg

	def error(self, msg):
		print msg

def my_hook(d):
	if d['status'] == 'finished':
		print "Done downloading, now converting ..."

def grab_video(url, channel, userName):
	ydl_opts = {'logger': MyLogger(),'progress_hooks': [my_hook],'outtmpl': "%(id)s.%(ext)s"}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		videoInfo = ydl.extract_info(url, download=False)
		fileName = videoInfo['id']# + "." + videoInfo['ext']
		print fileName
		ydl.download([url])
		slack.chat.post_message(channel, "@" + userName + " requested the following file be downloaded.")
		prefixed = [plusExt for plusExt in os.listdir('.') if plusExt.startswith(fileName)]
		slack.files.upload(prefixed[0], channels=channel)