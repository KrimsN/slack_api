import typing as t
from enum import Enum
from functools import partial


__all__ = ['ApiAction', 'Emoji']


def _action(value: str, group: t.Optional[str] = None, separator: t.Optional[str] = '.'):
    if group is None:
        separator = ''
        group = ''
    return "{grp}{sep}{val}".format(grp=group, sep=separator, val=value)


action = partial(partial, _action)


class AbstractAction(str, Enum):
    pass


class ApiAction:
    """
    Класс - обёртка для классов с типами запросов
    """
    class ReactionAction(AbstractAction):
        _reaction = action(group='reactions')

        Add = _reaction('add')
        Remove = _reaction('remove')

    class ConversationAction(AbstractAction):
        _conversation = action(group='conversations')

        MessageHistory = _conversation('history')
        RepliesHistory = _conversation('replies')


class Emoji(str, Enum):
    """
    Класс с значениями типов Emoji
    """
    white_check_mark = 'white_check_mark'   # ✅
    eyes = 'eyes'                           # 👀
    raised_hands = 'raised_hands'           # 🙌
    dart = 'dart'                           # 🎯
