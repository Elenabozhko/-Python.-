import hashlib
import uuid

salt = uuid.uuid4().hex
cache_obj = {}


def get_page(url):
    if cache_obj.get(url):
        print(f'адрес: {url} присутствует в хеше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = res
        print(cache_obj)


get_page('gb.ru')
get_page('gb.ru')
get_page('gb.ru')
get_page('gb.ru')