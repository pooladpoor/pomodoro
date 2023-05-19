from notifypy import Notify
from time import sleep

pomodoro = int(input('pomodoro:'))
repose = int(input('repose:'))
number = int(input('number:'))

print("_"*20)
print("Let's go :)")
print("-"*20)

li = [pomodoro, repose]
while number > 0:
    for i in li:
        sleep(i*60)
        notification = Notify()
        notification.title = "استراحت" if li[0] == i else 'فوکوس'
        notification.message = "کارت عالی بود" if li[0] == i else "دوباره شروع کن"
        notification.send()
    number -= 1
    print(f"{number} times left until rest")

