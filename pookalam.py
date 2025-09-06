c1 =circle(r=150,fill="black")
r1 =rectangle(w=210,h=210,fill="brown",stroke="brown") | repeat(15, rotate(50))
r2 =rectangle(w=195,h=195,fill="red",stroke="red") | rotate(15) | repeat(15, rotate(50))
r3 =rectangle(w=179,h=179,fill="orange",stroke="orange") | repeat(15, rotate(50))
r4 =rectangle(w=162,h=162,fill="yellow",stroke="yellow") | rotate(15) | repeat(15, rotate(50))
r5 =rectangle(w=144,h=144,fill="white",stroke="white") | repeat(15, rotate(50))
r6 =rectangle(w=130, h=130,fill ="green",stroke="green") | rotate(15) | repeat(50, rotate (30))
c2 =circle(r=92,fill="purple", stroke="purple")
e1 =ellipse(w=200, h=10, fill="magenta", stroke="darkmagenta", stroke_width=2) \
     | repeat(50, rotate(5)) | scale(0.7) | translate(x=0, y=0)
c3 =circle(r=50,fill="white",stroke="purple")
diamond_shape1 =[Point(35,-12), Point(45,10), Point(75,20), Point(60,-10)]
diamond_shape2 =[Point(70,-30), Point(60,-10), Point(75,20), Point(85,-12)]
diamond_shape3 =[Point(105,-20), Point(85,-12), Point(75,20), Point(103,5)]
diamond_shape4 =[Point(125,12), Point(103,5), Point(75,20), Point(105,29)]
diamond_shape5 =[Point(115,50), Point(105,29), Point(75,20), Point(89,45)]
diamond_shape6 =[Point(80,69), Point(89,45), Point(75,20), Point(67,48)]
diamond_shape7 =[Point(39,54), Point(67,48), Point(75,20), Point(50,32)]
diamond_shape8 =[Point(24,22), Point(50,32), Point(75,20), Point(45,10)]
d1 =polygon(diamond_shape1, fill="orange", stroke="brown", stroke_width=3) | translate(-75,-20)
d2 =polygon(diamond_shape2, fill="yellow", stroke="brown", stroke_width=3) | translate(-75,-20)
d3 =polygon(diamond_shape3, fill="orange", stroke="brown", stroke_width=3) | translate(-75,-20)
d4 =polygon(diamond_shape4, fill="yellow", stroke="brown", stroke_width=3) | translate(-75,-20)
d5 =polygon(diamond_shape5, fill="orange", stroke="brown", stroke_width=3) | translate(-75,-20)
d6 =polygon(diamond_shape6, fill="yellow", stroke="brown", stroke_width=3) | translate(-75,-20)
d7 =polygon(diamond_shape7, fill="orange", stroke="brown", stroke_width=3) | translate(-75,-20)
d8 =polygon(diamond_shape8, fill="yellow", stroke="brown", stroke_width=3) | translate(-75,-20)
c4 =circle(r=10,fill="red",stroke ="green", stroke_width =5)
c5 =circle(r=43,fill="purple", stroke="purple")


show(c1, r1, r2, r3, r4, r5, c2, r6, e1, c3, c5, d1, d2, d3, d4, d5, d6, d7, d8, c4 )
