def solve_units_problem(T, total_units, multiplier):
    X = (total_units - T) / (multiplier - 1)
    Y = T - X
    return int(X), int(Y)

T2, M_total2 = 70, 2500
H, M = solve_units_problem(T2, M_total2, 60)
print(f"Problem 2 Output: H = {H}, M = {M}")

T3, D_total3 = 50, 260
W, D = solve_units_problem(T3, D_total3, 7)
print(f"Problem 3 Output: W = {W}, D = {D}")
