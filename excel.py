import pandas as pd
import csv

# df = pd.read_csv(r'data.csv')
# data = df.head(1)
# print(str(data))

lines = csv.reader(open('data.csv', 'r'))
for line in lines:
    print([line[0], line[1]])

# 计算任意多边形的面积，顶点按照顺时针或者逆时针方向排列
def compute_polygon_area(points):
    point_num = len(points)
    if(point_num < 3): return 0.0
    s = points[0][1] * (points[point_num-1][0] - points[1][0])
    #for i in range(point_num): # (int i = 1 i < point_num ++i):
    for i in range(1, point_num): # 有小伙伴发现一个bug，这里做了修改，但是没有测试，需要使用的亲请测试下，以免结果不正确。
        s += points[i][1] * (points[i-1][0] - points[(i+1)%point_num][0])
    return abs(s/2.0)

# polygon = [[0,0], [2,0],[2,2], [0,2]] #4.0
polygon = [[3,3],[4,2],[6,1],[7,6],[9,7],[3,16],[0,3],[2,4],[1,5],[6,6]] #62.0
# polygon = [[3,3],[4,2],[6,4],[7,6],[9,7],[3,9],[0,5],[2,4],[4,4]] #29.0
print(compute_polygon_area(polygon))
