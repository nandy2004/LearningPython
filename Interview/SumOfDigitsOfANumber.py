def Number():
    num=input("Enter any number more than single digit : ")
    summ=0
    for i in num:
        summ=summ+int(i)
    return summ

result=Number()
print(result)