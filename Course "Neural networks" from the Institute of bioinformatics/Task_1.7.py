"""https://stepik.org/lesson/18696/step/15?unit=4493"""

import urllib
from urllib import request
import numpy as np

fname = """https://stepic.org/media/attachments/lesson/16462/boston_houses.csv"""   # read file name from stdin
f = urllib.request.urlopen(fname)   # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)   # load data to work with
x = data.copy()
y = []
for i in x:
    y.append(i[0])
    i[0] = 1
answer = np.linalg.inv(x.T @ x) @ x.T @ y
print(*answer)


"""second way"""

x = np.loadtxt(request.urlopen(input()), skiprows=1, delimiter=',')
y = x[:, 0].copy()
x[:, 0] = 1
answer = np.linalg.inv(x.T @ x) @ x.T @ y
print(*answer)


