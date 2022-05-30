lst=list(map(int,input().split()))
x=list.copy(lst)
list.sort(x)
if (x==lst):
    print("True")
else:
    print("False")
