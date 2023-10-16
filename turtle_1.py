import turtle

n = float(input(">"))
turtle.speed(0) #描画速度表示
d = 360/n
for i in range(2000):　
    turtle.forward(200)　#線の長さ
    turtle.left(d)　#角度

turtle.done()
