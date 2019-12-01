# coding=UTF-8
import re
from z3 import *
import xlrd
import xlwt
import datetime

from xlutils.copy import copy

file = '/home/dzhb/Documents/AgentsABC.xlsx'

newfile = xlwt.Workbook()
newSheet = newfile.add_sheet('Simple', cell_overwrite_ok=True)

starttime = datetime.datetime.now()

s = Solver()

pathImg = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
]
# pathImg = [
#     [0, 0, 1, 1],
#     [0, 0, 1, 1],
#     [1, 0, 1, 1],
#     [1, 0, 0, 0],
# ]
pathImg = [
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
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
rows = len(pathImg)
cols = len(pathImg[0])

for i in range(rows):
    for j in range(cols):
        if (pathImg[i][j] == 1):
            newSheet.write(i, j, 1)
newfile.save(file)

f = open('test.txt', 'w')

# try:
Agents = ["A", "B", "C", "D", "E", "F", "G", "H", "I","J"]  # 表示个机器人
startX = [0, 1, 0, 0, 5, 10, 0, 15, 3, 20]  # Ｘ轴坐标
startY = [0, 0, 1, 2, 2, 7, 10, 8, 5, 8]

endX = [28, 28, 27, 26, 25, 24, 23, 25, 24, 20]
endY = [28, 27, 28, 26, 28, 28, 28, 27, 27, 28]

t = 0  # 记录时间
a = 0  # 表示第a个ａｇｅｎｔ
isSat = unsat
arr = []  # 约束

# T = []  # 所有agent的分布情况
while isSat == unsat and a < len(Agents):
    # A = []  # 每个agent的情况
    # S = []
    # while a < 2:
    for i in range(len(pathImg)):
        for j in range(len(pathImg[0])):
            if pathImg[i][j] == 0:
                expr_A = Bool("t" + str(t) + "_" + Agents[a] + "_x" + str(i) + "_y" + str(j))
                expr_B = []
                if i >= 1 and j >= 1 and pathImg[i - 1][j - 1] == 0:  # 左上
                    expr_B.append(
                        Bool("t" + str(t + 1) + "_" + Agents[a] + "_x" + str(i - 1) + "_y" + str(j - 1)))
                if j >= 1 and pathImg[i][j - 1] == 0:  # 左
                    expr_B.append(Bool("t" + str(t + 1) + "_" + Agents[a] + "_x" + str(i) + "_y" + str(j - 1)))
                if i <= rows - 2 and j >= 1 and pathImg[i + 1][j - 1] == 0:  # 左下
                    expr_B.append(
                        Bool("t" + str(t + 1) + "_" + Agents[a] + "_x" + str(i + 1) + "_y" + str(j - 1)))
                if i >= 1 and pathImg[i - 1][j] == 0:  # 上
                    expr_B.append(Bool("t" + str(t + 1) + "_" + Agents[a] + "_x" + str(i - 1) + "_y" + str(j)))
                if i <= rows - 2 and pathImg[i + 1][j] == 0:  # 下
                    expr_B.append(Bool("t" + str(t + 1) + "_" + Agents[a] + "_x" + str(i + 1) + "_y" + str(j)))
                if i >= 1 and j <= cols - 2 and pathImg[i - 1][j + 1] == 0:  # 右上
                    expr_B.append(
                        Bool("t" + str(t + 1) + "_" + Agents[a] + "_x" + str(i - 1) + "_y" + str(j + 1)))
                if j <= cols - 2 and pathImg[i][j + 1] == 0:  # 右
                    expr_B.append(Bool("t" + str(t + 1) + "_" + Agents[a] + "_x" + str(i) + "_y" + str(j + 1)))
                if i <= rows - 2 and j <= cols - 2 and pathImg[i + 1][j + 1] == 0:  # 右下
                    expr_B.append(
                        Bool("t" + str(t + 1) + "_" + Agents[a] + "_x" + str(i + 1) + "_y" + str(j + 1)))
                expr_B.append(Bool("t" + str(t + 1) + "_" + Agents[a] + "_x" + str(i) + "_y" + str(j)))
                # T.append(Or(Not(expr_A), Or(expr_B)))
                # S.append(Or(Not(expr_A), Or(expr_B)))
                s.append(Or(Not(expr_A), Or(expr_B)))

        # a = a + 1
        # T.append(And(S))

    # s.add(And(T))
    distance = abs(endX[a] - startX[a])
    if distance < abs(endY[a] - startY[a]):
        distance = abs(endY[a] - startY[a])

    if t > distance:
        s.push()

        startP = Bool("t" + str(0) + "_" + Agents[a] + "_x" + str(startX[a]) + "_y" + str(startY[a]))

        endP = Bool("t" + str(t) + "_" + Agents[a] + "_x" + str(endX[a]) + "_y" + str(endY[a]))

        # for k in range(1):
        s.add(startP)
        s.add(endP)
        for i in range(len(pathImg)):
            for j in range(len(pathImg[0])):
                if pathImg[i][j] == 0:
                    if not (i == endX[a] and j == endY[a]):
                        s.add(Not(Bool("t" + str(t + 1) + "_" + Agents[a] + "_x" + str(i) + "_y" + str(j))))
                        # print "t" + str(t + 1) + "_" + Agents[k] + "_x" + str(i) + "_y" + str(j)

        # for k in range(1,2):
        #     s.add(startP[k])
        #     s.add(endP[k])
        # for i in range(len(pathImg)):
        #     for j in range(len(pathImg[0])):
        #         if pathImg[i][j] == 0:
        #             if not (i == endX[k] and j == endY[k]):
        #                 s.add(Not(Bool("t" + str(t + 1) + "_" + Agents[k] + "_x" + str(i) + "_y" + str(j))))
        #                 print "t" + str(t + 1) + "_" + Agents[k] + "_x" + str(i) + "_y" + str(j)
        isSat = s.check()
        print "第" + str(t) + "步的解：", isSat
        if isSat == sat:
            f.write(Agents[a] + "第" + str(t) + "步的解：" + str() + "\n")
            for n in range(len(s.model())):
                ast = Bool(str(s.model()[n]))
                if (s.model().evaluate(ast) == True):
                    f.write(str(s.model()[n]) + " " + str(s.model().evaluate(ast)) + "\n")
                    if (a + 1 < len(Agents)):
                        # arr.append(Not(Bool(str(s.model()[n]).replace(Agents[a], Agents[a + 1]))))
                        # dicName = "t"+re.findall(r"t(\d+)_",str(s.model()[n]))[0] + "_x"+re.findall(r"\w_x(\d+)_",str(s.model()[n]))[0] + "_y"+ re.findall(r"\w_y(\d+)",str(s.model()[n]))[0]
                        # arr[dicName] = 1
                        arr2 = [int(re.findall(r"t(\d+)_", str(s.model()[n]))[0]),
                                int(re.findall(r"\w_x(\d+)_", str(s.model()[n]))[0]),
                                int(re.findall(r"\w_y(\d+)", str(s.model()[n]))[0])]
                        arr.append(arr2)

                        # print str(s.model()[n]).replace(Agents[a], Agents[a + 1])

            data = xlrd.open_workbook(file, formatting_info=True)
            excel = copy(wb=data)  # 完成xlrd对象向xlwt对象转换
            excel_table = excel.get_sheet(0)  # 获得要操作的页
            table = data.sheets()[0]

            oldtable = data.sheet_by_index(0)  # 通过索引获得第一页

            for tt in range(t + 1):
                for i in range(rows):
                    for j in range(cols):
                        if (s.model().evaluate(
                                Bool("t" + str(tt) + "_" + Agents[a] + "_x" + str(i) + "_y" + str(j))) == True):
                            # if tt > 0:
                            #     old = oldSheet.cell(i, j).value
                            #     newSheet.write(i, j, str(old) + Agents[a] + str(tt) + "_")
                            # else:
                            # newSheet.write(i, j, Agents[a] + str(tt) + "_")
                            excel_table.write(i, j, str(oldtable.cell(i, j).value) + Agents[a] + str(tt) + "_")

            excel.save(file)

            isSat = unsat
            s.reset()
            a = a + 1
            t = 0
            if a < len(Agents):
                for n in range(len(arr)):
                    # s.add(Not(Bool(str(arr[n]))))
                    s.add(Not(
                        Bool("t" + str(arr[n][0]) + "_" + Agents[a] + "_x" + str(arr[n][1]) + "_y" + str(arr[n][2]))))
            continue
            # print s
        s.pop()

    t = t + 1
    # s.reset()

f.close()
endtime = datetime.datetime.now()
print (endtime - starttime).seconds, "秒"
# newfile.save('/home/dzhb/Documents/AgentsABC.xlsx')

# except Exception as e:
#     print "faild:", e
