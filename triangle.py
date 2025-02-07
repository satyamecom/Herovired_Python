#triangle
f_side=int(input("Enter a first side : "))
s_side=int(input("Enter a second side : "))
t_side=int(input("Enter a third side : "))

if f_side == s_side and s_side == t_side and t_side == f_side:
    print("Equilateral triangle")
elif f_side == s_side or s_side == t_side or t_side == f_side:
    print("Isoceles triangle")
else:
    print("Scalene triangle")


