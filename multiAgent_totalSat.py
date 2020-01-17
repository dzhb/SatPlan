# coding=UTF-8
# SAT多机路径规划
import re
from z3 import *
import datetime
import xlrd
import xlwt
import numpy


solver1 = Solver()
# －－－－－－－－－－－－－－－－－－－－－－－－测试数据１－－－－－－－－－－－－－－－－－－－－－
pathImg = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
]
Agents = ["A","B","C"]
startX = [0, 1,1]  # Ｘ轴坐标
startY = [0, 0,1]

endX = [8,9,9]
endY = [8,9,8]
# ---------------------------------------------------------------------------------

# －－－－－－－－－－－－－－－－－－－－－－－－测试数据2－－－－－－－－－－－－－－－－－－－－－

pathImg = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
]
Agents = ["A", "B", "C", "D", "E"]  # 表示机器人
startX = [0, 1, 0, 0, 5]  # Ｘ轴坐标
startY = [0, 0, 1, 2, 2]

endX = [28, 28, 27, 26, 25]
endY = [28, 27, 28, 26, 28]

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

def minDistance():
    min = 0
    for agt in range(agentsNum):
        distance = int(math.sqrt(abs(math.pow((endX[agt] - startX[agt]), 2) + math.pow((endY[agt] - startY[agt]), 2)))) - 1
        if min < distance:
            min = distance
    return min


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
pattern_Agent = re.compile(r'[A-Z]') #匹配“B_t9_x8_y8”中的"A"
pattern_T_X_Y = re.compile(r'\d+') #匹配“B_t9_x8_y8”中的"9 8 8"三个数字
for n in range(len(solver1.model())):
    a = Bool(str(solver1.model()[n]))
    if (solver1.model().evaluate(a) == True):
        f.write(str(solver1.model()[n]) + " " + str(solver1.model().evaluate(a)) + "\n")
        string = str(solver1.model()[n])
        AgentName = str(pattern_Agent.findall(string)[0])
        T_X_Y = pattern_T_X_Y.findall(string)
        # print len(pathPlan)," ",len(pathPlan[0])," ",len(pathPlan[0][0])
        pathPlan[int(T_X_Y[1])][int(T_X_Y[2])] = str(pathPlan[int(T_X_Y[1])][int(T_X_Y[2])]) + str(AgentName) + str(T_X_Y[0]) + ","


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
        if (pathImg[i][j] == 1):
            newSheet.write(i, j, 1, style1)
        else:
            newSheet.write(i, j, pathPlan[i][j], style2)

newfile.save(file_excel)


