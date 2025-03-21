import time
import random

PROXY_ROTATION_INTERVAL = 10 * 60  # 10 minutos

class ProxyManager:
    def __init__(self, proxy_file="proxies.txt"):
        self.proxy_file = proxy_file
        self.last_rotation = 0
        self.proxies = self.load_proxies()
        self.current_proxy = random.choice(self.proxies)

    def load_proxies(self):
        with open(self.proxy_file, "r") as f:
            return [p.strip() for p in f.readlines() if p.strip()]

    def get_proxy(self):
        now = time.time()
        if now - self.last_rotation > PROXY_ROTATION_INTERVAL:
            self.current_proxy = random.choice(self.proxies)
            self.last_rotation = now
            print(f"[ProxyManager] Proxy rotated: {self.current_proxy}")
        return self.current_proxy
