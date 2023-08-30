#coding = utf-8

#RGB -> HSV
# '''
# 计算色调（Hue）：
# 最大值 maxVal = max(R, G, B)
# 最小值 minVal = min(R, G, B)
# 如果 maxVal 和 minVal 相等，则 H = 0（表示没有明确定义的色调）
# 否则，根据最大值的位置计算色调：
# 如果 maxVal 等于 R，则 H = (G - B) / (maxVal - minVal)
# 如果 maxVal 等于 G，则 H = 2 + (B - R) / (maxVal - minVal)
# 如果 maxVal 等于 B，则 H = 4 + (R - G) / (maxVal - minVal)
# 将 H 转换为角度制，即 H *= 60°
# 如果 H 小于 0，则 H += 360°
# '''
import matplotlib.pyplot as plt
import math

def toAngle(H):
    res = math.floor(H * 60)
    if res < 0:
        res += 360
    # print("res:", res)
    return res
def anasysisA(hue):
    diffs = []
    for i in range(0, len(hue) - 1):
        if hue[i] != hue[i+1]:
            diffs.append(i)
    print("diff:", diffs)


step = 4
R = range(1, 255, step)
G = range(1, 255, step)
B = range(1, 255, step)
H = 0
i = 0
hue = [0] * 360
for r in R:
    for g in G:
        for b in B:
            diff = max(r, g, b) - min(r, g, b) #差值
            if(max(r, g, b) == min(r, g, b)):
                H = 0
            elif max(r, g, b) == r:
                H = (g - b) / diff
                hue[toAngle(H)] = 1
            elif max(r, g, b) == g:
                H = 2 + (b - r) / diff
                hue[toAngle(H)] = 2
            elif max(r, g, b) == b:
                H = 4 + (r - g) / diff
                hue[toAngle(H)] = 3
            H *= 60
            if H < 0:
                H += 360
            i += 1
print("len:", i)
anasysisA(hue)
print(hue, len(hue), len(range(0,360)))
plt.scatter(range(0,360), hue)
plt.show()

            
