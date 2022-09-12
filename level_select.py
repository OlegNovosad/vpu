levels = {
    1: "Рівень 1",
    2: "Рівень 2",
    3: "Рівень 3",
}

def show_levels_select():
    print("Виберіть рівень:")
    for key, value in levels.items():
        print(f'{key} - {value}')
        
    while True:
        try:
            level_choice = int(input())
            
            if level_choice in levels:
                return level_choice
            else:
                raise Exception()
        except:
            print("Неправильний рівень")