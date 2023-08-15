from collections import deque

class Task(object):
    

    def __init__(self, taskDesc, hasPriority=False) -> None:
        self.taskDesc = taskDesc
        self.hasPriority = hasPriority

    def __str__(self) -> str:
        return "Task: {0}, Priority:{1}".format(self.taskDesc, self.hasPriority)

task_queue = deque()

def add_task(task):
    if task.hasPriority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)

def do_task():
    return task_queue.popleft()

def print_task():
    for t in task_queue:
        print(t.task_queue)


def main():
    add_task(Task("Make List"))
    add_task(Task("Make breakfast"))
    add_task(Task("Respond to email", True))
    print_task()
    print(do_task())

    return

if __name__ == "__main__":
    main()
