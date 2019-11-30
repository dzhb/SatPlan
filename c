# coding=UTF-8
from z3 import *
import datetime
import cv2

s = Solver()


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

rows = len(pathImg)
cols = len(pathImg[0])
f = open('test.txt', 'w')

# try:
start_X = 0
start_Y = 0

end_X = 28
end_Y = 28

path = []
s.push()

f = open('test.txt', 'w')
t = 0
T = []
isSat = unsat
while isSat == unsat:
    S = []
    for i in range(len(pathImg)):
        for j in range(len(pathImg[0])):
            if pathImg[i][j] == 0:
                expr_A = Bool("t" + str(t) + "_x" + str(i) + "_y" + str(j))
                expr_B = []
                if i >= 1 and j >= 1 and pathImg[i - 1][j - 1] == 0:  # 左上
                    expr_B.append(Bool("t" + str(t + 1) + "_x" + str(i - 1) + "_y" + str(j - 1)))
                if j >= 1 and pathImg[i][j - 1] == 0:  # 左
                    expr_B.append(Bool("t" + str(t + 1) + "_x" + str(i) + "_y" + str(j - 1)))
                if i <= rows - 2 and j >= 1 and pathImg[i + 1][j - 1] == 0:  # 左下
                    expr_B.append(Bool("t" + str(t + 1) + "_x" + str(i + 1) + "_y" + str(j - 1)))
                if i >= 1 and pathImg[i - 1][j] == 0:  # 上
                    expr_B.append(Bool("t" + str(t + 1) + "_x" + str(i - 1) + "_y" + str(j)))
                if i <= rows - 2 and pathImg[i + 1][j] == 0:  # 下
                    expr_B.append(Bool("t" + str(t + 1) + "_x" + str(i + 1) + "_y" + str(j)))
                if i >= 1 and j <= cols - 2 and pathImg[i - 1][j + 1] == 0:  # 右上
                    expr_B.append(Bool("t" + str(t + 1) + "_x" + str(i - 1) + "_y" + str(j + 1)))
                if j <= cols - 2 and pathImg[i][j + 1] == 0:  # 右
                    expr_B.append(Bool("t" + str(t + 1) + "_x" + str(i) + "_y" + str(j + 1)))
                if i <= rows - 2 and j <= cols - 2 and pathImg[i + 1][j + 1] == 0:  # 右下
                    expr_B.append(Bool("t" + str(t + 1) + "_x" + str(i + 1) + "_y" + str(j + 1)))
                expr_B.append(Bool("t" + str(t + 1) + "_x" + str(i) + "_y" + str(j)))
                S.append(Or(Not(expr_A), Or(expr_B)))
    s.add(And(S))
    s.push()
    startP = Bool("t" + str(0) + "_x" + str(start_X) + "_y" + str(start_X))
    endP = Bool("t" + str(t) + "_x" + str(end_X) + "_y" + str(end_Y))
    s.add(startP)
    s.add(endP)
    # s.add(Or(Not(startP),endP))
    for i in range(len(pathImg)):
        for j in range(len(pathImg[0])):
            if pathImg[i][j] == 0:
                if not (i == end_X and j == end_Y):
                    s.add(Not(Bool("t" + str(t + 1) + "_x" + str(i) + "_y" + str(j))))

    isSat = s.check()
    print "第" + str(t) + "步的解：", isSat
    if isSat == sat:
        f.write("第" + str(t) + "步的解：" + str() + "\n")
        for n in range(len(s.model())):
            a = Bool(str(s.model()[n]))
            if (s.model().evaluate(a) == True):
                f.write(str(s.model()[n]) + " " + str(s.model().evaluate(a)) + "\n")
        # print s
        # findPath(0, start_X, start_Y, path)
        # for b in range(len(path)):
        #     f.write("X_"+str(path[b][0])+"_Y_"+str(path[b][1])+"\n")
        endtime = datetime.datetime.now()
        print (endtime - starttime).seconds, "秒"
        # f.write(str(s))

    t = t + 1
    s.pop()

f.close()
