'''distance = speed * time

if a train travels 40 miles per hour for three hours=120 miles.
Write a program that asks the 
user for the speed of a vehicle (in miles per hour) and the number 
of hours it has traveled . It should then use a loop to display the distance the vehicle has traveled for each hour of that time period.
Here is an example of the desired output:

What is the speed of the vehicle in mph? 40
How many hours has it traveled? 3 

Hour   Distance Traveled
1           40
2           80
3           120'''


def traveled():
    
    speed = float(input('Enter the speed of vehicle in mph: '))
    time = int(input('Hours traveled: '))
    
    print('Hour',"\t", "Traveled Distance")
    for currentHour in range(1, time +1):
        distance = speed * currentHour
        print(currentHour,"\t", distance)
traveled()
    
    
