import time
from dataclasses import dataclass
from typing import Optional


@dataclass
# исполнитель
class Executor:
    is_connected: bool
    current_task: Optional[DAGRunTask] = None

    @property
    def is_free(self) -> bool:
        return self.current_task is None

    # время выполнения задания
    def tick(self):
        if self.current_task is not None:
            self.current_task.tick()


class ExecutionManager:
    def __init__(self, count_executors: int):
        self.__active = [self.__create_executor() for i in range(count_executors)]
        self.__inactive = []
        self.__task_queue = []

    def __create_executor(self):
        time.sleep(60)
        return Executor(is_connected=True)

    def tick(self):
        to_deactivate_list = []
        for executor in enumerate(self.__active):
            executor.tick()
            if executor.is_free:
                if len(self.__task_queue) > 0:
                    executor.current_task = self.__task_queue.pop()
                else:
                    to_deactivate_list.append()

        for idx in to_deactivate_list[::-1]:
            executor = self.__active.pop(idx)
            executor.is_connected = False
            self.__inactive.append(executor)

    def add_task_to_execution_queue(self, task: DAGRunTask):
        if len(self.__inactive) > 0:
            executor = self.__inactive.pop()
            executor.is_connected = True
            executor.current_task = task
            self.__active.append(executor)
        else:
            self.__task_queue.append(task)

        for executor in self.__active:
            if executor.is_connected and executor.is_free:
                executor.current_task = task

        executor = self.__create_executor()

    def __active_executor(self):
        if len(self.__inactive) > 0:
            executor = self.__inactive.pop()
            executor.is_connected = True
            self.__active.append(executor)
            return self.__active[-1]
