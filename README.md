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
        }
    ], 
    'has_more': False, 
    'pin_count': 0, 
    'channel_actions_ts': None, 
    'channel_actions_count': 0, 
    '_Result': True}

```