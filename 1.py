# a. 生成一個整數2維陣列，大小為10x10，名稱為map
map = [[0 for _ in range(10)] for _ in range(10)]

# b. 生成一個整數1維陣列，大小為10，名稱為rowMap
rowMap = [0] * 10

# c. 給rowMap賦值
rowMap[:] = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]

# d. 在二維陣列中顯示炸彈
for index in rowMap:
    row, col = divmod(index, 10)
    map[row][col] = -1  # -1 代表炸彈位置

# e. 統計炸彈周邊的數量
def count_bombs(map):
    for i in range(10):
        for j in range(10):
            if map[i][j] == -1:  # 炸彈位置
                continue
            bomb_count = 0
            # 檢查八個鄰居
            for x in range(max(0, i-1), min(10, i+2)):
                for y in range(max(0, j-1), min(10, j+2)):
                    if map[x][y] == -1:
                        bomb_count += 1
            map[i][j] = bomb_count

count_bombs(map)

# 打印最終的二維陣列
for row in map:
    print(" ".join(str('*' if x == -1 else ' ' if x == 0 else x) for x in row))
