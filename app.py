import logging
import math

logging.basicConfig(level=logging.INFO, format="%(message)s")


def sqrt(x):
    return math.sqrt(x)


if __name__ == "__main__":
    logging.info("Hello World")
    logging.info(sqrt(9))
