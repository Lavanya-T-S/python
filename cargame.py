command=""
started=False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("car is already started")
        else:
            started=True
            print("car started..") 
    elif command=="stop":
        if not started:
            print("car is already stoped")
        else:
            started=False
            print("car stopped..")