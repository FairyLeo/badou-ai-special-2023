def calculate_average(points):
    # 初始化x坐标和y坐标的总和为0
    x_sum = 0
    y_sum = 0

    # 遍历所有点
    for point in points:
        # 将当前点的x坐标加到x_sum上
        x_sum += point[0]
        # 将当前点的y坐标加到y_sum上
        y_sum += point[1]

    # 计算平均点的x坐标和y坐标
    avg_x = x_sum / len(points)
    avg_y = y_sum / len(points)

    # 返回平均点的坐标
    return (avg_x, avg_y)


def is_same_point(point1, point2):
    # 判断两个点的x坐标和y坐标是否都相等
    if point1[0] == point2[0] and point1[1] == point2[1]:
        return True
    else:
        return False

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
