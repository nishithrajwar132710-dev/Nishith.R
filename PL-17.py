import sympy as sp

n, z = sp.symbols('n z')
x_n = 3**n
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
sp.pprint(X_z, use_unicode=True)


#pl-2

import sympy as sp

n, z, omega = sp.symbols('n z omega')
x_n = sp.cos(omega * n)
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
sp.pprint(X_z, use_unicode=True)
