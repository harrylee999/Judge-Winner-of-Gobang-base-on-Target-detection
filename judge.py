#求与水平线的角度
def getAngle(point1,point2):
    dx1 = point2[0] - point1[0]
    dy1 = point1[1] - point2[1]
    if (abs(dx1)<80) and (abs(dy1)<80) :
        angle1 = math.atan2(dy1, dx1)
        angle1 = int(angle1 * 180 / math.pi)
    #    print(angle1)
    else:
        angle1 = None
    return angle1

#递归求某一方向上的棋子数量 并且保存坐标
def getnum(point,angle,midpoint,win):
    b=0
    win.append(point)
    for i in midpoint:
        if i != point:
            a = getAngle(point,i)
            if a != None:
                if angle == 180:
                    if ((a > -180) and (a < -175)) or (a > 175) and (a <= 180):
                        b = 1
                        m = getnum(i, angle, midpoint,win)
                        b+=m
                        break
                else:
                    if (a>(angle-5)) and (a<(angle+5)):
                        b = 1
                        m = getnum(i, angle, midpoint,win)
                        b+=m
                        break
    return b

#求得5个棋子中心坐标
def win(white):
    i = 0

    while i < len(white):
        a = white[i]
        a135 = 1
        a90 = 1
        a45 = 1
        a0 = 1
        a_45 = 0
        a_90 = 0
        a_135 = 0
        a180 = 0
        win135=[]
        win90=[]
        win45=[]
        win0=[]
        for point in white:
            if a == point:
                continue
            else:
                angle = getAngle(a, point)
                if angle != None:
                    if (angle > 130) and (angle < 140):
                        a135 += 1
                        a135 += getnum(point, 135, white,win135)
                        if a135 + a_45 == 5:
                            win135.append(a)
                            return win135
                    elif (angle > 85) and (angle < 95):
                        a90 += 1
                        a90 += getnum(point, 90, white,win90)
                        if a90 + a_90 == 5:
                            win90.append(a)
                            return win90
                    elif (angle > 40) and (angle < 50):
                        a45 += 1
                        a45 += getnum(point, 45, white,win45)
                        if a45 + a_135 == 5:
                            win45.append(a)
                            return win45
                    elif (angle > -5) and (angle < 5):
                        a0 += 1
                        a0 += getnum(point, 0, white,win0)
                        if a0 + a180 == 5:
                            win0.append(a)
                            return win0
                    elif (angle > -50) and (angle < -40):
                        a_45 += 1
                        a_45 += getnum(point, -45, white,win135)
                        if a135 + a_45 == 5:
                            win135.append(a)
                            return win135
                    elif (angle > -95) and (angle < -85):
                        a_90 += 1
                        a_90 += getnum(point, -90, white,win90)
                        if a90 + a_90 == 5:
                            win90.append(a)
                            return win90
                    elif (angle > -140) and (angle < -130):
                        a_135 += 1
                        a_135 += getnum(point, -135, white,win45)
                        if a_135 + a45 == 5:
                            win45.append(a)
                            return win45
                    elif ((angle > -180) and (angle < -175)) or (angle > 175) and (angle <= 180):
                        a180 += 1
                        a180 += getnum(point, 180, white,win0)
                        if a180 + a0 == 5:
                            win0.append(a)
                            return win0
        i+=1

        
winpoint = win(white)
if winpoint != None:
    str = '白方胜利！'
else:
    winpoint = win(black)
    if winpoint != None:
        str = '黑方胜利！'
    else:
        str = '未能正确识别或未检测到胜利方，请检查图片！！！！'
print(winpoint)
print(str)
