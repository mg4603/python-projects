import notify2
import time
from top_stories import topstories

news_items = topstories()

notify2.init("News Notifier")
n = notify2.Notification(None)

n.set_urgency(notify2.URGENCY_NORMAL)

n.set_timeout(10000)

for newsitem in news_items:
    n.update(newsitem['title'],  newsitem['description'])
    n.show()
    time.sleep(15)
