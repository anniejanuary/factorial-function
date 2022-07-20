#silnia = en. factorial
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

factorial(5)

print(f"{5} factorial is: {factorial(5)}")
