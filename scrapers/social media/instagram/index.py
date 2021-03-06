import multiprocessing
import os
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from worker import worker

the_queue = multiprocessing.JoinableQueue()

def worker_main(queue):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    browser = webdriver.PhantomJS('/usr/local/nvm/versions/node/v9.2.0/lib/node_modules/phantomjs-prebuilt/bin/phantomjs', desired_capabilities=dcap)
    while True:
        LINK = queue.get(True)
        worker(browser, LINK)
        queue.task_done()

the_pool = multiprocessing.Pool(10, worker_main, (the_queue,))

LINKS = [
  "https://www.instagram.com/explore/tags/logoembossedclutchbag",
  "https://www.instagram.com/explore/tags/studdedwaistbelt",
  "https://www.instagram.com/explore/tags/backpack",
  "https://www.instagram.com/explore/tags/continentalwallet",
  "https://www.instagram.com/explore/tags/continentalwallet",
  "https://www.instagram.com/explore/tags/embellishedturtleneck",
  "https://www.instagram.com/explore/tags/floralprintscarf",
  "https://www.instagram.com/explore/tags/printscarf",
  "https://www.instagram.com/explore/tags/clipcardholder",
  "https://www.instagram.com/explore/tags/shoulderbag"
]

for L in LINKS:
    the_queue.put(L)

the_queue.join()
