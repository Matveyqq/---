import random
list = [0,350,400,450,500,550,600,650,700,850,900,950,1000,"сектор СИГМА","сектор ПРИЗ","банкрот","сектор ПЛЮС"]
points = 0








def prokrutka_barabana():
    list = [0, 350, 400, 450, 500, 550, 600, 650, 700, 850, 900, 950, 1000, "сектор СИГМА", "сектор ПРИЗ", "банкрот",
            "сектор ПЛЮС"]
    points = 0
    choose = random.choice(list)
    print(choose)
    if type(choose) == int:
        points += choose
    else:
        if choose == "сектор СИГМА":
            print *2
    if choose == "банкрот":
        points = 0






prokrutka_barabana()