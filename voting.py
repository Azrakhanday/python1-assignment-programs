def voting_system():
    candidates={"azra":0,"mutakeen":0,"gazal":0}
    total_votes=0
    while True:
        print("1.add vote")
        print("2.view vote")
        print("3.quit")
        choice=input("enter your choice")
        if choice=="1":
            for candidate in candidates:
                print(candidates)
                vote=input("enter your vote")
                if vote in candidates:
                    candidates[vote]+=1
                    total_votes+=1
        elif choice=="2":
            print("voting result")
            for candidate,votes in candidates.items():
                print(f"{candidate}:{votes}votes")
                print(f"Total votes:{total_votes}")
        else:
            print("Quit")
voting_system()
