def calculate_triangle_area():
    s = (a+b+c)/2
    area = (s* (s - a) * (s-b) * (s-c)) ** 0.5 
    return area


a = float(input("Enter the length of sidea: "))

b = float(input("Enter the length of sideb: "))

c = float(input("Enter the length of side c: "))
triangle_area = calculate_triangle_area()

print(triangle_area)