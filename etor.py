# Input
n = int(input("Digite el valor de N: "))

# Processing
S = 0
i = 1
while i <= n:
    S = S + i
    i = i + 1

# Output
print("La suma de los primeros " + str(n) + " números naturales es: " + str(S))

