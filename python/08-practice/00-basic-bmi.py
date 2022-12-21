
weight=input('input weight:')
height=input('input height:')

bmi = float(weight) / ((float(height)/100)**2)

if bmi < 18.5:
    print('体重过轻')
if bmi > 24:
    print('体重过重')
else:
    print('体重正常')
