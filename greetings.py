import time
stamp = time.strftime("%H:%M:%S")
stamp1= int(time.strftime("%H"))
stamp2 = int(time.strftime("%M"))
stamp3 = int(time.strftime("%S"))
# print(stamp)
# print(stamp1)
# print(stamp2)
# print(stamp3)

if (stamp1 < 12):
    print("good morning\nThe time is ", stamp)

elif(stamp1 > 12 and stamp1 < 20):
    print("good afternoon\nThe time is ", stamp)

else:
    print("good night\nThe time is ", stamp)