# coding=UTF-8
# SAT多机路径规划
import re
from z3 import *
import datetime
import xlrd
import xlwt
import numpy


solver1 = Solver()
# －－－－－－－－－－－－－－－－－－－－－－－－测试数据１_10x10－－－－－－－－－－－－－－－－－－－－－
# pathImg = [
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
#     [1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
#     [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
#     [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
#     [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
# ]
# Agents = ["A","B","C","D","E"]
# startX = [0, 1,1,0,2]  # Ｘ轴坐标
# startY = [0, 0,1,1,1]
#
# endX = [8,9,9,7,8]
# endY = [8,9,8,7,7]
# ---------------------------------------------------------------------------------
# －－－－－－－－－－－－－－－－－－－－－－－－测试数据１_10x10－－－－－－－－－－－－－－－－－－－－－
# pathImg = [
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
# ---------------------------------------------------------------------------------
pathImg = []
for x in range(18):
    pathImg2 = []
    for y in range(18):
        pathImg2.append(0)
    pathImg.append(pathImg2)

Agents = []
startX = []  # Ｘ轴坐标
startY = []
endX = []
endY = []

for agt in range(18):
    Agents.append("A"+str(agt))
    startX.append(0)
    startY.append(agt)
    endX.append(16)
    endY.append(agt)

    Agents.append("B"+str(agt))
    startX.append(1)
    startY.append(agt)
    endX.append(17)
    endY.append(agt)

# －－－－－－－－－－－－－－－－－－－－－－－－测试数据3_29x29－－－－－－－－－－－－－－－－－－－－

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
# startX = [0, 1, 0, 0, 5]  # Ｘ轴坐标
# startY = [0, 0, 1, 2, 2]
#
# endX = [28, 28, 27, 26, 25]
# endY = [28, 27, 28, 26, 28]

# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# －－－－－－－－－－－－－－－－－－－－－测试数据３－－－－－－－－－－－－－－－－－－－－－－－－－－－

# import numpy as np
# f = open(r"ost003d.map")
# line = f.readline()
# data_list = []
# while line:
#     num = list(map(str,line.split()))
#     data_list.append(num)
#     line = f.readline()
# f.close()
# pathImg = np.array(data_list)
#
# Agents = ["A"]  # 表示机器人
# startX = [143, 1, 0, 0, 5]  # Ｘ轴坐标
# startY = [40, 0, 1, 2, 2]
#
# endX = [191, 28, 27, 26, 25]
# endY = [111, 27, 28, 26, 28]
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# pathImg = []
# for p in range(64):
#     W = []
#     for q in range(64):
#         W.append(0)
#     pathImg.append(W)
#
# Agents = []
# startX = []
# startY = []
# endX = []
# endY = []
# rows = len(pathImg)     #行数
# cols = len(pathImg[0])  #列数
# for v in range(200):
#     Agents.append("A"+str(v))
#
# for x in range(54):
#     for y in range(54):
#         if(x % 4 == 0 and y % 3 == 0):
#             startX.append(x)
#             startY.append(y)
#             endX.append(rows-x)
#             endY.append(cols-y)
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
pathImg = []
for x in range(3):
    pathImg2 = []
    for y in range(3):
        pathImg2.append(0)
    pathImg.append(pathImg2)

Agents = []
startX = []  # Ｘ轴坐标
startY = []
endX = []
endY = []

for agt in range(3):
    Agents.append("A"+str(agt))
    startX.append(0)
    startY.append(agt)
    endX.append(0)
    endY.append(agt)

    Agents.append("B"+str(agt))
    startX.append(1)
    startY.append(agt)
    endX.append(1)
    endY.append(agt)

for agt in range(2):
    Agents.append("C"+str(agt))
    startX.append(2)
    startY.append(agt)
    endX.append(2)
    endY.append(agt)

endX[0] = 2
endY[0] = 2

# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－


rows = len(pathImg)     #行数
cols = len(pathImg[0])  #列数

f = open('test.txt', 'w')

agentsNum = len(Agents)
t = 0  # 记录时间
currentAgent = 0  # 当前agent
isSat = unsat
constrainstsArr = []  # 约束
starttime = datetime.datetime.now() #　计时

VECTEX = 0 #途中表示顶点的字符

# 起点终点最短距离
def minDistance():
    min = 0
    for agt in range(agentsNum):
        distance = int(math.sqrt(abs(math.pow((endX[agt] - startX[agt]), 2) + math.pow((endY[agt] - startY[agt]), 2)))) - 1
        if min < distance:
            min = distance
    return min

for agt in range(agentsNum):
    if(pathImg[startX[agt]][startY[agt]] != VECTEX):
        print "agent的起点不能为障碍物"
        exit()
    if (pathImg[endX[agt]][endY[agt]] != VECTEX):
        print "agent的终点不能为障碍物"
        exit()

for agt in range(agentsNum):
    for agt2 in range(agt+1,agentsNum):
        if(startX[agt] == startX[agt2] and startY[agt] == startY[agt2]):
            print "Agent",Agents[agt],"与Agent",Agents[agt2],"所在起点冲突"
            exit()
        if(endX[agt] == endX[agt2] and endY[agt] == endY[agt2]):
            print "Agent",Agents[agt],"与Agent",Agents[agt2],"所在终点冲突"
            exit()

# init first vectex for per agent
for p in range(len(Agents)):
    solver1.append(Bool(Agents[p] + "_t" + str(t) + "_x" + str(startX[p]) + "_y" + str(startY[p])))

while isSat == unsat:
    for currentAgent in range(len(Agents)):
        for i in range(rows):
            for j in range(cols):
                if pathImg[i][j] == 0:
                    expr_A = Bool(Agents[currentAgent] + "_t" + str(t) + "_x" + str(i) + "_y" + str(j))
                    expr_B = []
                    if i >= 1 and j >= 1 and pathImg[i - 1][j - 1] == 0:  # 左上
                        expr_B.append(
                            Bool(Agents[currentAgent] + "_t" + str(t + 1) + "_x" + str(i - 1) + "_y" + str(j - 1)))
                    if j >= 1 and pathImg[i][j - 1] == 0:  # 左
                        expr_B.append(Bool(Agents[currentAgent] + "_t" + str(t + 1) + "_x" + str(i) + "_y" + str(j - 1)))
                    if i <= rows - 2 and j >= 1 and pathImg[i + 1][j - 1] == 0:  # 左下
                        expr_B.append(
                            Bool(Agents[currentAgent] + "_t" + str(t + 1) +  "_x" + str(i + 1) + "_y" + str(j - 1)))
                    if i >= 1 and pathImg[i - 1][j] == 0:  # 上
                        expr_B.append(Bool(Agents[currentAgent] + "_t" + str(t + 1) + "_x" + str(i - 1) + "_y" + str(j)))
                    if i <= rows - 2 and pathImg[i + 1][j] == 0:  # 下
                        expr_B.append(Bool(Agents[currentAgent] + "_t" + str(t + 1) + "_x" + str(i + 1) + "_y" + str(j)))
                    if i >= 1 and j <= cols - 2 and pathImg[i - 1][j + 1] == 0:  # 右上
                        expr_B.append(
                            Bool(Agents[currentAgent] + "_t" + str(t + 1) + "_x" + str(i - 1) + "_y" + str(j + 1)))
                    if j <= cols - 2 and pathImg[i][j + 1] == 0:  # 右
                        expr_B.append(Bool(Agents[currentAgent] + "_t" + str(t + 1) + "_x" + str(i) + "_y" + str(j + 1)))
                    if i <= rows - 2 and j <= cols - 2 and pathImg[i + 1][j + 1] == 0:  # 右下
                        expr_B.append(
                            Bool(Agents[currentAgent] + "_t" + str(t + 1) + "_x" + str(i + 1) + "_y" + str(j + 1)))
                    expr_B.append(Bool(Agents[currentAgent] + "_t" + str(t + 1) + "_x" + str(i) + "_y" + str(j))) #current vectex
                    solver1.add(Or(Not(expr_A), Or(expr_B)))

                    expr_C = []
                    expr_D = []
                    for a1 in range(len(Agents)):
                        if a1 != currentAgent:
                            expr_C.append(Bool(Agents[a1] + "_t" + str(t) + "_x" + str(i) + "_y" + str(j)))
                            expr_D.append(Bool(Agents[a1] + "_t" + str(t+1) + "_x" + str(i) + "_y" + str(j)))
                    # 每个位置每次只能有一个Agent
                    solver1.add(Not(And(expr_A,Or(expr_C))))
                    # 多个agent不能同一时间进出一个vectex
                    solver1.add(Not(And(expr_A,Or(expr_D))))

    if t > minDistance(): # 当步骤大于图中起点和终点最近的agent
        solver1.push()
        for agt in range(agentsNum):
            for i in range(len(pathImg)):
                for j in range(len(pathImg[0])):
                    if pathImg[i][j] == 0:
                        if not (i == endX[agt] and j == endY[agt]):
                            solver1.add(Not(Bool(Agents[agt] + "_t" + str(t + 1) + "_x" + str(i) + "_y" + str(j))))
            solver1.add(Bool(Agents[agt] + "_t" + str(t + 1) + "_x" + str(endX[agt]) + "_y" + str(endY[agt])))
        isSat = solver1.check()
        solver1.pop()

    endtime = datetime.datetime.now()
    print "第",t,"次",isSat,"\ttime:",(endtime - starttime).seconds,"秒"
    t = t + 1



pathPlan = [["" for mm in range(cols)] for nn in range(rows)]
pattern_Agent = re.compile(r'(.+?)_t') #匹配“B_t9_x8_y8”中的"A"
pattern_sub = re.compile(r't_[*]') #匹配除agent外的字符
pattern_T_X_Y = re.compile(r'\d+') #匹配“B_t9_x8_y8”中的"9 8 8"三个数字
for n in range(len(solver1.model())):
    a = Bool(str(solver1.model()[n]))
    if (solver1.model().evaluate(a) == True):
        f.write(str(solver1.model()[n]) + " " + str(solver1.model().evaluate(a)) + "\n")
        string = str(solver1.model()[n])
        AgentName = str(pattern_Agent.findall(string)[0])
        T_X_Y = pattern_T_X_Y.findall(str(re.findall(r"[A-Za-z0-9]+(.+)",string)))
        # print len(pathPlan)," ",len(pathPlan[0])," ",len(pathPlan[0][0])
        pathPlan[int(T_X_Y[1])][int(T_X_Y[2])] = str(pathPlan[int(T_X_Y[1])][int(T_X_Y[2])]) + str(AgentName) + "_" + str(T_X_Y[0]) + ","

# f.write(str(solver1.model()))

f.close()

print pathPlan

# 写入ｅｘｃｅｌ中
file_excel = '/home/dzhb/Documents/MultiAgents_totalSat.xlsx'
newfile = xlwt.Workbook()
newSheet = newfile.add_sheet('Simple', cell_overwrite_ok=True)
style1 = xlwt.easyxf('pattern: pattern solid, fore_colour black;')
style2 = xlwt.easyxf('pattern: pattern solid, fore_colour white;')
for i in range(rows):
    for j in range(cols):
        if (pathImg[i][j] != VECTEX):
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



