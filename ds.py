'''Assuming there are no accidents or delays, 
the distance that a car travels down 
the inter-state can be calculated with the following formula:

Distance = Speed * Time

A car is traveling at 70 miles per hour. Write a program that displays the following:
The distance the car will travel in 6 hours
The distance the car will travel in 10 hours
The distance the car will travel in 15 hours'''

def car_speed():
    driver = int(input('> '))
    
    
    distance = int(driver * 1)
    distance1 =int(driver * 3)
    distance3 = int(driver * 6)
    distance4 = int(driver * 10)
    distance5 = int(driver * 15)
    distance6 =int( driver * 24)
    
    while True:
        
        print(f'In 1 hour, the car will travel {distance}, miles.')
        print(f'In 3 hour, the car will travel {distance1}, miles.')
        print(f'In 6 hour, the car will travel {distance3}, miles.')
        print(f'In 10 hours, the car will travel {distance4}, miles.')
        print(f'In 15 hours, the car will travel {distance5}, miles.')
        print(f'In 24 hours, the car will travel {distance6}, miles.')
        break
    
car_speed()