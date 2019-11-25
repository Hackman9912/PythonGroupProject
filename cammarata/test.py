import io
import sys

stdout = sys.stdout
sys.stdout = io.StringIO()

help('modules')

output = sys.stdout.getvalue()
sys.stdout = stdout

print('hi')
