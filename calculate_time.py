'''
    CS 5001
    Lab 1
    Exercise 4
    Name: Karina Martinez
'''

'''
Write a Python program to solve the general version of the problem below. Ask the user for the time now (in hours),
and ask for the number of hours to wait. Your program should output what the time will be on the clock when the
alarm goes off.

You look at the clock and it is exactly 11am. You set an alarm to go off in 51 hours.
At what time does the alarm go off?

You may assume military time, so 1pm is 13:00 hours. Here is some example output:

What time is it? 23
How long until your alarm expires? 4
Your alarm will expire at 3.
'''

def main():
    current_time = int(input("What time is it?"))
    alarm = int(input("How long until your alarm expires?"))
    if alarm : 6
    alarm_time = (current_time + alarm) % 24
    print(f'Your alarm_time will expire at {alarm_time}.')
if __name__ == '__main__':
    main()
