def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if (ay1 >= by2 or by1 >= ay2 or ax1 >= bx2 or bx1 >= ax2) or (ax1 == ax2 and ay1 == ay2) or \
            bx1 == bx2 or by1 == by2:
        return (ay2 - ay1) * (ax2 - ax1) + (by2 - by1) * (bx2 - bx1)

    else:
        area, x_lim, y_lim =0, (min(ax1, bx1), max(ax2, bx2)), (min(ay1, by1), max(ay2, by2))
        for i in range(x_lim[1]-x_lim[0]):
            i = i + x_lim[0]
            for j in range(y_lim[1]-y_lim[0]):
                j = j + y_lim[0]
                if (ax1 > i or i >= ax2 or ay1 > j or j >= ay2) and (bx1 > i or i >= bx2 or by1 > j or j >= by2):
                    continue
                area = area + 1
    return area

print(computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))