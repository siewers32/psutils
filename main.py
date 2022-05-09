import psutil

for i in psutil.pids():
    p = psutil.Process(i)

    if p.name()[:2] == "Go":
        print(p)
