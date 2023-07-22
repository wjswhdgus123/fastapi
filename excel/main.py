from openpyxl import Workbook

write_wb = Workbook()

write_ws = write_wb.create_chartsheet("생성시트")
write_ws = write_wb.active
write_ws['A1'] = 'hostname'
write_ws['B1'] = 'ip'
write_ws.append([1,2,3])
write_ws.append([4,5,6])
write_ws.cell(5, 5, '5행5열')
write_wb.save("/Users/jeonjonghyeon/fastapi/fastapi/excel/test.xlsx")