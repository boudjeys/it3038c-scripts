import time
from datetime import datetime


#collect birthdate


print('What month were you born in? (enter month number)')
bMonth = int(input())

print('What day of the month were you born on? (enter day number)')
bDay = int(input())

print('What year were you born in?')
bYear = int(input())
#according to my research, the average baby is born between 8 and 9 am, so 8:30 for my calculation here
bdDateTime = datetime(bYear, bMonth, bDay, 8, 30)


bdDelta = str(int(((datetime.now() - bdDateTime)).total_seconds()))

print()
print("Approximately " + bdDelta + " seconds have passed since " + str(bMonth) + "/" + str(bDay) + "/" + str(bYear))