def sizes_body():
    biceps_right = [29, 32]
    biceps_left = [28.5, 29]
    shoulders = [155, 160]
    breast = [93, 95]
    legs_right = [46, 49]
    legs_left = [45, 50]
    if biceps_right[0] > biceps_right[1]:
        print(f'Правый бицепс: {biceps_right[0]} -{biceps_right[0] - biceps_right[1]} {biceps_right[1]}')
    else:
        print(f'Правый бицепс: {biceps_right[0]} +{biceps_right[1] - biceps_right[0]} {biceps_right[1]}')
    if biceps_left[0] > biceps_left[1]:
        print(f'Левый бицепс: {biceps_left[0]} -{biceps_left[0] - biceps_left[1]} {biceps_left[1]}')
    else:
        print(f'Левый бицепс: {biceps_left[0]} +{biceps_left[1] - biceps_left[0]} {biceps_left[1]}')
    if shoulders[0] > shoulders[1]:
        print(f'Плечи: {shoulders[0]} -{shoulders[0] - shoulders[1]} {shoulders[1]}')
    else:
        print(f'Плечи: {shoulders[0]} +{shoulders[1] - shoulders[0]} {shoulders[1]}')
    if breast[0] > breast[1]:
        print(f'Грудь: {breast[0]} -{breast[0] - breast[1]} {breast[1]}')
    else:
        print(f'Грудь: {breast[0]} +{breast[1] - breast[0]} {breast[1]}')
    if legs_right[0] > legs_right[1]:
        print(f'Правая нога: {legs_right[0]} -{legs_right[0] - legs_right[1]} {legs_right[1]}')
    else:
        print(f'Правая нога: {legs_right[0]} +{legs_right[1] - legs_right[0]} {legs_right[1]}')
    if legs_left[0] > legs_left[1]:
        print(f'Левая нога: {legs_left[0]} -{legs_left[0] - legs_left[1]} {legs_left[1]}')
    else:
        print(f'Левая нога: {legs_left[0]} +{legs_left[1] - legs_left[0]} {legs_left[1]}')


sizes_body()
