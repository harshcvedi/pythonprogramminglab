def fun(x):
  return x[-1]
marks={'math':23,'python':3,'english':20}
out=dict(sorted(marks.items(),key=fun))
print(out)
