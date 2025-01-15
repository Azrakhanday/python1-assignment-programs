def temp_log():
    celsius=[]
    for i in range(7):
        day=["monday","tuesday","wednesday","thursday","friday","Saturday","sunday"][i]
        temp=float(input(f"enter your temperture for {day}"))
        celsius.append(temp)
        average_temp=sum(celsius)/len(celsius)
    for i ,temp in enumerate(celsius):
        print(f"{['monday','Tuesday','wednesday','thursday','friday','saturday','sunday'][i]}")

        print(f"your average temp is:{average_temp}")
temp_log()

