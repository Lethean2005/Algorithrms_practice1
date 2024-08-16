# Ex4 - String 
text = "3 4 5 6"
# Q1 - display number 1 by one without space
for number in text:
    if number!= " ":
        print(number)
# Q2 - Sum all number (Total: 18)
sum=0
for number in text:
    if number!=" ":
        sum+=int(number)
print("sum all number: ",sum)
