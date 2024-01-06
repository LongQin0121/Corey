import random,math,datetime,calendar
import os
import antigravity


courses = ['History','Math','Physics','CompSci']

random_course = random.choice(courses)

print(random_course)

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

print(os.getcwd())  # current working directory
print(os.__file__)