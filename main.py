from lib.gen_func import parse_command
from slackclient import SlackClient
import os, json

class UtilBot:
    
    def MainLoop(self):
        slack_token = os.environ["SLACK_BOT_TOKEN"]
        sc = SlackClient(slack_token)
        
        if sc.rtm_connect(with_team_state=False):
            
            # Check if bot is running
            print ("On")
            
            while True:
                incoming_stream = sc.rtm_read()
                if incoming_stream:
                    incoming_json = json.dumps(incoming_stream[0])
                    incoming_json = json.loads(incoming_json)
                    
                    # If the incoming json type is a message parse the text and check it for commands.
                    if incoming_json["type"] == "message":
                        outgoing_message = parse_command(incoming_json["text"])
                        
                        if outgoing_message is not None:
                            sc.api_call(
                                "chat.postMessage",
                                channel=incoming_json["channel"],
                                text="Hostname is " + outgoing_message
                            )
                            
        else:
            print ("Connection Failed")
            
