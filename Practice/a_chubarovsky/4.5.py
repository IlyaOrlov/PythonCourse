planets_day = {"Mercury": 1407.36, "Venus": 5832.00, "Earth": 24.00, "Mars": 24.39,
               "Jupiter": 09.55, "Saturn": 10.34, "Uranus": 17.14, "Pluto": 153.17}

for i, x in planets_day.items():
    x /= 24
    print("В сутках на планете {} {:.2f} дней.".format(i, x))
