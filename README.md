# slack_api

```python
>>>from settings import COOKIES, HEADERS
>>>from slack_api import SlackApi
>>>user_token: str = 'YOUR TOKEN'
>>>user_id: str = "YOUR ID"
>>>company_url: str = 'YOURS COMPANY URL '

>>>slack_route: str = '<SLACK_ROUTE>'   # параметр из строки браузера https://app.slack.com/client/ <SLACK_ROUTE> /XXXXX
        
>>>channel: str = '<CHANNEL>'         # параметр из строки браузера https://app.slack.com/client/XXXXX/ <CHANNEL>

>>>api = SlackApi(user_token, user_id, company_url, cookies=COOKIES, headers=HEADERS)


>>>messages = api.get_messages_from_channel(slack_route, channel)

>>>messages
{
    'ok': True, 
    'latest': '1614326544.002583', 
    'oldest': '0000000000.000001', 
    'messages': [
        {
            'client_msg_id': 'e98fdac2-e48c-4222-becc-ffa9e06ab395', 
            'type': 'message', 
            'text': '^[[]{1}[0-9]{1}[]]{1}$', 
            'user': 'U01NW0EKVFT', 
            'ts': '1613990526.002800', 
            'team': 'T01NAHZ7170', 
            'blocks': [
                {
                    'type': 'rich_text', 
                    'block_id': 'K72', 
                    'elements': [
                        {
                            'type': 'rich_text_section',
                            'elements': [
                                {
                                    'type': 'text', 
                                    'text': '^[[]{1}[0-9]{1}[]]{1}$'
                                }
                            ]
                        }
                    ]
                }
            ], 
            'thread_ts': '1613990526.002800', 
            'reply_count': 1, 
            'reply_users_count': 1, 
            'latest_reply': '1614175423.000900', 
            'reply_users': ['U01NW0EKVFT'], 
            'subscribed': True, 
            'last_read': '1614175423.000900'
        },
        {
            'client_msg_id': '46518757-3cd1-41a4-9cf7-bd5c8890a8a1', 
            'type': 'message', 
            'text': 'У нас появилась новая задача на ревью:) ABC-12345: [Тема данной задачи - 0] Имя Фамилия (<mailto:mail@example.com>)', 
            'user': 'U01NW0EKVFT', 
            'ts': '1613990098.002600', 
            'team': 'T01NAHZ7170', 
            'blocks': [
                {
                    'type': 'rich_text', 
                    'block_id': '24YV4', 
                    'elements': [
                        {
                            'type': 'rich_text_section',
                            'elements': [
                                {
                                    'type': 'text', 
                                    'text': 'У нас появилась новая задача на ревью:) ABC-12345: [Тема данной задачи - 0] Имя Фамилия ('
                                }, 
                                {
                                    'type': 'link', 
                                    'url': 'mailto:mail@example.com', 
                                    'text': 'mail@example.com'
                                }, 
                                {
                                    'type': 'text', 
                                    'text': ')'
                                }
                            ]
                        }
                    ]
                }
            ], 
            'reactions': [
                {
                    'name': 'eyes', 
                    'users': ['U01NW0EKVFT'], 
                    'count': 1
                }, 
                {
                    'name': 'innocent', 
                    'users': ['U01NW0EKVFT'], 
                    'count': 1
                }, 
                {
                    'name': 'white_check_mark', 
                    'users': ['U01NW0EKVFT'], 
                    'count': 1
                }
            ]
        }
    ], 
    'has_more': False, 
    'pin_count': 0, 
    'channel_actions_ts': None, 
    'channel_actions_count': 0, 
    '_Result': True}

```