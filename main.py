import requests
import time
from fake_useragent import UserAgent
import random

ua = UserAgent()

proxies = {
    "http": "http://127.0.0.1:3128",
    "https": "https://127.0.0.1:3128"
}

print("""
... (البقية من الكود)
""")

site = input("Enter your Blog Address: ")
blog = int(input("Enter The number of Viewers: "))

search_engines = ['https://www.google.com/', 'https://www.bing.com/', 'https://search.yahoo.com/']  # قائمة بمحركات البحث

def run():
    search_engine = random.choice(search_engines)
    
    # تحديث رأس User-Agent و Referer بشكل عشوائي مع كل زيارة
    headers = {
        "User-Agent": ua.random,
        "Referer": search_engine
    }
    
    response = requests.get(site, headers=headers, proxies=proxies, verify=False)
    print("[" + str(i) + "]" + " Blog View Added With IP:" + requests.get('http://ipecho.net/plain', proxies=proxies, headers=headers).text)
    
    # انتظر فترة زمنية عشوائية بين 5 إلى 20 ثانية بين الطلبات لجعلها تبدو أكثر واقعية
    time.sleep(random.uniform(5, 20))

if __name__ == '__main__':
    for i in range(blog):
        run()
