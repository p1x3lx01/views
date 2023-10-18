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

def run():
    # تحديث رأس User-Agent بشكل عشوائي مع كل زيارة
    headers = {
        "User-Agent": ua.random,
        "Referer": f"https://www.google.com/search?q={random.choice(['twitter', '@ahmed629231', '1714679426133201174'])}"
    }
    
    response = requests.get(site, headers=headers, proxies=proxies, verify=False)
    print("[" + str(i) + "]" + " Blog View Added With IP:" + requests.get('http://ipecho.net/plain', proxies=proxies, headers=headers).text)
    
    # انتظر فترة زمنية عشوائية بين 5 إلى 10 ثوانٍ بين الطلبات لجعلها تبدو أكثر واقعية
    time.sleep(random.uniform(5, 10))

if __name__ == '__main__':
    for i in range(blog):
        run()
