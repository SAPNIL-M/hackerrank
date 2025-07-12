import sys
num1=int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
num2=int(input())

arr1.sort()
arr2.sort()

arr2=arr2[::-1]
sum=0
diff=0
money=0
for i in range(num1):
    if(arr1[i]+arr2[i]>num2):
        sum=arr1[i]+arr2[i]
        diff=sum-num2
        money=money+diff

print(money*100)
        
        
