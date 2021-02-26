import typing as t
import json
import pathlib


__all__ = ['COOKIES', 'HEADERS']


def loads_cookies(filename: t.Union[pathlib.Path, str]) -> dict:
    with open(filename) as fp:
        cookies = json.load(fp)
    return cookies


def convert_cookie_for_requests(cookies: dict) -> dict:
    requests_cookies = dict()
    for cookie in cookies:
        requests_cookies[cookie['name']] = cookie['value']
    return requests_cookies


HEADERS: dict[str, str] = {
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.41 Safari/537.36'
}


COOKIES_JSON_PATH: t.Union[pathlib.Path, str] = 'Z:\\projects\\slack\\slack_cookies.json'

COOKIES: dict = convert_cookie_for_requests(loads_cookies(COOKIES_JSON_PATH))










