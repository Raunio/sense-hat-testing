from globals import Globals
import asyncio
class RepeatableTask:
    def __init__(self, task, condition):
        self.task = task
        self.condition = condition
    async def update(self):
        while self.condition:
            self.task()
            await asyncio.sleep(Globals.UPDATE_INTERVAL)

