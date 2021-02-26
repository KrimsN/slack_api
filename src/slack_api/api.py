#
#
#

import typing as t
import requests
import time
import json


from .enums import (
    Emoji,
    ApiAction
)


def get_timestamp():
    """
    Получить timestamp В формате необходимому для slack
    """
    timestamp = time.time()
    return "{timestamp:.6f}".format(timestamp=timestamp)


class SlackApi:

    _URL_QUERY_T = '?_x_id={_x_id}&_x_csid={_x_csid}&slack_route={slack_route}&_x_version_ts={_x_version_ts}&_x_gantry={_x_gantry}'
    _URL_T = "https://{company_url}/api/{action}" + _URL_QUERY_T

    def __init__(self, user_token: str, user_id: str, company_url: str, cookies: dict, headers: dict):
        self._user_token = user_token
        self._user_id = user_id
        self._company_url = company_url
        self._cookies = cookies
        self._headers = headers

        self.default_url_params = {
            'company_url': self._company_url,
            '_x_csid': 'AloezodcEjs',
            '_x_version_ts': '1614137584',
            '_x_gantry': 'true'
        }

    def reactions(
            self,
            action_type: t.Union[ApiAction.ReactionAction, str],
            slack_route: str,
            channel: str,
            message_id: str,
            emoji: t.Union[Emoji, str],
            *,
            url_params: t.Optional[dict] = None,
            data_params: t.Optional[dict] = None
    ) -> dict:
        """
        Отправка запроса к api на установку emoji reaction


        :param action_type: Тип реакции (add/remove)
        :param slack_route: параметр из строки браузера https://app.slack.com/client/ <SLACK_ROUTE> /XXXXX
        :param channel: параметр из строки браузера https://app.slack.com/client/XXXXX/ <CHANNEL>
        :param message_id: идентификатор сообщения, представлен в виде строки timestamp(дата отправки сообщения)
        :param emoji: emoji которым нужно отреагировать на сообщение (в виде строки или Emoji(enum))
        :param url_params: параметры url, которые можно передать в случае сбоя работы параметров по умолчанию
        :param data_params: параметры data, которые можно передать в случае сбоя работы параметров по умолчанию

        :return : JSON ответ сервера (_Result == True) | словарь с ответом сервера (_Result == True, resp -> requests.Response)
        """

        if url_params is None:
            url_params = dict()
        if data_params is None:
            data_params = dict()
        if isinstance(emoji, Emoji):
            emoji = emoji.value
        if isinstance(action_type, ApiAction.ReactionAction):
            action_type = action_type.value

        default_reactions_url_params = {
            'company_url': self._company_url,
            'action': action_type,
            '_x_id': "{user_code}-{timestamp}".format(user_code=self._user_id, timestamp=get_timestamp()),
            'slack_route': slack_route,
        } | self.default_url_params

        default_reactions_data_params = {
            'timestamp': message_id,  # MSG ID
            'channel': channel,  # CHANNEL ID
            'name': emoji,  # EMOJI NAME
            'token': self._user_token,  # USER TOKEN
            '_x_mode': 'online',
            '_x_sonic': 'true',
            '_x_reason': 'changeReactionFromUserAction'
        }

        url_params = default_reactions_url_params | url_params
        data_params = default_reactions_data_params | data_params

        request_url = self._URL_T.format(**url_params)

        reactions_add_response = self._request_json(request_url, data_params)
        return reactions_add_response

    def get_messages_from_channel(
            self,
            slack_route: str,
            channel: str,
            limit: t.Optional[int] = 100,
            *,
            url_params: t.Optional[dict] = None,
            data_params: t.Optional[dict] = None
    ) -> dict:
        """
        Отправка запроса к api на получение сообщений из канала

        :param slack_route: параметр из строки браузера https://app.slack.com/client/ <SLACK_ROUTE> /XXXXX
        :param channel: параметр из строки браузера https://app.slack.com/client/XXXXX/ <CHANNEL>
        :param limit: максимальное количество сообщений из канала
        :param url_params: параметры url, которые можно передать в случае сбоя работы параметров по умолчанию
        :param data_params: параметры data, которые можно передать в случае сбоя работы параметров по умолчанию

        :return : JSON ответ сервера (_Result == True) | словарь с ответом сервера (_Result == True, resp -> requests.Response)
        """
        if url_params is None:
            url_params = dict()
        if data_params is None:
            data_params = dict()

        default_conversations_history_url_params = {
            'company_url': self._company_url,
            'action': ApiAction.ConversationAction.MessageHistory,
            '_x_id': "{user_code}-{timestamp}".format(user_code=self._user_id, timestamp=get_timestamp()),
            'slack_route': slack_route,
        } | self.default_url_params

        default_conversations_history_data_params = {
            'channel': channel,
            'limit': str(limit),
            'ignore_replies': 'false',
            'include_pin_count': 'false',
            'inclusive': 'true',
            'no_user_profile': 'true',
            'oldest': '0000000000.000001',
            'latest': get_timestamp(),
            'token': self._user_token,
            '_x_reason': 'channel-history-store.CFM.fetch',
            '_x_mode': 'online',
            '_x_sonic': 'true'
        }

        url_params = default_conversations_history_url_params | url_params
        data_params = default_conversations_history_data_params | data_params

        request_url = self._URL_T.format(**url_params)

        messages_info = self._request_json(request_url, data_params)
        return messages_info

    def get_message_replies(
            self,
            slack_route: str,
            channel: str,
            message_id: str,
            limit: t.Optional[int] = 100,
            *,
            url_params: t.Optional[dict] = None,
            data_params: t.Optional[dict] = None
    ) -> dict:
        """

        :param slack_route: параметр из строки браузера https://app.slack.com/client/ <SLACK_ROUTE> /XXXXX
        :param channel: параметр из строки браузера https://app.slack.com/client/XXXXX/ <CHANNEL>
        :param message_id: идентификатор сообщения, представлен в виде строки timestamp(дата отправки сообщения)
        :param limit: максимальное количество сообщений из треде
        :param url_params: параметры url, которые можно передать в случае сбоя работы параметров по умолчанию
        :param data_params: параметры data, которые можно передать в случае сбоя работы параметров по умолчанию

        :return : JSON ответ сервера (_Result == True) | словарь с ответом сервера (_Result == True, resp -> requests.Response)
        """
        if url_params is None:
            url_params = dict()
        if data_params is None:
            data_params = dict()

        default_conversations_history_url_params = {
            'action': ApiAction.ConversationAction.RepliesHistory,
            '_x_id': "{user_code}-{timestamp}".format(user_code=self._user_id, timestamp=get_timestamp()),
            'slack_route': slack_route
        } | self.default_url_params

        default_conversations_history_data_params = {
            'channel': channel,
            'ts': message_id,  # MSG ID
            'inclusive': 'true',
            'limit': str(limit),
            'oldest': '0000000000.000001',
            'token': self._user_token,
            '_x_reason': 'history-api/fetchReplies',
            '_x_mode': 'online',
            '_x_sonic': 'true'
        }

        url_params = default_conversations_history_url_params | url_params
        data_params = default_conversations_history_data_params | data_params

        request_url = self._URL_T.format(**url_params)

        replies = self._request_json(request_url, data_params)
        return replies

    def _request_json(self, request_url: str, data: dict[str, str]) -> dict:

        resp = requests.post(request_url, headers=self._headers, data=data, cookies=self._cookies)
        if resp.status_code == 200:
            result_json = json.loads(resp.text)
            result_json['_Result'] = True
            return result_json
        else:
            return {'_Result': False, 'resp': resp}
