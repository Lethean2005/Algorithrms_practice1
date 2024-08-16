# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# text = "9394884039"
# Count=0
# for i in range(len(text)):
#     if text[i]=="8":
#         Count+=1
# print(Count)
# Q2 - What is first index of letter 8
text = "9394884039"
possition=0
isfound=False
for i in range(len(text)):
    if text[i]=="8" and not isfound:
        possition=i
        isfound=True
print(possition)
