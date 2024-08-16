# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0

number=""
for i in range(5):
    result=input("Enter text: ")
    number+=str(result)
    max=number
    min=number
    for i in range(len(number)):
        if number[i]> max:
            max=number[i]
        elif number[i]<min:
            min=number[i]
print(max)
print(min)
        

