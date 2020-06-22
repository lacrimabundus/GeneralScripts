# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
This script is used to send messages to any NextcloudTalk chat.
It is recommended to use App Token.

"""

__author__ = "Maximilian Stefani"
__credits__ = ["Maximilian Stefani", "Sven Kielmann", "David Luhmer"]
__email__ = "maximilian.stefani@unibw.de"
__version__ = "1.0"
__date__ = "Jun 18 2020"
__license__ = "GPLv3"

import requests
import json
import argparse 

# Initialize parser 
parser = argparse.ArgumentParser() 

# Adding optional argument 
parser.add_argument( "-m", "--message", 
                    help = "Message in brackets to be sent", 
                    required=True) 
parser.add_argument( "-ID", "--channelId", 
                    help = "The chat-ID. You can find them at the end of the ULR of the chat.", 
                    required=True) 
parser.add_argument( "-u", "--username", 
                    help = "User who should send the message", 
                    required=True) 
parser.add_argument( "-p", "--password", 
                    help = "Password or app token", 
                    required=True) 
parser.add_argument( "-url", "--server", 
                    help = "The url of the nextcloud instance", 
                    required=True) 

  
# Read arguments from command line 
args = parser.parse_args() 

data = {
        "token": args.channelId,
        "message": args.message,
        "actorDisplayName": "PYTHON-NOTIFICATION",
        "actorType": "",
        "actorId": "",
        "timestamp": 0,
        "messageParameters": []
    }

url = "{}/ocs/v2.php/apps/spreed/api/v1/chat/{}".format(args.server, args.channelId)
    # print(url)
payload = json.dumps(data);

headers = {'content-type': 'application/json', 'OCS-APIRequest': 'true'}
resp = requests.post(url, data=payload, headers=headers, auth=(args.username, args.password))
print(resp)
# print(resp.text)
