
# print("Started")

# 5 times

# a=0

# while a<5:
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     a+=1

# no of iteration: 1,2,3,4,5
# a = 0,1,2,3,4,5


# print("End")

# a="Priyanka"

# print(a[7])
# print(len(a))

# i=range(10,30,3)

# for p in i:
#     print(p)

# print(list(range(100)))

# for i in range(1,101,1):
#      print(i)

# i=0

# while i<=10:
#     if i==5:
#         continue
#     print(i)
#     i+=1

# print("Loop ended")

# i=0,1,2,3,4,5
# iter =1,2,3,4,5
# out = 0,1,2,3,4

# no of iteration: inf

# for i in range(1,101):
#     if i==30:
#         continue
#     print(i)


# 1 - 100 num 
# no of iter = 100

# for i in range(1,101):
#     print(i)

secret_num=33

while True:
    num = int(input("Enter a number: "))

    if num==secret_num:
        print("You got it!")
        break
    else:
        print("Try again!")