# coding=UTF-8
from z3 import *
import datetime
import cv2

s = Solver()

# s1 = BitVec("s1",1)
# s2 = BitVec("s2",1)
# s3 = BitVec("s3",1)
# s4 = BitVec("s4",1)
# s5 = BitVec("s5",1)
# s6 = BitVec("s6",1)

# def getRound(x,y,direction):
#     if direction == "TL":
#         return 10 * x
starttime = datetime.datetime.now()



# M = AstMap()
def findPath(tt, startX, startY, path):
    i = startX
    j = startY
    if (s.model().evaluate(Bool("t" + str(tt) + "_x" + str(i) + "_y" + str(j))) == True):
        print "t" + str(tt) + "_x" + str(i) + "_y" + str(j) + " " + str(
            s.model().evaluate(Bool("t" + str(tt) + "_x" + str(i) + "_y" + str(j)))) + "\n"
        path.append([i, j])
        if i >= 1 and j >= 1 and s.model().evaluate(
                Bool("t" + str(tt + 1) + "_x" + str(i - 1) + "_y" + str(j - 1))) == True:  # 左上
            findPath(tt + 1, i - 1, j - 1, path)
        elif j >= 1 and s.model().evaluate(
                Bool("t" + str(tt + 1) + "_x" + str(i) + "_y" + str(j - 1))) == True:  # 左
            findPath(tt + 1, i, j - 1, path)
        elif i <= rows - 2 and j >= 1 and s.model().evaluate(
                Bool("t" + str(tt + 1) + "_x" + str(i + 1) + "_y" + str(j - 1))) == True:  # 左下
            findPath(tt + 1, i + 1, j - 1, path)
        elif i >= 1 and s.model().evaluate(
                Bool("t" + str(tt + 1) + "_x" + str(i - 1) + "_y" + str(j))) == True:  # 上
            findPath(tt + 1, i - 1, j, path)
        elif i <= rows - 2 and s.model().evaluate(
                Bool("t" + str(tt + 1) + "_x" + str(i + 1) + "_y" + str(j))) == True:  # 下
            findPath(tt + 1, i + 1, j, path)
        elif i >= 1 and j <= cols - 2 and s.model().evaluate(
                Bool("t" + str(tt + 1) + "_x" + str(i - 1) + "_y" + str(j + 1))) == True:  # 右上
            findPath(tt + 1, i - 1, j + 1, path)
        elif j <= cols - 2 and s.model().evaluate(
                Bool("t" + str(tt + 1) + "_x" + str(i) + "_y" + str(j + 1))) == True:  # 右
            findPath(tt + 1, i, j + 1, path)
        elif i <= rows - 2 and j <= cols - 2 and s.model().evaluate(
                Bool("t" + str(tt + 1) + "_x" + str(i + 1) + "_y" + str(j + 1))) == True:  # 右下
            findPath(tt + 1, i + 1, j + 1, path)


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

# pathImg = []
# for p in range(29):
#     W = []
#     for q in range(29):
#         W.append(0)
#     pathImg.append(W)

# pathImg = [
#     [0, 0, 1, 1],
#     [0, 0, 1, 1],
#     [1, 0, 1, 1],
#     [1, 0, 0, 0],
# ]
rows = len(pathImg)
cols = len(pathImg[0])
f = open('test.txt', 'w')

# try:
start_X = 0
start_Y = 0

end_X = 28
end_Y = 28

path = []

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
                # T.append(Or(Not(expr_A), Or(expr_B)))
    # for ss in S: T.append(ss)
    T.append(And(S))
    s.add(And(T))

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
        findPath(0, start_X, start_Y, path)
        # for b in range(len(path)):
        #     f.write("X_"+str(path[b][0])+"_Y_"+str(path[b][1])+"\n")
        endtime = datetime.datetime.now()
        print (endtime - starttime).seconds, "秒"
        # f.write(str(s))

    t = t + 1
    s.reset()

# while isSat == sat:
#
#     m = []
#     f.write("解：" + str() + "\n")
#     for n in range(len(s.model())):
#         a = Bool(str(s.model()[n]))
#         if (s.model().evaluate(a) == True):
#             f.write(str(s.model()[n]) + " " + str(s.model().evaluate(a)) + "\n")
#             m.append(a)
#     s.add(Not(And(m)))
#     isSat = s.check()

f.close()

# except Exception as e:
#     print "faild:",e

# ---------------------------------------------------------------------


# for t in range(22):
#     for i in range(len(pathImg)):
#         for j in range(len(pathImg[0])):
#             exprs.push(Bool("t"+str(t)+"_x" + str(i) + "_y" + str(j)))
#
# T = []
# for t in range(22):
#     S = []
#     for i in range(len(pathImg)):
#         for j in range(len(pathImg[0])):
#             # s.add(exprs[10 * i + j])
#             if pathImg[i][j] == 0:
#                 # print("to:",i,"_",j)
#                 expr_A = exprs[10 * i + j]
#                 expr_B = []
#                 if i >= 1 and j >= 1 and pathImg[i-1][j-1] == 0:  # 左上
#                     expr_B.append(exprs[t * 100 +10 * (i - 1) + j - 1])
#                 if j >= 1 and pathImg[i][j-1] == 0:  # 左
#                     expr_B.append(exprs[t * 100 +10 * i + j - 1])
#                 if i <= 8 and j >= 1 and pathImg[i+1][j-1] == 0:  # 左下
#                     expr_B.append(exprs[t * 100 +10 * (i + 1) + j - 1])
#                 if i >= 1 and pathImg[i-1][j] == 0:  # 上
#                     expr_B.append(exprs[t * 100 +10 * (i - 1) + j])
#                 if i <= 8 and pathImg[i+1][j] == 0:  # 下
#                     expr_B.append(exprs[t * 100 +10 * (i + 1) + j])
#                 if i >= 1 and j <= 8 and pathImg[i-1][j+1] == 0:  # 右上
#                     expr_B.append(exprs[t * 100 +10 * (i - 1) + j + 1])
#                 if j <= 8 and pathImg[i][j+1] == 0:  # 右
#                     expr_B.append(exprs[t * 100 +10 * i+ j + 1])
#                 if i <= 8 and j <= 8 and pathImg[i+1][j+1] == 0:  # 右下
#                     expr_B.append(exprs[t * 100 +10 * (i + 1) + j + 1])
#                 # s.add(Or(Not(expr_A),Or(expr_B)))
#                 S.append(Or(Not(expr_A),Or(expr_B)))
#     T.append(Or(S))
#
# s.add(And(T))
# s.add(exprs[0])
# s.add(exprs[2199])


try:
    # s.add(s1 & (s2 | s4) == 1)
    # s.add(s2 & (s1 | s3 | s4 | s5) == 1)
    # s.add(s3 & (s2 | s4 | s5) == 1)
    # s.add(s4 & (s1 | s2 | s3 | s5 | s6) == 1)
    # s.add(s5 & (s2 | s3 | s4 | s6) == 1)
    # s.add(s6 & (s4 | s5) == 1)

    # s1 = Bool("s1")
    # s2 = Bool("s2")
    # s3 = Bool("s3")
    # s4 = Bool("s4")
    # s5 = Bool("s5")
    # s6 = Bool("s6")
    # s7 = Bool("s7")
    # s8 = Bool("s8")
    # s9 = Bool("s9")
    # s10 = Bool("s10")
    # s11 = Bool("s11")
    # s12 = Bool("s12")
    # s13 = Bool("s13")
    # s14 = Bool("s14")
    # s15 = Bool("s15")

    # s.add(Or(Not(s1),Or(s2,s4)))
    # s.add(Or(Not(s2),Or(s1,s3,s4)))
    # s.add(Or(Not(s3),Or(s2,s4,s5)))
    # s.add(Or(Not(s4),Or(s1,s2,s3,s5,s6)))
    # s.add(Or(Not(s5),Or(s2,s3,s4,s6)))
    # s.add(Or(Not(s6),Or(s4,s5)))

    # s.add(And(Or(Not(s1),Or(s2,s5)),Or(s1,Not(Or(s2,s5)))))
    # s.add(And(Or(Not(s2),Or(s1,s3,s5)),Or(s2,Not(Or(s1,s3,s5)))))
    # s.add(And(Or(Not(s3),Or(s2,s4,s6)),Or(s3,Not(Or(s2,s4,s6)))))
    # s.add(And(Or(Not(s4),Or(s3,s7)),Or(s4,Not(Or(s3,s7)))))
    # s.add(And(Or(Not(s5),Or(s1,s2,s6,s8)),Or(s5,Not(Or(s1,s2,s6,s8)))))
    # s.add(And(Or(Not(s6),Or(s3,s5,s7,s8)),Or(s6,Not(Or(s3,s5,s7,s8)))))
    # s.add(And(Or(Not(s7),Or(s4,s6,s9)),Or(s7,Not(Or(s4,s6,s9)))))
    # s.add(And(Or(Not(s8),Or(s5,s6,s9,s10)),Or(s8,Not(Or(s5,s6,s9,s10)))))
    # s.add(And(Or(Not(s9),Or(s10,s7,s8)),Or(s9,Not(Or(s10,s7,s8)))))
    # s.add(And(Or(Not(s10),Or(s9,s8)),Or(s10,Not(Or(s9,s8)))))

    #
    # s.add(Or(Not(s1),Or(s2,s5)))
    # s.add(Or(Not(s2),Or(s1,s3,s5)))
    # s.add(Or(Not(s3),Or(s2,s4,s6)))
    # s.add(Or(Not(s4),Or(s3,s7,s11)))
    # s.add(Or(Not(s5),Or(s1,s2,s6,s8)))
    # s.add(Or(Not(s6),Or(s3,s5,s7,s8)))
    # s.add(Or(Not(s7),Or(s4,s6,s9,s12)))
    # s.add(Or(Not(s8),Or(s5,s6,s9,s10)))
    # s.add(Or(Not(s9),Or(s7,s8,s10,s13)))
    # s.add(Or(Not(s10),Or(s9,s8,s14,s15)))
    # s.add(Or(Not(s11),Or(s4,s7,s12)))
    # s.add(Or(Not(s12),Or(s11,s7,s13)))
    # s.add(Or(Not(s13),Or(s9,s12,s14)))
    # s.add(Or(Not(s14),Or(s10,s13,s15)))
    # s.add(Or(Not(s15),Or(s10,s14)))
    # # #
    # # #
    # s.add(Or(Not(s1),s15))
    # s.add(s15)
    # s.add(s1)

    # times = 0
    T = []
    # while times < 10:
    #     S = []
    #     S.append(Or(Not(Bool("t"+str(times)+"_s1")),Or(Bool("t"+str(times+1)+"_s2"),Bool("t"+str(times+1)+"_s5"))))
    #     S.append(Or(Not(Bool("t"+str(times)+"_s2")),Or(Bool("t"+str(times+1)+"_s1"),Bool("t"+str(times+1)+"_s3"),Bool("t"+str(times+1)+"_s5"))))
    #     S.append(Or(Not(Bool("t"+str(times)+"_s3")),Or(Bool("t"+str(times+1)+"_s2"),Bool("t"+str(times+1)+"_s4"),Bool("t"+str(times+1)+"_s6"))))
    #     S.append(Or(Not(Bool("t"+str(times)+"_s4")),Or(Bool("t"+str(times+1)+"_s3"),Bool("t"+str(times+1)+"_s7"))))
    #     S.append(Or(Not(Bool("t"+str(times)+"_s5")),Or(Bool("t"+str(times+1)+"_s1"),Bool("t"+str(times+1)+"_s2"),Bool("t"+str(times+1)+"_s6"),Bool("t"+str(times+1)+"_s8"))))
    #     S.append(Or(Not(Bool("t"+str(times)+"_s6")),Or(Bool("t"+str(times+1)+"_s3"),Bool("t"+str(times+1)+"_s5"),Bool("t"+str(times+1)+"_s7"),Bool("t"+str(times+1)+"_s8"))))
    #     S.append(Or(Not(Bool("t"+str(times)+"_s7")),Or(Bool("t"+str(times+1)+"_s4"),Bool("t"+str(times+1)+"_s6"),Bool("t"+str(times+1)+"_s9"))))
    #     S.append(Or(Not(Bool("t"+str(times)+"_s8")),Or(Bool("t"+str(times+1)+"_s5"),Bool("t"+str(times+1)+"_s6"),Bool("t"+str(times+1)+"_s9"),Bool("t"+str(times+1)+"_s10"))))
    #     S.append(Or(Not(Bool("t"+str(times)+"_s9")),Or(Bool("t"+str(times+1)+"_s7"),Bool("t"+str(times+1)+"_s8"),Bool("t"+str(times+1)+"_s10"))))
    #     S.append(Or(Not(Bool("t"+str(times)+"_s10")),Or(Bool("t"+str(times+1)+"_s8"),Bool("t"+str(times+1)+"_s9"))))
    #     s.add(Or(S))
    # s.check()

    # while s.check():
    #     m = s.model()
    #     print m
    #     s.add(Not(And(s1==m[s1],s2==m[s2],s3==m[s3],s4==m[s4],s5==m[s5],s6==m[s6],s7==m[s7],s8==m[s8],s9==m[s9],s10==m[s10])))

    # print(s.check())
    # a = Bool("t0_x0_y0")
    # print s.model()

    # f = open('test.txt', 'w')
    # for n in range(len(s.model())):
    #     a = Bool(str(s.model()[n]))
    #     if (s.model().evaluate(a) == True):
    #         f.write(str(s.model()[n]) + " " + str(s.model().evaluate(a)) + "\n")
    # f.close()



except Exception as e:
    print("faild:", e)
