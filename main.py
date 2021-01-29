import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = input('Enter project name\n')
HOMEPAGE = input('Enter home page\n')
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '\queue.txt'
CRAWLED_FILE = PROJECT_NAME + '\crawled.txt'
NUMBER_OF_THREADS = input('Enter no of threads ... for now enter 4\n')

queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

# create worker threads (will die when main exits)
def create_workers():
    for _ in range(int(NUMBER_OF_THREADS)):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# to next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

# each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# check if items on to do list ie. queue and crawl
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

create_workers()
crawl()