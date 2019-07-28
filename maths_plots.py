"""import turtle
x = 0
while x<300:
    y = x**2/300
    turtle.goto(x, y)
    x = x + 100
    print(turtle.pos())

    


turtle.mainloop()


import turtle
num_pts = 5
for u in range(num_pts):
    turtle.left(360/num_pts)
    turtle.forward(100)
    
turtle.mainloop()    
"""
import turtle
result = []
for count in range(1,900):
    if count % 3 == 0 and count % 5 ==0:
        result.append ("Fizzbuzz")
    elif count % 5 == 0:
        result.append("buzz")
    elif count % 3 ==0:
         result.append("fizz")  
    else:
            result.append(count)
print(result)     
