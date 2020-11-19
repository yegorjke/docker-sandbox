import logging
import math
import time

logging.basicConfig(level=logging.INFO, format="%(message)s")


def sqrt(x):
    return math.sqrt(x)


def loop(sec: int):
    i = 0
    while i < sec:
        time.sleep(1)
        i += 1
        logging.info(f"{i}...")


if __name__ == "__main__":
    logging.info("Hello World")
    # logging.info(sqrt(9))

    loop(10)
