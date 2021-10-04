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


### 프로그래머스 <정렬 <k번째 수
def solution(array, commands):
    answer = []
    for x in range(len(commands)):
        cut = []
        i = commands[x][0]
        j = commands[x][1]
        k = commands[x][2]
        for y in range(i-1, j):
            cut.append(array[y])
        cut.sort()
        answer.append(cut[k-1])
    return answer

### 프로그래머스 <해시 < 완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if(completion[i] != participant[i]):
            answer = participant[i]
            break

    if answer == '':
        answer = participant[-1]

    return answer
