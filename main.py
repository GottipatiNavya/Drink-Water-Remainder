import time
from plyer import notification

while True:
    notification.notify(
        title="Please drink some water 💧 ",
        message="You need to drink some water to stay hydrated!",
        timeout=10
    )
    time.sleep(60 * 60)
