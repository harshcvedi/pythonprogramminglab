def perfect_number(n):
  sum=0
  for i in range(1,n):
    if (n%i==0):
      sum=sum+i
   return sum == n
print(perfect_number(6))
