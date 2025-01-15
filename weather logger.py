temperature=[]
for i in range(7):
    temp=float(input(f"Enter temperature for day {i+1} (in celsius): "))
    temperature.append(temp)
average_temp=sum(temperature)/len(temperature)
print("Temperature for the week")
for i ,temp in enumerate(temperature):
    print(f"Day {i+1}:{temp}c")
print(f"Average temperature{average_temp:.2f}c")