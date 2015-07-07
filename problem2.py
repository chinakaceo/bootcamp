import webbrowser
import time

def runbrowser(timer, holdlist):
	holdtime=0
	for x in holdlist:
		holdtime += timer
		webbrowser.open(x)
		time.sleep(holdtime)

runbrowser(10, ["andela.com", "google.com", "yahoo.com"])