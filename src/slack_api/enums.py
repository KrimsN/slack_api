from enum import Enum


class Emoji(str, Enum):
    white_check_mark = 'white_check_mark'   # ✅
    eyes = 'eyes'                           # 👀
    raised_hands = 'raised_hands'           # 🙌
    dart = 'dart'                           # 🎯


class ReactionAction(str, Enum):
    Add = 'add'
    Remove = 'remove'


class ConversationAction(str, Enum):
    MessageHistory = 'history'
    RepliesHistory = 'replies'