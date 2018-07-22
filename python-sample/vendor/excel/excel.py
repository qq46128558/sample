#!/usr/bin/env python3

'excel读写操作(xls)'

import xlwt
import xlrd

# 写excel
book1=xlwt.Workbook()
sheet1=book1.add_sheet('sheet1',cell_overwrite_ok=True)

# 标题
for i in range(5):
    # 行 列 值
    sheet1.write(0,i,'Title'+str(i+1))
# 内容
for i in range(1,11):
    for j in range(5):
        # 行 列 值
        sheet1.write(i,j,'Value('+str(i)+","+str(j)+')')
book1.save('workbook1.xls')


# 读excel
book2=xlrd.open_workbook(filename='workbook1.xls')
sheet2=book2.sheet_by_name('sheet1')
for i in range(sheet2.nrows):
    print(sheet2.row_values(i))
