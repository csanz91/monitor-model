import logging
import logging.handlers
import signal

from threading import Event
from zoneinfo import ZoneInfo
from notifiers import get_notifier

from docker_secrets import getDocketSecrets


logger = logging.getLogger()
handler = logging.handlers.RotatingFileHandler(
    "/app/logs/main.log", mode="a", maxBytes=1024 * 1024 * 10, backupCount=2
)
formatter = logging.Formatter(
    "%(asctime)s <%(levelname).1s> %(funcName)s:%(lineno)s: %(message)s"
)
logger.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

TELEGRAM_TOKEN = getDocketSecrets("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = getDocketSecrets("TELEGRAM_CHAT_ID")

telegram = get_notifier("telegram")

exitEvent = Event()


def exit_gracefully(signum, frame):
    exitEvent.set()


signal.signal(signal.SIGINT, exit_gracefully)
signal.signal(signal.SIGTERM, exit_gracefully)

tz = ZoneInfo(key="Europe/Madrid")

logger.info("Starting...")

SLEEP_INTERVAL = 30

def check_stock():
    # Check stock
    return True

try:

    while not exitEvent.is_set():
        stock_available = check_stock()
        if stock_available:
            logger.info("Stock available")
            telegram.notify(
                    message=f"¡Stock disponible!",
                    token=TELEGRAM_TOKEN,
                    chat_id=TELEGRAM_CHAT_ID,
                )
            exit(0)
            
        exitEvent.wait(SLEEP_INTERVAL)

finally:
    logger.info("Exiting...")
