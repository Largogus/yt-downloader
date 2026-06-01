import requests


def check_proxy(proxy):
    try:
        r = requests.get(
            "http://httpbin.org/ip",
            proxies={
                "http": proxy,
            },
            timeout=5,
        )

        return r.status_code == 200

    except Exception:
        return False


def get_proxy():
    # url = "https://raw.githubusercontent.com/Largogus/yt-downloader/refs/heads/master/config.json"
    # _proxy = requests.get(url).json()

    _proxy = {'proxy': [
        "http://144.79.35.11:3125",
        "http://202.154.18.72:8084",
        "http://119.134.178.12:7890",
        "http://125.234.91.117:1080"
    ]}

    proxies = _proxy["proxy"]

    return next((proxy for proxy in proxies if check_proxy(proxy)), None)