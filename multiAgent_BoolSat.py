# coding=UTF-8
from z3 import *
from time import time
import xlwt

# 将图上的每个点用数字表示并转化成bool数组表示

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
# Agents = ["A"]
# Agents = ["A","B"]
startX = [0, 1, 1, 0, 2, 3, 4, 4, 8, 9, 9, 7, 8, 8, 9]
startY = [0, 0, 1, 1, 1, 1, 1, 2, 8, 9, 8, 7, 7, 6, 7]

endX = [8, 9, 9, 7, 8, 8, 9, 6, 0, 1, 1, 0, 2, 3, 4]
endY = [8, 9, 8, 7, 7, 6, 7, 6, 0, 0, 1, 1, 1, 1, 1]



# pathImgOri = [
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
# # Agents = ["A", "B", "C", "D", "E"]
# Agents = ["A"]  # 表示机器人
# startX = [0, 1, 0, 1, 5]  # Ｘ轴坐标
# startY = [0, 0, 1, 1, 2]
#
# endX = [28, 28, 27, 26, 25]
# endY = [28, 27, 28, 26, 28]
#
pathImg = [[1 for mm in range(len(pathImgOri[0]) + 2)] for nn in range(len(pathImgOri) + 2)]
for x in range(len(pathImgOri)):
    for y in range(len(pathImgOri[0])):
        pathImg[x + 1][y + 1] = pathImgOri[x][y]

print pathImg
for agt in range(len(Agents)):
    startX[agt] = startX[agt] + 1
    startY[agt] = startY[agt] + 1
    endX[agt] = endX[agt] + 1
    endY[agt] = endY[agt] + 1

rows = len(pathImg)
cols = len(pathImg[0])

VERTEX = 0

bvSize = 1
graphSize = rows * cols
while graphSize > 1:
    graphSize = graphSize / 2
    bvSize = bvSize + 1

graphSize = rows * cols
print "graphSize:", graphSize
print "bvSize:", bvSize

timeStep = 0
isSat = unsat
agentsNum = len(Agents)

def cXor(a,b):
    return (not (a and b)) and (a or b)

def getBitArr(number,bvSize,sub=False): # sub=false:加法　sub=true:减法
    b = str(bin(number)).replace('0b', '')
    bitArr = []
    for i in range(bvSize):
        if i < len(b):
            if b[len(b)-1 - i] == '1':
                bitArr.append(True)
            else:
                bitArr.append(False)
        else:
            # bb = b[len(b)-1 - i]
            bitArr.append(False)
    if sub:
        for i in range(bvSize):
            bitArr[i] = cXor(bitArr[i],sub)
    return bitArr

# print getBitArr(13,8)


# for agt in range(agentsNum):
#     b = str(bin(startX[agt] * cols + startY[agt])).replace('0b', '')
#     startStatus = []
#     for i in range(bvSize):
#         if i < len(b):
#             print b
#             if b[len(b)-1 - i] == '1':
#                 startStatus.append(Bool(Agents[agt]+str("_t0_")+str(i)))
#             else:
#                 startStatus.append(Not(Bool(Agents[agt]+str("_t0_")+str(i))))
#         else:
#             # bb = b[len(b)-1 - i]
#             startStatus.append(Not(Bool(Agents[agt] + str("_t0_") + str(i))))
#
#             # print str(b),bb
#     print startStatus
#     solver.add(And(startStatus))
        # solver.add()




def Half_adder(a,b):
    s = Xor(a,b)
    co = And(a,b)
    return s,co

def Full_adder(a,b,ci):
    s,co1 = Half_adder(a,b)
    s,co2 = Half_adder(ci,s)
    co = Or(co1,co2)
    return s,co

starttime = time()  # 计时

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


for agt in range(agentsNum):
    startStatus = []
    bitArr = getBitArr(startX[agt] * cols + startY[agt],bvSize)
    for i in range(len(bitArr)):
        solver.add(Bool(Agents[agt] + str("_t0_") + str(i)) == bitArr[i])


graph = []
for x in range(len(pathImg)):
    for y in range(len(pathImg[0])):
        if pathImg[x][y] == 0:
            p = getBitArr(x * rows + y,bvSize)
            graph.append(p)


while isSat == unsat:
    toUp = getBitArr(cols,bvSize,True)
    toDown = getBitArr(cols,bvSize)
    toLeft = getBitArr(1,bvSize,True)
    toRight= getBitArr(1,bvSize)
    toLeftUp = getBitArr(cols+1,bvSize,True)
    toLeftDown = getBitArr(cols-1,bvSize)
    toRightUp = getBitArr(cols-1,bvSize,True)
    toRightDown= getBitArr(cols+1,bvSize)
    # print "Up:",toUp
    # print "Down:",toDown
    # print "Left:",toLeft
    # print "Right:",toRight

    for agt in range(len(Agents)):
        constraintArr_current = []
        constraintArr_next = []
        for i in range(bvSize):
            c = Bool(Agents[agt] + str("_t")+ str(timeStep) + str("_") + str(i))
            n = Bool(Agents[agt] + str("_t")+ str(timeStep+1) + str("_") + str(i))
            constraintArr_current.append(c)
            constraintArr_next.append(n)
        # print constraintArr_current

        constraintArr_Wait = []
        constraintArr_Down = []
        constraintArr_Up = []
        constraintArr_Left = []
        constraintArr_Right = []
        constraintArr_LeftUp = []
        constraintArr_RightUp = []
        constraintArr_LeftDown = []
        constraintArr_RightDown = []

        # 等待
        for i in range(bvSize):
            constraintArr_Wait.append(constraintArr_next[i] == constraintArr_current[i])

        # 向上
        S = [False for mm in range(bvSize)] # 加法位
        C = [False for mm in range(bvSize)] # 进位位
        for i in range(bvSize):
            if i == 0:
                S[i], C[i] = Half_adder(constraintArr_current[i],toUp[i])
            if i > 0:
                S[i], C[i] = Full_adder(constraintArr_current[i],toUp[i],C[i-1])
            # if S[i]:
            #     constraintArr_Up.append(constraintArr_next[i])
            # else:
            #     constraintArr_Up.append(Not(constraintArr_next[i]))
            # constraintArr_Up.append(Xor(S[i],Not(constraintArr_next[i])))
            constraintArr_Up.append(constraintArr_next[i] == S[i])
            # constraintArr_Up.append(Or(Or(Not(S[i]),constraintArr_current[i]),Or(Not(S[i]),Not(constraintArr_current[i]))))

        # 向下
        S = [False for mm in range(bvSize)]  # 加法位
        C = [False for mm in range(bvSize)]  # 进位位
        for i in range(bvSize):
            if i == 0:
                S[i], C[i] = Half_adder(constraintArr_current[i], toDown[i])
            if i > 0:
                S[i], C[i] = Full_adder(constraintArr_current[i], toDown[i], C[i-1])
            # constraintArr_Down.append(Xor(S[i],Not(constraintArr_next[i])))
            # constraintArr_Down.append(Or(Or(Not(S[i]),constraintArr_current[i]),Or(Not(S[i]),Not(constraintArr_current[i]))))

            # if S[i]:
            #     constraintArr_Down.append(constraintArr_next[i])
            # else:
            #     constraintArr_Down.append(Not(constraintArr_next[i]))
            constraintArr_Down.append(constraintArr_next[i] == S[i])

        # 向左
        S = [False for mm in range(bvSize)]  # 加法位
        C = [False for mm in range(bvSize)]  # 进位位
        for i in range(bvSize):
            if i == 0:
                S[i], C[i] = Half_adder(constraintArr_current[i], toLeft[i])
            if i > 0:
                S[i], C[i] = Full_adder(constraintArr_current[i], toLeft[i], C[i-1])
            # constraintArr_Left.append(Xor(S[i], Not(constraintArr_next[i])))
            # constraintArr_Left.append(Or(Or(Not(S[i]),constraintArr_current[i]),Or(Not(S[i]),Not(constraintArr_current[i]))))

            # if S[i]:
            #     constraintArr_Left.append(constraintArr_next[i])
            # else:
            #     constraintArr_Left.append(Not(constraintArr_next[i]))
            constraintArr_Left.append(constraintArr_next[i] == S[i])

        # 向右
        S = [False for mm in range(bvSize)]  # 加法位
        C = [False for mm in range(bvSize)]  # 进位位
        for i in range(bvSize):
            if i == 0:
                S[i], C[i] = Half_adder(constraintArr_current[i], toRight[i])
            if i > 0:
                S[i], C[i] = Full_adder(constraintArr_current[i], toRight[i], C[i-1])
            # constraintArr_Right.append(Xor(S[i],Not(constraintArr_next[i])))
            # constraintArr_Right.append(Or(Or(Not(S[i]),constraintArr_current[i]),Or(Not(S[i]),Not(constraintArr_current[i]))))

            # if S[i]:
            #     constraintArr_Right.append(constraintArr_next[i])
            # else:
            #     constraintArr_Right.append(Not(constraintArr_next[i]))
            constraintArr_Right.append(constraintArr_next[i] == S[i])

        # 左上
        S = [False for mm in range(bvSize)]  # 加法位
        C = [False for mm in range(bvSize)]  # 进位位
        for i in range(bvSize):
            if i == 0:
                S[i], C[i] = Half_adder(constraintArr_current[i], toLeftUp[i])
            if i > 0:
                S[i], C[i] = Full_adder(constraintArr_current[i], toLeftUp[i], C[i-1])
            constraintArr_LeftUp.append(constraintArr_next[i] == S[i])

        # 左下
        S = [False for mm in range(bvSize)]  # 加法位
        C = [False for mm in range(bvSize)]  # 进位位
        for i in range(bvSize):
            if i == 0:
                S[i], C[i] = Half_adder(constraintArr_current[i], toLeftDown[i])
            if i > 0:
                S[i], C[i] = Full_adder(constraintArr_current[i], toLeftDown[i], C[i-1])
            constraintArr_LeftDown.append(constraintArr_next[i] == S[i])

        # 右上
        S = [False for mm in range(bvSize)]  # 加法位
        C = [False for mm in range(bvSize)]  # 进位位
        for i in range(bvSize):
            if i == 0:
                S[i], C[i] = Half_adder(constraintArr_current[i], toRightUp[i])
            if i > 0:
                S[i], C[i] = Full_adder(constraintArr_current[i], toRightUp[i], C[i-1])
            constraintArr_RightUp.append(constraintArr_next[i] == S[i])

        # 右下
        S = [False for mm in range(bvSize)]  # 加法位
        C = [False for mm in range(bvSize)]  # 进位位
        for i in range(bvSize):
            if i == 0:
                S[i], C[i] = Half_adder(constraintArr_current[i], toRightDown[i])
            if i > 0:
                S[i], C[i] = Full_adder(constraintArr_current[i], toRightDown[i], C[i-1])
            constraintArr_RightDown.append(constraintArr_next[i] == S[i])

        solver.add(Or(And(constraintArr_Wait),And(constraintArr_Down),And(constraintArr_Right),And(constraintArr_Left),And(constraintArr_Right)
                      ,And(constraintArr_LeftUp),And(constraintArr_LeftDown),And(constraintArr_RightUp),And(constraintArr_RightDown)))


        constraintArr_collide = []
        constraintArr_follow = []
        for agt2 in range(len(Agents)):
            if agt < agt2:
                collide = []
                for i in range(bvSize):
                    collide.append(Bool(Agents[agt] + str("_t") + str(timeStep) + str("_") + str(i))
                                   == Bool(Agents[agt2] + str("_t") + str(timeStep) + str("_") + str(i)))
                constraintArr_collide.append(Not(And(collide)))
            if agt2 != agt:
                follow = []
                for i in range(bvSize):
                    follow.append(Bool(Agents[agt] + str("_t") + str(timeStep) + str("_") + str(i))
                                  == Bool(Agents[agt2] + str("_t") + str(timeStep + 1) + str("_") + str(i)))
                constraintArr_follow.append(Not(And(follow)))
        solver.add(And(constraintArr_collide)) # 碰撞约束
        solver.add(And(constraintArr_follow)) # 跟随约束


        # 图约束
        constraintArr_graph = []
        for p in range(len(graph)):
            collide = []
            for i in range(bvSize):
                collide.append(constraintArr_next[i] == graph[p][i])
            constraintArr_graph.append(And(collide))
        solver.add(Or(constraintArr_graph))


    if timeStep > minDistance():
        solver.push()
        for agt in range(len(Agents)):
            endP = getBitArr(endX[agt] * cols + endY[agt],bvSize)
            for i in range(bvSize):
                solver.add(Bool(Agents[agt] + str("_t") + str(timeStep + 1) + str("_") + str(i)) == endP[i])

        isSat = solver.check()

        solver.pop()
    dur = time() - starttime
    print "第", timeStep, "次", isSat, "\ttime:", ('%0.6f秒' % dur)
    timeStep = timeStep + 1

# print solver.model()

pathPlan = [["" for mm in range(cols + 1)] for nn in range(rows + 1)]

f = open('test.txt', 'w')

for agt in range(len(Agents)):
    for t in range(timeStep + 1):
        result = 0
        for i in range(bvSize):
            b = Bool(str(Agents[agt] + "_t" + str(t) + "_" + str(i) ))
            v = solver.model().evaluate(b)
            # print v
            if v:
                # print "True"
                result = result + math.pow(2,i)

        pathPlan[int(result / cols)][int(result % cols)] = pathPlan[int(result / cols)][int(result % cols)] + str(Agents[agt]) + "_t" + str(t) + ","
        f.write(str(Agents[agt]) + "_t" + str(t) + "=" + str(result) + "\tx=" + str(int(result / cols -1)) + ",y=" + str(int(result % cols -1)) + "\n")



f.close()

# 写入excel中
file_excel = '/home/dzhb/Documents/MultiAgents_BoolSat.xlsx'
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
