from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine():
    def __init__(self):
        self.machine = GraphMachine(
            model=self, 
            **{
                "states":["start","user", "state1", "state2"],
                "transitions":[
                    {
                        "trigger": "advance",
                        "source": "start",
                        "dest": "user",
                        "conditions": "is_going_to_user",
                    },
                    {
                        "trigger": "advance",
                        "source": "user",
                        "dest": "state1",
                        "conditions": "is_going_to_state1",
                    },
                    {
                        "trigger": "advance",
                        "source": "user",
                        "dest": "state2",
                        "conditions": "is_going_to_state2",
                    },
                    {"trigger": "go_back", "source": ["state1", "state2"], "dest": "start"},
                ],
                "initial":"start",
                "auto_transitions":False,
                "show_conditions":True,
            }
        )

    def is_going_to_user(self, event):
        text = event.message.text
        return text.lower() == "go to user"
    
    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_user(self, event):
        print("I'm entering user")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger user")
        self.go_back()

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
