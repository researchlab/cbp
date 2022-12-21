
for i in [1, 2, 3]:
    if i == 3:
        break
    print(i)
else:
    print('break结束之后不会执行这里的代码')

for i in '中华夏国':
    if i in ['华', '夏']:
        continue
    print(i)
else:
    print('for continue 正常结束之后执行这里的代码')

i = 1
while i < 3:
    if i == 2:
        break
    print(i)
    i += 1
else:
    print('while break 结束终止, 不执行这个else的代码')

j = 0
while j < 3:
    j += 1
    if j in [1, 2]:
        continue
    print(j)
else:
    print('while continue 正常结束，执行这里的else代码')
