# coding=UTF-8
import datetime
from z3 import *
from time import time


import xlwt

solver = Solver()

pathImgOri = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
]
# for x in range(10):
#     for y in range(10):
#         pathImgOri[x][y] = 0
Agents = ["A", "B", "C", "D", "E"]
# Agents = ["A", "B", "C", "D", "E","F","G","H","I","J","K","L","M","N","O"]
# Agents = ["A","B"]
# Agents = ["A"]
# startX = [0, 1, 1, 0, 2, 3, 4, 4, 8, 9,9,7,8,8,9]  # Ｘ轴坐标
# startY = [0, 0, 1, 1, 1, 1, 1, 2, 8, 9,8,7,7,6,7]
#
# endX = [8, 9, 9, 7, 8, 8, 9, 6, 0, 1,1,0,2,3,4]
# endY = [8, 9, 8, 7, 7, 6, 7, 6, 0, 0,1,1,1,1,1]

startVertexs = [(0, 0), (1, 0), (1, 1), (0, 1), (2, 1),
                (3, 1), (4, 1), (4, 2), (8, 8), (9, 9),
                (9, 8), (7, 7), (8, 7),(8, 6), (9, 7)]
endVertexs = [(8, 8), (9, 9), (9, 8), (7, 7), (8, 7),
              (8, 6), (9, 7), (6, 6), (0, 0), (1, 0),
              (1, 1), (0, 1), (2, 1), (3, 1), (4, 1)]



# -------------------------------------------------------------------
# pathImgOri = [
#     [0, 0, 1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1, 0, 1, 1],
#     [1, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 1, 0, 1],
#     [1, 1, 1, 1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 0, 0, 0, 0]
# ]
# Agents = ["A","B","C","D","E"]
# startX = [0, 1,1,0,2]  # Ｘ轴坐标
# startY = [0, 0,1,1,1]
#
# endX = [5,7,7,7,7]
# endY = [1,4,5,6,7]
# -------------------------------------------------------------------
# pathImg = [
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
#     [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
#     [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
# ]
# Agents = ["A", "B", "C", "D", "E"]  # 表示机器人
# startX = [0, 1, 0, 1, 5]  # Ｘ轴坐标
# startY = [0, 0, 1, 1, 2]
#
# endX = [28, 28, 27, 26, 25]
# endY = [28, 27, 28, 26, 28]
# -----------------------------------------------

# pathImg = []
# for x in range(3):
#     pathImg2 = []
#     for y in range(3):
#         pathImg2.append(0)
#     pathImg.append(pathImg2)
#
# Agents = []
# startX = []  # Ｘ轴坐标
# startY = []
# endX = []
# endY = []
#
# for agt in range(3):
#     Agents.append("A"+str(agt))
#     startX.append(0)
#     startY.append(agt)
#     endX.append(0)
#     endY.append(agt)
#
#     Agents.append("B"+str(agt))
#     startX.append(1)
#     startY.append(agt)
#     endX.append(1)
#     endY.append(agt)
#
# for agt in range(2):
#     Agents.append("C"+str(agt))
#     startX.append(2)
#     startY.append(agt)
#     endX.append(2)
#     endY.append(agt)
#
# endX[0] = 2
# endY[0] = 2
# -----------------------------------------------

startX = []
startY = []
endX = []
endY = []

for agt in range(len(Agents)):
    startX.append(startVertexs[agt][0])
    startY.append(startVertexs[agt][1])
    endX.append(endVertexs[agt][0])
    endY.append(endVertexs[agt][1])

pathImg =[[1 for mm in range(len(pathImgOri[0])+2)] for nn in range(len(pathImgOri)+2)]
for x in range(len(pathImgOri)):
    for y in range(len(pathImgOri[0])):
           pathImg[x+1][y+1] = pathImgOri[x][y]

print pathImg
for agt in range(len(Agents)):
    startX[agt] = startX[agt] + 1
    startY[agt] = startY[agt] + 1
    endX[agt] = endX[agt] + 1
    endY[agt] = endY[agt] + 1

rows = len(pathImg)  # 行数
cols = len(pathImg[0])  # 列数

VERTEX = 0  # 途中表示顶点的字符

graphSize = rows * cols
print "graphSize:", graphSize

timeStep = 0
isSat = unsat

# for x in range(rows):
#     for y in range(cols):
#         if pathImg[x][y] == 0:
#             solver.add(Bool("graph_x"+str(x)+"_y"+str(y)))
#         else:
#             solver.add(Not(Bool("graph_x"+str(x)+"_y"+str(y))))

for agt in range(len(Agents)):
    current = Int(str(Agents[agt] + "_t0"))
    solver.add(current == startX[agt] * cols + startY[agt])

# print solver.check()
# print solver.model()

starttime = time()  # 计时

agentsNum = len(Agents)


# 起点终点最短距离
def minDistance():
    min = 0
    for agt in range(agentsNum):
        distance = int(
            math.sqrt(abs(math.pow((endX[agt] - startX[agt]), 2) + math.pow((endY[agt] - startY[agt]), 2)))) - 1
        if min < distance:
            min = distance
    return min


for agt in range(agentsNum):
    if (pathImg[startX[agt]][startY[agt]] != VERTEX):
        print "agent的起点不能为障碍物"
        exit()
    if (pathImg[endX[agt]][endY[agt]] != VERTEX):
        print "agent的终点不能为障碍物"
        exit()

for agt in range(agentsNum):
    for agt2 in range(agt + 1, agentsNum):
        if (startX[agt] == startX[agt2] and startY[agt] == startY[agt2]):
            print "Agent", Agents[agt], "与Agent", Agents[agt2], "所在起点冲突"
            exit()
        if (endX[agt] == endX[agt2] and endY[agt] == endY[agt2]):
            print "Agent", Agents[agt], "与Agent", Agents[agt2], "所在终点冲突"
            exit()

# graph = []
# for x in range(len(pathImg)):
#     for y in range(len(pathImg[0])):
#         if pathImg[x][y] == 0:
#             # solver.add(Int(str(Agents[agt] + "_t" + str(timeStep+1))) != x * rows + y) # agent不能在有障碍物的位置
#             # constraintArr_graph.append(Int(str(Agents[agt] + "_t" + str(timeStep + 1))) == x * rows + y)
#             p = [x, y]
#             graph.append(p)

# 获取agent在timsStep时刻下的最大移动范围
def getRange(timeStep,startVertex):
    timeStep = timeStep + 1
    x = startVertex[0]
    y = startVertex[1]
    range_x = [x - timeStep, x + timeStep]
    range_y = [y - timeStep, y + timeStep]
    if range_x[0] < 0:
        range_x[0] = 0
    if range_y[0] < 0:
        range_y[0] = 0
    if range_x[1] > rows:
        range_x[1] = rows
    if range_y[1] > cols:
        range_y[1] = cols

    return [range_x,range_y]


while isSat == unsat:
    # constraintArr_current = []
    constraintArr_next = []

    for agt in range(len(Agents)):
        # constraintArr_current.append(Int(str(Agents[agt] + "_t" + str(timeStep))))

        current = Int(str(Agents[agt] + "_t" + str(timeStep)))
        next = Int(str(Agents[agt] + "_t" + str(timeStep + 1)))
        MvUp = current - cols
        MvDown = current + cols
        MvLeft = current - 1
        MvRight = current + 1
        Wait = current
        # solver.add(Or(next == MvUp,next == MvDown,next == MvLeft, next == MvRight, next == Wait))
        MvLeftUp = current - cols - 1
        MvRightUp = current - cols + 1
        MvLeftDown = current + cols - 1
        MvRightDown = current + cols + 1
        solver.add(Or(next == MvUp, next == MvDown, next == MvLeft, next == MvRight, next == Wait,
                      next == MvLeftUp, next == MvRightUp, next == MvLeftDown, next == MvRightDown))
        solver.add(next >= 0)

        constraintArr_graph = []
        currentRange = getRange(timeStep+1, startVertexs[agt])
        for x in range(currentRange[0][0],currentRange[0][1]):
            for y in range(currentRange[1][0],currentRange[1][1]):
                if pathImg[x][y] == 0:
                    # solver.add(Int(str(Agents[agt] + "_t" + str(timeStep+1))) != x * rows + y) # agent不能在有障碍物的位置
                    constraintArr_graph.append(Int(str(Agents[agt] + "_t" + str(timeStep+1))) == x * rows + y)
        # for g in range(len(graph)):
        #     constraintArr_graph.append(
        #         Int(str(Agents[agt] + "_t" + str(timeStep + 1))) == graph[g][0] * rows + (graph[g][1]))
        solver.add(Or(constraintArr_graph))


        for agt2 in range(len(Agents)):
            if agt != agt2:
                solver.add(Int(str(Agents[agt2] + "_t" + str(timeStep + 1))) != Int(
                    str(Agents[agt] + "_t" + str(timeStep))))  # 跟随约束

        constraintArr_next.append(next)


    for c1 in range(len(constraintArr_next)):
        for c2 in range(len(constraintArr_next)):
            if c2 != c1:
                solver.add(constraintArr_next[c1] != constraintArr_next[c2])  # 碰撞约束

    if timeStep > minDistance(): # 当步骤大于图中起点和终点最近的agent
        solver.push()
        for agt in range(len(Agents)):
            solver.add(Int(str(Agents[agt] + "_t" + str(timeStep + 1))) == endX[agt] * cols + endY[agt])  # 目标位置
            # print "end:",endX[agt] * cols + endY[agt],"\tt=",timeStep

        isSat = solver.check()
        # if isSat == sat:
        # print solver.model()
        solver.pop()
    dur = time() - starttime
    print "第", timeStep, "次", isSat, "\ttime:", ('%0.6f秒' % dur)
    timeStep = timeStep + 1

pathPlan = [["" for mm in range(cols + 1)] for nn in range(rows + 1)]

f = open('test.txt', 'w')

for agt in range(len(Agents)):
    for t in range(timeStep + 1):
        b = Int(str(Agents[agt] + "_t" + str(t)))
        v = int(str(solver.model().evaluate(b)))
        # f.write(str(b) + "=" + str(v) + "\tx=" + str(v / cols) + ",y=" + str(v % cols))
        pathPlan[v / cols][v % cols] = pathPlan[v / cols][v % cols] + str(b) + ","

f.write(str(solver.model()))
f.close()

print pathPlan

# 写入excel中
file_excel = '/home/dzhb/Documents/MultiAgents_INT.xlsx'
newfile = xlwt.Workbook()
newSheet = newfile.add_sheet('Simple', cell_overwrite_ok=True)
style1 = xlwt.easyxf('pattern: pattern solid, fore_colour black;')
style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white;')
for i in range(rows):
    for j in range(cols):
        if (pathImg[i][j] != VERTEX):
            # newSheet.write(i, j, 1, style1)
            newSheet.write(i, j, pathPlan[i][j], style1)

        else:
            newSheet.write(i, j, pathPlan[i][j], style2)

newfile.save(file_excel)

print "Finish!!!"
