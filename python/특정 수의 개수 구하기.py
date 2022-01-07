from bisect import bisect_left, bisect_right

def count_by_range(array,left,right):
    right=bisect_right(array,right)
    left=bisect_left(array,left)
    return = right-left

n,x=map(int,input().split())
array=list(map(int,input().split(' ')))

count=count_by_range(array,x,x)

if count ==0
    print(-1)
else:
    print(count)
    
