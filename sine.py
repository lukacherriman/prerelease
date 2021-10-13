"""import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()"""

"""start = 1

for i in range(start, 15):
    sum = 0
    for j in range(i-start+1, i+1):
        sum += j
    print(sum)
"""

import math
import sqlite3

def normalised_power(self, result):
    """cursor = self.connection.cursor()
    cursor.execute(f"SELECT power FROM ride{ride_id}")
    result = cursor.fetchall()"""
    average_v1 = 0

    for i in range(30, len(result)):
        total = 0
        for j in range(i - 30, i):
            print(result[j])
            total += result[j]
        weighted_average = (total/30) ** 4
        average_v1 += weighted_average

    average_v1 = average_v1 / len(result)
    normalised_power = average_v1 ** (1/4)

    return normalised_power

def power_curve(connection):
    points = [1, 5, 10, 30, 60, 300, 600, 1200, 3600]
    power_points = []
    heartrate_points = []
    cursor = connection.cursor()
    cursor.execute(f"SELECT watts FROM ride14")
    result = cursor.fetchall()
    for point in points:
        power_total = 0
        heartrate_total = 0
        power = []
        heartrate = []
        max = 0
        for i in range(len(result)):
            power.append(result[i][0])
            power_total += result[i][0]
            if len(power) > 30:
                removed = power.pop(0)
                power_total -= removed
                average = power_total // point
                if average > max:
                    max = average
        power_points.append(max)

    return points, power_points, heartrate_points

def heartrate_variance():
    print("a")
    # get the average power for the ride
    # collect average samples of data power, hr for first 10 minutes
    # collect average samples of data power, hr for the rest of the ride
    # if the power samples of data are within a range of the average
    # calculate the percentage change from the initial average
    # append the percentage change to a list with the time marker

# list = [10,20,20,25,15,35,19,20,20,25,15,35,19,20,20,25,15,35,19,20,20,25,15,35,19,20,20,25,15,35,19,20,20,25,15,35,19,20,20,25,15,35,19,20,20,25,15,35,19,20,20,25,15,35,19,20,20,25,15,35,19]
#
# print(normalised_power(1, list))
# print(math.ceil(16 ** (1/4)))


# connection = sqlite3.connect('trainingTipsDatabase.db')
# power_curve(connection)
def tss():
    TSS_list = [100 for i in range(100)]

    fitness_list = []
    total = 0
    for tss in TSS_list:
        total = total * 0.9
        total += tss
        fitness_list.append(total/10)
    print(fitness_list)

def hashing_algorithm(username, password):
    # to make sure all the hashes are unique the salt used will be their unique username
    us_list = [ord(ch) for ch in username]
    pw_list = [ord(ch) for ch in password]

    pw_weight = [pw_list[i] ** (2*(i+1)) for i in range(len(pw_list))]
    us_weight = [us_list[i] ** 2*(i+1) for i in range(len(us_list))]
    hash_pw = sum(pw_weight) + sum(us_weight)

    mod_hash = hash_pw % 2 ** 64

    return mod_hash

print(hashing_algorithm("Lcherriman", "Dank385,"))
print(hashing_algorithm("bellherry", "Dank385,"))
