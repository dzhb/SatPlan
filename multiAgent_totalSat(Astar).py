# coding=UTF-8
import datetime
from z3 import *
from time import time
from singleAgent.Astar import astar
import re

import xlwt

solver1 = Solver()

# def min(a,b):
#     if a >= b:
#         return b
#     else:
#         return a

pathImg = [
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
#         pathImg[x][y] = 0
Agents = ["A", "B", "C", "D", "E"]
# Agents = ["A", "B", "C", "D", "E","F","G","H","I","J","K","L","M","N","O"]
# Agents = ["A","B", "C"]
# Agents = ["A"]
# startX = [0, 1, 1, 0, 2, 3, 4, 4, 8, 9,9,7,8,8,9]  # Ｘ轴坐标
# startY = [0, 0, 1, 1, 1, 1, 1, 2, 8, 9,8,7,7,  6,7]
# endX = [8, 9, 9, 7, 8, 8, 9, 6, 0, 1,1,0,2,3,4]
# endY = [8, 9, 8, 7, 7, 6, 7, 6, 0, 0,1,1,1,1,1]



startVertexs = [(0, 0), (1, 0), (1, 1), (0, 1), (2, 1),
                (3, 1), (4, 1), (4, 2), (8, 8), (9, 9),
                (9, 8), (7, 7), (8, 7),(8, 6), (9, 7)]
endVertexs = [(8, 8), (9, 9), (9, 8), (7, 7), (8, 7),
              (8, 6), (9, 7), (6, 6), (0, 0), (1, 0),
              (1, 1), (0, 1), (2, 1), (3, 1), (4, 1)]




# pathImg = []
# for x in range(100):
#     pathImg2 = []
#     for y in range(100):
#         pathImg2.append(0)
#     pathImg.append(pathImg2)
#
# startVertexs = [(0, 0), (1, 0), (2, 1), (0, 1), (1, 1),
#                 (3, 1), (4, 1), (4, 2), (8, 8), (9, 9),
#                 (9, 8), (7, 7), (8, 7),(8, 6), (9, 7)]
# endVertexs = [(99, 99), (89, 89), (88, 87), (87, 87), (89, 88),
#               (88, 86), (89, 87), (6, 6), (0, 0), (1, 0),
#               (1, 1), (0, 1), (2, 1), (3, 1), (4, 1)]


startX = []
startY = []
endX = []
endY = []

for agt in range(len(Agents)):
    startX.append(startVertexs[agt][0])
    startY.append(startVertexs[agt][1])
    endX.append(endVertexs[agt][0])
    endY.append(endVertexs[agt][1])

# -------------------------------------------------------------------


rows = len(pathImg)  # 行数
cols = len(pathImg[0])  # 列数

f = open('test.txt', 'w')

agentsNum = len(Agents)
timestep = 0  # 记录时间
currentAgent = 0  # 当前agent
isSat = unsat
constrainstsArr = []  # 约束
starttime = time()  # 计时

VERTEX = 0  # 途中表示顶点的字符


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

allPath = []
for agt in range(len(Agents)):
    path = astar(pathImg, startVertexs[agt], endVertexs[agt])
    allPath.append(path)
print "allPath:", allPath

colideList = [0 for mm in range(len(Agents))]  # 各Agent发生冲突的数量
for agt1 in range(len(Agents)):
    for agt2 in range(agt1 + 1, len(Agents)):
        dur = min(len(allPath[agt1]), len(allPath[agt2]))
        for timestep in range(dur-1):
            if ((allPath[agt1][timestep] == allPath[agt2][timestep])):
                print "发生碰撞冲突：", agt1, agt2, "t =", timestep
                colideList[agt1] = colideList[agt1] + 1
                colideList[agt2] = colideList[agt2] + 1
                break
            if ((allPath[agt1][timestep] == allPath[agt2][timestep+1])):
                print "发生跟随冲突：", agt1, agt2, "t =", timestep
                colideList[agt1] = colideList[agt1] + 1
                colideList[agt2] = colideList[agt2] + 1
                break

print colideList



# 获取未与其他agent发生冲突的agent列表,若所有不存在这种agent,这选择一个冲突数最少的
# colideList 表示每个agent与其他agent的A*求解路径发生冲突的数量
def getEarlyPathAgentList(colideList):
    earlyPathList = []
    temp_minColidNum = min(colideList)
    if temp_minColidNum == 0:
        for agt in range(len(colideList)):
            if colideList[agt] == 0:
                earlyPathList.append(agt)
    # else:
    #     for agt in range(len(colideList)):
    #         if colideList[agt] == temp_minColidNum:
    #             earlyPathList.append(agt)
    #             break
    return earlyPathList

earlyPathAgentList = getEarlyPathAgentList(colideList)

print "ooo:",earlyPathAgentList



earlyPath_expr = []
maxTime = 0
for agt in range(len(colideList)):
    expr = []
    if agt in earlyPathAgentList:
        maxTime = max(maxTime, len(allPath[agt]))
        for timestep in range(len(allPath[agt])):
            expr.append(Bool(
                str(Agents[agt]) + "_t" + str(timestep) + "_x" + str(allPath[agt][timestep][0]) + "_y" + str(
                    allPath[agt][timestep][1])))
    earlyPath_expr.append(expr)

print "预先路径：", earlyPath_expr
print "预先最长时间:", maxTime

# init first vertex for per agent
for p in range(len(Agents)):
    solver1.append(Bool(Agents[p] + "_t" + str(timestep) + "_x" + str(startX[p]) + "_y" + str(startY[p])))

for i in range(len(earlyPath_expr)):
    # solver1.add(And(earlyPath_expr[i]))
    for j in range(len(earlyPath_expr[i])):
        solver1.add(earlyPath_expr[i][j])

while isSat == unsat:
    for currentAgent in range(len(Agents)):
        if currentAgent not in earlyPathAgentList:
            currentRange = getRange(timestep, startVertexs[currentAgent])
            for i in range(currentRange[0][0],currentRange[0][1]):
                for j in range(currentRange[1][0],currentRange[1][1]):
                    if pathImg[i][j] == 0:
                        expr_A = Bool(Agents[currentAgent] + "_t" + str(timestep) + "_x" + str(i) + "_y" + str(j))
                        expr_B = []
                        expr_B.append(Bool(
                            Agents[currentAgent] + "_t" + str(timestep + 1) + "_x" + str(i) + "_y" + str(
                                j)))  # current vertex
                        if i >= 1 and j >= 1 and pathImg[i - 1][j - 1] == 0:  # 左上
                            expr_B.append(
                                Bool(Agents[currentAgent] + "_t" + str(timestep + 1) + "_x" + str(i - 1) + "_y" + str(
                                    j - 1)))
                        if j >= 1 and pathImg[i][j - 1] == 0:  # 左
                            expr_B.append(
                                Bool(Agents[currentAgent] + "_t" + str(timestep + 1) + "_x" + str(i) + "_y" + str(
                                    j - 1)))
                        if i <= rows - 2 and j >= 1 and pathImg[i + 1][j - 1] == 0:  # 左下
                            expr_B.append(
                                Bool(Agents[currentAgent] + "_t" + str(timestep + 1) + "_x" + str(i + 1) + "_y" + str(
                                    j - 1)))
                        if i >= 1 and pathImg[i - 1][j] == 0:  # 上
                            expr_B.append(
                                Bool(Agents[currentAgent] + "_t" + str(timestep + 1) + "_x" + str(i - 1) + "_y" + str(
                                    j)))
                        if i <= rows - 2 and pathImg[i + 1][j] == 0:  # 下
                            expr_B.append(
                                Bool(Agents[currentAgent] + "_t" + str(timestep + 1) + "_x" + str(i + 1) + "_y" + str(
                                    j)))
                        if i >= 1 and j <= cols - 2 and pathImg[i - 1][j + 1] == 0:  # 右上
                            expr_B.append(
                                Bool(Agents[currentAgent] + "_t" + str(timestep + 1) + "_x" + str(i - 1) + "_y" + str(
                                    j + 1)))
                        if j <= cols - 2 and pathImg[i][j + 1] == 0:  # 右
                            expr_B.append(
                                Bool(Agents[currentAgent] + "_t" + str(timestep + 1) + "_x" + str(i) + "_y" + str(
                                    j + 1)))
                        if i <= rows - 2 and j <= cols - 2 and pathImg[i + 1][j + 1] == 0:  # 右下
                            expr_B.append(
                                Bool(Agents[currentAgent] + "_t" + str(timestep + 1) + "_x" + str(i + 1) + "_y" + str(
                                    j + 1)))
                        solver1.add(Or(Not(expr_A), Or(expr_B)))

                        expr_C = []
                        expr_D = []
                        for a1 in range(len(Agents)):
                            if a1 not in earlyPathAgentList:
                                if a1 != currentAgent:
                                    expr_C.append(
                                        Bool(Agents[a1] + "_t" + str(timestep) + "_x" + str(i) + "_y" + str(j)))
                                    expr_D.append(
                                        Bool(Agents[a1] + "_t" + str(timestep + 1) + "_x" + str(i) + "_y" + str(j)))

                        # 每个位置每次只能有一个Agent
                        solver1.add(Not(And(expr_A, Or(expr_C))))
                        # 多个agent不能同一时间进出一个vertex
                        solver1.add(Not(And(expr_A, Or(expr_D))))

    for agt in range(len(Agents)):
        if len(allPath[agt]) > timestep and (agt in earlyPathAgentList):
            for agt2 in range(len(Agents)):
                if agt2 not in earlyPathAgentList:
                    solver1.add(Not(
                        Bool(Agents[agt2] + "_t" + str(timestep) + "_x" + str(allPath[agt][timestep][0]) + "_y" + str(
                            allPath[agt][timestep][1]))))
                    solver1.add(Not(
                        Bool(Agents[agt2] + "_t" + str(timestep + 1) + "_x" + str(
                            allPath[agt][timestep][0]) + "_y" + str(
                            allPath[agt][timestep][1]))))

    if timestep > minDistance():  # 当步骤大于图中起点和终点最近的agent
        solver1.push()
        for agt in range(agentsNum):
            if agt not in earlyPathAgentList:
                for i in range(len(pathImg)):
                    for j in range(len(pathImg[0])):
                        if pathImg[i][j] == 0:
                            if not (i == endX[agt] and j == endY[agt]):
                                solver1.add(
                                    Not(Bool(Agents[agt] + "_t" + str(timestep + 1) + "_x" + str(i) + "_y" + str(j))))
            solver1.add(Bool(Agents[agt] + "_t" + str(timestep + 1) + "_x" + str(endX[agt]) + "_y" + str(endY[agt])))
        isSat = solver1.check()
        solver1.pop()

    dur = time() - starttime
    print "第", timestep, "次", isSat, "\ttime:", ('%0.6f秒' % dur)

    timestep = timestep + 1

pathPlan = [["" for mm in range(cols)] for nn in range(rows)]
pattern_Agent = re.compile(r'(.+?)_t')  # 匹配“B_t9_x8_y8”中的"A"
pattern_sub = re.compile(r't_[*]')  # 匹配除agent外的字符
pattern_T_X_Y = re.compile(r'\d+')  # 匹配“B_t9_x8_y8”中的"9 8 8"三个数字
for n in range(len(solver1.model())):
    a = Bool(str(solver1.model()[n]))
    if (solver1.model().evaluate(a) == True):
        f.write(str(solver1.model()[n]) + " " + str(solver1.model().evaluate(a)) + "\n")
        string = str(solver1.model()[n])
        AgentName = str(pattern_Agent.findall(string)[0])
        T_X_Y = pattern_T_X_Y.findall(str(re.findall(r"[A-Za-z0-9]+(.+)", string)))
        # print len(pathPlan)," ",len(pathPlan[0])," ",len(pathPlan[0][0])
        pathPlan[int(T_X_Y[1])][int(T_X_Y[2])] = str(pathPlan[int(T_X_Y[1])][int(T_X_Y[2])]) + str(
            AgentName) + "_" + str(T_X_Y[0]) + ","

# f.write(str(solver1.model()))

f.close()

print pathPlan

# 写入ｅｘｃｅｌ中
file_excel = '/home/dzhb/Documents/MultiAgents_totalSat(Astar).xlsx'
newfile = xlwt.Workbook()
newSheet = newfile.add_sheet('Simple', cell_overwrite_ok=True)
style1 = xlwt.easyxf('pattern: pattern solid, fore_colour black;')
style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white;')
for i in range(rows):
    for j in range(cols):
        if (pathImg[i][j] != VERTEX):
            newSheet.write(i, j, 1, style1)
        else:
            newSheet.write(i, j, pathPlan[i][j], style2)

newfile.save(file_excel)

list = []
with open('test.txt', 'r') as f:
    for line in f:
        list.append(line.strip())

with open("gym_done.txt", "w") as f:
    for item in sorted(list):
        f.writelines(item)
        f.writelines('\n')
    f.close()

print "Finish!"
