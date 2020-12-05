from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine():
    def __init__(self):
        self.machine = GraphMachine(
            model=self, 
            **{
                "states":["user", "state1", "state2"],
                "transitions":[
                    {
                        "trigger": "advance",
                        "source": "user",
                        "dest": "state1",
                        "conditions": "is_going_to_state1",
                    },
                    {
                        "trigger": "advance",
                        "source": "state1",
                        "dest": "state2",
                        "conditions": "is_going_to_state2",
                    },
                    {"trigger": "go_back", "source": "state2", "dest": "user"},
                ],
                "initial":"user",
                "auto_transitions":False,
                "show_conditions":True,
            }
        )

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")

    def on_exit_state1(self, event):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back(event)

    def on_exit_state2(self, event):
        print("Leaving state2")