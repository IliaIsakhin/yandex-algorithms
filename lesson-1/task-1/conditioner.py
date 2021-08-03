t_room, t_cond = list(map(int, input().split()))
mode = input()

if (mode == "fan") | ((mode == "freeze") & (t_room < t_cond)) | ((mode == "heat") & (t_room > t_cond)):
    print(t_room)
else:
    print(t_cond)
