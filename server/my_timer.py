import time

class Timer:
    def __init__(self):
        self.timings = {}
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def record_timing(self, name):
        if name in self.timings:
            raise ValueError(f"Timing '{name}' already recorded.")
        if self.start_time is None:
            raise ValueError("Timer has not been started.")
        if self.end_time is None:
            raise ValueError("Timer has not been stopped.")
        self.timings[name] = self.end_time - self.start_time

    def get_timing(self, name):
        if name not in self.timings:
            raise ValueError(f"Timing '{name}' has not been recorded.")
        return self.timings[name]

    def print_timings(self):
        for name, timing in self.timings.items():
            print(f"{name}: {timing:.2f} 秒")

# 示例使用
if __name__ == '__main__':
    timer = Timer()

    # 记录第一段时间
    timer.start()
    print("第一段程序开始运行...")
    time.sleep(2)  # 模拟第一段程序运行中的一些操作
    timer.stop()
    timer.record_timing("第一段")

    # 记录第二段时间
    timer.start()
    print("第二段程序开始运行...")
    time.sleep(5)  # 模拟第二段程序运行中的一些操作
    timer.stop()
    timer.record_timing("第二段")

    # 打印各段时间
    timer.print_timings()
