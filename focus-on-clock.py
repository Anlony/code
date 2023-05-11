# code
import time

def pomodoro(focus_time=25, break_time=5):
    print(f"开始工作，专注 {focus_time} 分钟!")
    time.sleep(focus_time * 60)
    print(f"休息时间，休息 {break_time} 分钟!")
    time.sleep(break_time * 60)

while True:
    pomodoro()
