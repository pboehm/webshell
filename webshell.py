#!/usr/bin/python -u

from sys import stdout
from collections import OrderedDict

import subprocess

# The following dict defines the allowed commands which should be available
# through webshell. This is also a security feature as it only executes
# commands which are in this dict
ALLOWED_COMMANDS = OrderedDict([
   ["du -sch ~/Downloads/*",   "du -sch ~/Downloads/*"],
   ["du -sch ~/dirty/*",       "du -sch ~/dirty/*"],
   ["series",                  "~/bin/series"],
   ["tree ~/Queue/",           "tree -l ~/dlna/Queue*"],
   ["rm ~/Downloads/*",        "rm ~/Downloads/*"],
   ["killall junkie",          "killall junkie"],
   ["remove_watched_episodes", "~/projects/Scripts/remove_watched_episodes.sh"],
   ["restart minidlna", "sudo service minidlna restart"],
   ["tv on/off", "irsend SEND_ONCE lg KEY_POWER"],
   ["tv prog+", "irsend SEND_ONCE lg KEY_CHANNELUP"],
   ["tv prog-", "irsend SEND_ONCE lg KEY_CHANNELDOWN"],
   ["sound on/off", "irsend SEND_ONCE logitech POWER"],
   ["sound vol+", "irsend SEND_ONCE logitech VOL_PLUS"],
   ["sound vol-", "irsend SEND_ONCE logitech VOL_MINUS"],
])

# send the allowed commands to th shell
for cmd in ALLOWED_COMMANDS.keys():
    print "COMMAND###%s\n" % cmd
    stdout.flush()

while True:
    cmd = raw_input()

    if cmd in ALLOWED_COMMANDS:
        try:
            print subprocess.check_output(ALLOWED_COMMANDS[cmd], shell=True)
            print "[program exited]"
        except Exception, e:
            print "ERROR: %s" % e

        stdout.flush()
