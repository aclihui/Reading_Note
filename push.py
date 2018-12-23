import subprocess
import datetime
i = datetime.datetime.now()
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "auto push at " + "%s-%s-%s" % (i.year, i.month, i.day)]) 
subprocess.call(["git", "push"])
