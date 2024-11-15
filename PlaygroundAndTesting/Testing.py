import matplotlib.pyplot as plt

# All the stuff below is for a line graph

x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]

x2 = [2, 4, 8, 16, 20]
y2 = [1, 2, 3, 4, 2]

plt.plot(x1, y1, marker='o', linestyle="-.", color="red", linewidth=3, label="Red One")
plt.plot(x2, y2, marker='D', linestyle="-", color="blue", linewidth=2, label="Blue One")
plt.annotate("Peak", xy=(16, 2), xytext=(15, 5), arrowprops=dict(facecolor="black", arrowstyle="->"))
plt.title("Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.grid(True)
plt.show()


# All the stuff below is for a pie chart

pie_sizes = [30, 20, 5, 45, 10]
pie_labels = ["A", "B", "C", "D", "E"]
pie_explode = [0.1, 0, 0, 0, 0]

plt.pie(pie_sizes, labels=pie_labels, autopct="%1.1f%%", explode=pie_explode, shadow=True, startangle=90)
plt.title("Pie Chart Example")
plt.show()