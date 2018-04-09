import subprocess
from openpyxl import load_workbook

filename = raw_input('Excel file name: ')
if '.xlsx' not in filename:
 filename += '.xlsx'

workbook = load_workbook(filename = filename).active

start_row = int(raw_input('Start row: '))
end_row = int(raw_input('End row: '))
num_rows = end_row - start_row + 1

data_directory = raw_input('Data directory: ')

for i in range(num_rows):
  index = str(i + start_row)
  pid = workbook['A' + index].value
  date = workbook['B' + index].value
  start_time = workbook['C' + index].value
  end_time = workbook['D' + index].value

  print 'Processing patient data...'
  print ' - {}'.format(pid)
  print ' - {}'.format(date)
  print ' - {}'.format(start_time)
  print ' - {}'.format(end_time)
  print
  subprocess.call('./sort_helper.sh {} {} {} {}'.format(pid, date, start_time, end_time, data_directory), shell=True)

print 'Sorting complete!\n'
