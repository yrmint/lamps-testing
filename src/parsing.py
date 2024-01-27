import re

"""
    Parse the file with experimental data
"""


f = open('task_1_lamps_testing.txt', 'r')
m = []
s = []

str = re.split(":|=|\n|,", f.readline())
n, nexp = int(str[1]), int(str[3])  # number of bulbs and number of experiments
f.readline()
for line in f:
    str1 = re.split("# |, |: |, 's': |}\n", line)
    m.append(int(str1[4]))  # selected bulbs
    s.append(int(str1[6]))  # faulty bulbs among selected
f.close()
