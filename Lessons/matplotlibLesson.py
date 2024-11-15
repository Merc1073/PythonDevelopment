"""

For reference, during this lesson I was having tremendous difficulty
in getting the normal matplotlib.pyplot as plt to work, and it always gave me
an error regarding "tcl not being installed correctly". After wasting many hours of
head scratching and a lot of research, I found there seems to be a bug with
python 3.13 at the moment and tcl, therefore I had to find an alternative way
of displaying graphs and charts via matplotlib.use('Agg'), which seems to
do the job well and still allows me to view the graph, albeit at the minor
cost of creating a png file instead of a live window, which honestly may
even be considered better than a live window, it's really cool :o


Update (15/11/2024, 10:28am):

Alrighty so I've switched to Python 3.11 to make sure that matplotlib
works for this lesson. I've installed Conda and created a new testing
environment so now the graphs all appear in a new window.
This is so cool haha I love it!

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Example data
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# plot() syntax:

plt.plot(x, y, color="blue", marker="o", linestyle="-", linewidth=3, markersize=5, label="Line")

# Create the plot
plt.plot(x, y)
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Simple Line Plot")

plt.show()

x = np.linspace(1, 10, 10)
y = np.random.randint(1, 10, 10)
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 30, 20, 10]
np.random.seed(10)
data = np.random.normal(size=100)
data2 = np.random.normal(size=100)
group_data = [np.random.normal(0, std, 100) for std in range(1, 4)]
sizes = [100, 200, 300, 400, 500]
figures = []

plt.figure()
plt.bar(categories, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
figures.append(plt.gcf())

plt.show()


plt.figure()
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title("Pie Chart")
figures.append(plt.gcf())

plt.show()


plt.figure()
plt.hist(data, bins=10, color="skyblue", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency")
figures.append(plt.gcf())

plt.show()


plt.figure()
plt.scatter(x, y, c="blue")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
figures.append(plt.gcf())

plt.show()