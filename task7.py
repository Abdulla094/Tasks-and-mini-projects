import matplotlib.pyplot as plt
import numpy as np

data = []
grades = ['DISTINCTION', 'FIRST CLASS',
          'SECOND CLASS', 'PASS CLASS', 'FAIL CLASS']

for g in grades:
    
    student = int(input(f"Enter the percentage of student {g}"))
    data.append(student)
    

color = ['yellow', 'green', 'red', 'blue', 'maroon']
explode = (0.1, 0.1, 0.1, 0.1, 0.1)

fig = plt.figure(figsize=(10, 10))
plt.pie(data, labels=grades, colors=color,
        explode=explode, startangle=90, shadow=True)

plt.legend(loc='best', title='GRADES')
plt.show()