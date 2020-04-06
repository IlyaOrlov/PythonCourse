planets_info = "В сутках на Меркурии Mercury дней, на Венере Venus дней, на Марсе Mars дня, на Юпитере Jupiter дня," \
               " на Сатурне Saturn дня, на Уране Uranus дня, на Плутоне Pluto дней."
planets_day = {"Mercury": "1407.36", "Venus": "5832.00", "Earth": "24.00", "Mars": "24.39",
               "Jupiter": "09.55", "Saturn": "10.34", "Uranus": "17.14", "Pluto": "153.17"}

planets_list = planets_info.split()
i = 0
while i < len(planets_list):
    if planets_list[i] in planets_day:
        (planets_list[i]) = float(planets_day[planets_list[i]])
        planets_list[i] = "{:.2f}".format(float(planets_list[i])/24)
    i += 1
print(' '.join(planets_list))
