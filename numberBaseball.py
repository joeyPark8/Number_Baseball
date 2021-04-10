import random

num = random.sample(range(1, 10), 3)

while True:
    inputNum = input('숫자를 입력: ').split()
    result = {'strike':0, 'ball':0}
    for i in inputNum:
        iNum = int(i)
        if iNum in num:
            if inputNum.index(i) == num.index(iNum):
                result['strike'] += 1
            else:
                result['ball'] += 1
    print(result, '\n')
    if result['strike'] == 3:
        print('맞추셨습니다!')
        break
        
