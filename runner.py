import subprocess


file_error_gen = 'error_gen.py'
running_error_gen = subprocess.Popen(['python', file_error_gen], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
from error_gen import error_present

if (error_present == False):
    file1_to_run = 'writer.py'
    file2_to_run = 'translator.py'


    process1 = subprocess.Popen(['python', file1_to_run], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process2 = subprocess.Popen(['python', file2_to_run], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process1.communicate()



    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')

    # Print the output
    print('Standard Output:')
    print(stdout)
    print('Standard Error:')
    print(stderr)
