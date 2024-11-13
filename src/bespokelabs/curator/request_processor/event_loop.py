import asyncio
from time import sleep

import nest_asyncio


def run_in_event_loop(coroutine):
    """
    Run a coroutine in the current event loop or create a new one if there isn't one.
    """

    try:
        asyncio.get_running_loop()
        # If there is an event loop running (the call
        # above doesn't raise an exception), we can
        # use nest_asyncio to patch the event loop.
        nest_asyncio.apply()

        return asyncio.run(coroutine)
    except RuntimeError as e:
        # If no event loop is running, asyncio will
        # return a RuntimeError (https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_running_loop).
        # In that case, we can just use asyncio.run.
        return asyncio.run(coroutine)
