from bs4 import BeautifulSoup
from puppeteer import launch
from puppeteer_cluster import Cluster
import proxy_chain
import user_agents

import Task from '../api/Tasks/model.py'
import Proxy from '../api/Proxies/model.py'
import Address from '../api/Addresses/model.py'

import { testProxy, createProxyString } from './proxies.py'
import sendEmail from './email.py'
import sendWebhookEvent from './webhook.py'
import Logger from './logger.py'
import { storePageInTaskCache } from './task-cache.py'

import sites from '../sites/index.py'

user_agent = user_agents.UserAgent()

puppeteer.use(Ua())

class PuppeteerCluster:
    @staticmethod
    async def build():
        proxies = await new Proxy().find({ has_been_used: False })
        valid_proxy = proxies.find(async (proxy) => {
            proxy_string = createProxyString(proxy)
            if await testProxy(proxy_string):
                await new Proxy(proxy.id).update({ has_been_used: True })
                return True
            return False
        })
        proxy = valid_proxy ? createProxyString(valid_proxy) : None
        new_proxy_url = None
        if proxy:
            new_proxy_url = await proxy_chain.anonymizeProxy(proxy)

        puppeteer_options = {
            "headless": False,
            "defaultViewport": None,
            "args": [
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-web-security",
                "--disable-features=IsolateOrigins,site-per-process",
                f"--user-agent={user_agent}",
            ],
        }
        if process.env.NODE_ENV == "docker":
            puppeteer_options["executablePath"] = "/usr/bin/google-chrome-stable"
        if new_proxy_url:
            puppeteer_options["args"].append(f"--proxy-server={new_proxy_url}")

        cluster = await Cluster.launch(
            {
                puppeteer,
                "concurrency": Cluster.CONCURRENCY_BROWSER,
                "maxConcurrency": int(process.env.PARALLEL_TASKS) or 1,
                "timeout": 5 * 60 * 1000,
                "puppeteerOptions": puppeteer_options,
            }
        )

        cluster.task(
