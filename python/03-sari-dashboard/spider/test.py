import csv

headers = ['No','name','age']
values = [
        {'No':'01','name':'zhanshan','age':18},
        {'No':'02','name':'mike','age':118},
        {'No':'03','name':'json','age':19},
        ]

values_arr = [
        [1,'somesh',18],
        [2,'mike',17],
        [3,'json',19],
        [4,'jack',20],
        ]

with open('test.csv','w',newline='') as fp:
    dic_writer = csv.DictWriter(fp, headers)
    dic_writer.writeheader()
    dic_writer.writerows(values)

with open('test_arr.csv', 'w', newline='') as fp:
    x = csv.writer(fp)
    x.writerow(headers)
    x.writerows(values_arr)
