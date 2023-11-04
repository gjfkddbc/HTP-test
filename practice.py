import tkinter as tk
import threading
import time

# 주 스레드에서 GUI를 만듭니다.
root = tk.Tk()
label = tk.Label(root, text="Original Text")
label.pack()

# 다른 스레드에서 GUI를 업데이트할 함수를 정의합니다.
def update_gui():
    # 이 함수는 주 스레드에서 실행되어야 합니다.
    label.config(text="Updated Text")

# 다른 스레드에서 GUI를 업데이트하는 함수를 실행할 스레드를 시작합니다.
def update_thread():
    # 스레드에서 일부 작업을 수행한 후, 주 스레드에서 GUI 업데이트 함수를 호출합니다.
    time.sleep(2)  # 임의의 작업 시뮬레이션
    root.after(30, update_gui)  # 0 밀리초 후에 주 스레드에서 update_gui 함수를 호출

# 다른 스레드를 시작합니다.
update_thread = threading.Thread(target=update_thread)
update_thread.start()

# Tkinter 이벤트 루프를 실행합니다.
root.mainloop()
