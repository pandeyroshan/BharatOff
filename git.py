import os
import time
import random

def execute_task():
    day = 1
    while True:
        message = ["OTP Token Change", "Authentication API Update", "Unused middleware removed","Updated ASGI"]

        os.system("cd /home/roshan/WORK/bharatoff/")
        os.system("git add .")
        commit_str = 'git commit --date="{0} day ago" -m "{1}" '.format(str(day), message[random.randint(0,3)])
        print(commit_str)
        os.system(commit_str)
        os.system("git push")

        day+=1
        time.sleep(1)

execute_task()







