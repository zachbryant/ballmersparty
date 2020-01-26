import enum


class ActionTypes:
    DISCONNECTED = "disconnected"
    SUBMIT_ANSWER = "submit_answer"
    READY = "ready"
    KICK_PLAYER = "kick"
    START_GAME = "start"


class Action:
    def __init__(self, action_type, action_data):
        self.type_ = action_type
        self.data = action_data

    @classmethod
    def from_dict(cls, dictionary):
        if "type" not in dictionary:
            return None

        if dictionary["type"] in (
            ActionTypes.SUBMIT_ANSWER,
            ActionTypes.READY,
            ActionTypes.KICK_PLAYER,
            ActionTypes.START_GAME,
        ):
            return cls(dictionary["type"], dictionary.get("data"))

    @classmethod
    def get_disconnect_action(cls):
        return Action(ActionTypes.DISCONNECTED, None)

