import turtle

def drawPath():
    turtle.title('数据驱动的动态路径绘制')
    turtle.setup(800,600,0,0)

    pen = turtle.Turtle()
    pen.color("red")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(5)

    # 读取文件
    result = []
    filename = input('输入文件名:')
    file = open(filename,"r")
    for line in file:
        result.append(list(map(float,line.split(','))))
    print(result)
    # 动态绘制
    for i in range(len(result)):
        pen.color((result[i][3],result[i][4],result[i][5]))
        pen.fd(result[i][0])
        if result[i][1]:
            pen.rt(result[i][2])
        else:
            pen.lt(result[i][2])
    pen.goto(0,0)


if __name__ == '__main__':
    drawPath()
