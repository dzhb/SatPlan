# coding=UTF-8
from z3 import *
import datetime


s = Solver()


starttime = datetime.datetime.now()

pathImg = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
]
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

start_X = 0
start_Y = 0

end_X = 28
end_Y = 28

distance = int(math.sqrt(abs(math.pow((end_X - start_X),2) + math.pow((end_Y-start_Y),2))))-1

pointNum = 0 #记录vectex数量

t = 0

isSat = unsat
while isSat == unsat:
    S = []
    for i in range(len(pathImg)):
        for j in range(len(pathImg[0])):
            if pathImg[i][j] == 0:
                if t == 0:
                    pointNum = pointNum + 1
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
                s.add(Or(Not(expr_A), Or(expr_B)))


    if (t >= distance):
        s.push()
        startP = Bool("t" + str(0) + "_x" + str(start_X) + "_y" + str(start_X))
        endP = Bool("t" + str(t) + "_x" + str(end_X) + "_y" + str(end_Y))
        s.add(startP)
        s.add(endP)

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

            endtime = datetime.datetime.now()
            print (endtime - starttime).seconds, "秒"

        s.pop()
    t = t + 1
    if(t > pointNum):
        print "无解！！！"
        break


f.close()


