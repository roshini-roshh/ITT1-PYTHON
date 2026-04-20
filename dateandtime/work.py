def calculate_work_hours(T, H_total):

    if not (H_total >= 24 and H_total % 2 == 0 and T < H_total):
        print("INVALID INPUT")
        return
    x = 18
    D = (H_total - (x * T)) / (24 - x)
    H = T - D
    if D.is_integer() and H.is_integer() and D >= 0 and H >= 0:
        print(f"D = {int(D)}, H = {int(H)}")
    else:
        print("No valid integer solution found for these parameters.")

T_input = 15
H_total_input = 330
calculate_work_hours(T_input, H_total_input)
