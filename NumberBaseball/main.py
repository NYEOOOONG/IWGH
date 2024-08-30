count = 0        #반복횟수
answer = [0,1,2] #정답의 각 자릿수
sbCount = [0,0]  #Strike와 Ball의 개수를 세는 리스트

while(count < 3):
    try:
        a, b, c = input("3자리 숫자를 입력해주세요: ")
        break
    except:
        count += 1


