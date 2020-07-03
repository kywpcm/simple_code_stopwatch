from datetime import datetime


class StopWatch:
    def __init__(self):
        print("init...")
        self.time = 0
        self.unit = ""

    def start(self):
        # 현재 시간 저장
        self.time = datetime.now()
        return -1

    def stop(self):
        delta = datetime.now() - self.time
        return delta

    def split(self):
        return 1
