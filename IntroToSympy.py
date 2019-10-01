from math import *
from sympy import *
from sympy.plotting import plot
from sympy.plotting import plot_implicit
init_printing(use_unicode=True)
x, y = symbols('x y')

print(solve(Eq(10, (x-1)/(x-2))))
print(solve_poly_system([x*y - 2*y, 2*y**2 - x**2], x, y))
print(solve_poly_system([.7071068*x**2 + sqrt(2) - y, -y**2 + x**3 - 3*x + 2], x, y))
