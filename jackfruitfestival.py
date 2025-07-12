N, D = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
sum = 0
while(D>0):
    sum=sum+arr[N-D]
    D=D-1
    
print(sum)
