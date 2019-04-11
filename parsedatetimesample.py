import parsedatetime as pdt
from datetime import datetime

cal = pdt.Calendar()

examples = [
  "2016-07-16",
  "2016/07/16",
  "2016-7-16",
  "2016/7/16",
  "07-16-2016",
  "7-16-16",
  "7/16/16"
]

print('{:30s}{:>30s}'.format('Input','Result'))
print('=' * 60)
for e in examples:
  dt, result = cal.parseDT(e)
  print('{:<30s}{:>30s}'.format(f'"{e}"', dt.ctime()))

examples2 = [
  "19 November 1975",
  "19 November 75",
  "19 Nov 75",
  "tomorrow",
  "yesterday",
  "10 minutes from now",
  "the first of January, 2001",
  "3 days ago",
  "in four days' time",
  "two weeks from now",
  "three months ago",
  "2 weeks and 3 days in the future"
]

print('*' * 60)
print(f'Now: {datetime.now()}')
print('{:30s}{:>30s}'.format('Input', 'Result'))
print('=' * 60)
for e in examples2:
  dt, result = cal.parseDT(e)
  print('{:<30s}{:>30s}'.format(f'"{e}"', dt.ctime()))