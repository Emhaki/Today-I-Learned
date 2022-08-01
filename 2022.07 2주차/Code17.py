A = input()
a = []
for i in range(len(A)):
    letter = ord(A[i])
    a.append(letter)

for i in range(len(A)):
    a[i] = chr(a[i]-32)
b = ''.join(a)
print(b)
