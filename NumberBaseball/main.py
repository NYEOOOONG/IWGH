#made by uk, nyeong

import random

count = 0        #반복횟수
#answer = [0,1,2] #정답의 각 자릿수
answer = random.sample(range(1, 10), 3)

while(count<3):
    sbCount = [0,0]  #Strike와 Ball의 개수를 세는 리스트
    game_input = list(map(int, input("3자리 숫자를 입력해주세요: ")))
    for i in range(3):
        for j in range(3):
            if(answer[i] == game_input[j]):
                if(i==j):
                    sbCount[0] += 1
                else:
                    sbCount[1] += 1
    print(f"{sbCount[0]}S {sbCount[1]}B")
    count += 1

print(answer)