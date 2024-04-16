# count = 0
# i = 13
# while i != 0:
#     count = count + 1
#     print("meow", count)
#     i = i - 1


# for _ in range(3):
    # print("cow")


# print("cow\n" * 3, end = "")


# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break #Si dala atkartosies kamer neizpildisies nosacijums
# for i in range(n):
#     print("cow")


# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if n > 0:
#             break
#     return n
        
# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()


produkti = {
    "Maize": "Graudu produkts",
    "Krējums": "Piena produkts",
    "Piens": "Piena produkts",
    "Olas": "Dzīvnieku produkts",
    "Gaļa": "Dzīvnieku produkts",
    "Milti": "Graudu produkts",
    "Burkāns": "Dārzeņi"
}

for produkts in produkti:
    print(produkts, produkti[produkts], sep = " - ") #sep - separators


import pandas as pd;

# def