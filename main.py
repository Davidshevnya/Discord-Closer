import psutil
import time


while True:
    for proc in psutil.process_iter():
        proc_name = [x for x in proc.name().split(".")]
        if proc_name[0].lower() == "discord":
            proc.kill()
            print("="*20 + "\n" + proc_name[0] + " was killed." + "\n" + "="*20)
    time.sleep(3)