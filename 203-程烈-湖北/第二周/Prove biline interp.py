def calculate_average(points):
    x_sum = 0
    y_sum = 0
    for point in points:
        x_sum += point[0]
        y_sum += point[1]
    return (x_sum / len(points), y_sum / len(points))

def is_same_point(point1, point2):
    return point1[0] == point2[0] and point1[1] == point2[1]

A = (10, 20)
B = (34, 47)
C = (55, 67)
D = (71, 87)

# 方法1
n = calculate_average([A, B])
m = calculate_average([C, D])
p1 = calculate_average([n, m])

# 方法2
p = calculate_average([A, C])
q = calculate_average([B, D])
p2 = calculate_average([p, q])

print("方法1计算得到的点p1：", p1)
print("方法2计算得到的点p2：", p2)
print("p1与p2是否重合：", is_same_point(p1, p2))
