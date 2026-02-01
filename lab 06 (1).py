# a = 10
# b = 30

# if a > b:
#     print (" a is greater")
# else:
#     print("b is greater")

# # a = int(input("Enter Value for a :"))
# # b = int(input("enter value for b "))

# # if a >= b:
# #     print("print a")
    
# # else:
# # #     print("b is greater")
# # # a = int(input("enter values for a: "))
# # # b = int(input("enter values for b: "))
# # # 3# = int(input("c"))
# # # if a > b:
# # #     print("a is greater value")
    
# # # else:
# # #     print("b is greater value")
    
# # # # else:
# # # #     print("c is graeter")

# # # a = int(input("enter values for A: "))
# # # b = int(input("enter values for B: "))

# # # if a > 10 and b > 20:
# # #     print("a is greater ")
    
# # # elif a < 10 and b < 20:
# # #     print("b is greater ")

# # # else:
# # #     ("invalid")



# # # #task:
# # # num1 = float(input("Enter first number: "))
# # # num2 = float(input("Enter second number: "))
# # # num3 = float(input("Enter third number: "))

# # # if num1 >= num2 and num1 >= num3:
# # #     largest = num1
# # # elif num2 >= num1 and num2 >= num3:
# # #     largest = num2
# # # else:
# # #     largest = num3

# # # print("The largest number is:", largest)


# # # total = float(input("Enter total amount: "))

# # # if total >= 500:
# # #     discount = total * 0.20
# # #     print("Discount: 20%")
# # # elif total >= 200:
# # #     discount = total * 0.10
# # #     print("Discount: 10%")
# # # else:
# # #     discount = 0
# # #     print("No discount")

# # # final_price = total - discount
# # # print("Final price:", final_price)



# # username = input("Enter username: ")
# # password = input("Enter password: ")

# # if username == "admin" and password == "pass123":
# #     print("Login successful")
# # else:
# #     print("Login failed")



    
# speed = float(input("Enter speed: "))

# if speed == 0:
#     print("No fine")
# elif speed <= 60:
#     print("Small fine")
# else:
#     print("Heavy fine")
    
    
   
# amount = float(input("Enter purchase amount: "))

# if amount >= 1000:
#     discount = amount * 0.20
# elif amount >= 500:
#     discount = amount * 0.10
# else:
#     discount = 0

# final_price = amount - discount
# print("Final price:", final_price)


    
# def calculate_final_price(price, tax_percentage):
#     tax = price * (tax_percentage / 100)
#     final_price = price + tax
#     return final_price

# price = float(input("Enter price: "))
# tax = float(input("Enter tax percentage: "))
# result = calculate_final_price(price, tax)
# print("Final price after tax:", result)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# num = int(input("Enter a number: "))
# print("Factorial:", factorial(num))



# def calculate_average(numbers):
#     if len(numbers) == 0:
#         return 0
#     return sum(numbers) / len(numbers)


# numbers = [10, 20, 30, 40, 50]
# print("Average:", calculate_average(numbers))


def classify_temperature(celsius):
    if celsius < 10:
        return "Cold"
    elif 10 <= celsius <= 25:
        return "Warm"
    else:
        return "Hot"


temp = float(input("Enter temperature in Celsius: "))
print(classify_temperature(temp))

def calculate(num1, num2):
    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    return sum_result, difference, product

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# sum_val, diff_val, prod_val = calculate(a, b)
# print("The sum:", sum_val)
# print("The difference:", diff_val)
# print("The product:", prod_val)
