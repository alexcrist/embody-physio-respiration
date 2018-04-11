from openpyxl import load_workbook
import os
import shutil

filename = raw_input('Excel file name: ')
if '.xlsx' not in filename:
 filename += '.xlsx'

workbook = load_workbook(filename = filename).active

start_row = int(raw_input('Start row: '))
end_row = int(raw_input('End row: '))
num_rows = end_row - start_row + 1

data_dir = raw_input('Data directory: ')
output_dir = raw_input('Output directory: ')

def process(pid, date, start_time, end_time, data_dir, output_dir):
  pid_dir = os.path.join(output_dir, str(pid))
  if not os.path.exists(pid_dir):
    os.makedirs(pid_dir)

  start_time = int(start_time)
  end_time = int(end_time)
  files = os.listdir(data_dir);
  for file in files:
    try:
      file_date = file[7:15]
      file_time = int(file[16:22])

      if file_date == date:
        if file_time > start_time and file_time < end_time:
          file_path = os.path.join(data_dir, file)
          output_path = os.path.join(pid_dir, file)
          shutil.copyfile(file_path, output_path)
    catch:
      print 'Ignoring file "' + file + '"'

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

  process(pid, date, start_time, end_time, data_dir, output_dir)

  break

print 'Sorting complete!\n'
