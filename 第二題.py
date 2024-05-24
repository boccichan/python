n = int(input()) # 輸入n
count = 0 # 計算總數
while n > 0 : #跑n次迴圈
    num = int(input()) #每組人數
    if num % 3 == 0 and num != 0 : #判斷是否合格
        count = count + 1 #是就加一
    n = n - 1
print(count) #輸出