K = int(input())
st =[]
sum = 0
for i in range(K):
    n = int(input())
    if(n != 0):
        st.append(n)
    else:
        st.pop()

for j in range(len(st)):
    sum += st[j]
print(sum)