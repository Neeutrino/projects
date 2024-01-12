def imb(w, h):
    imb_num = w / (h * h)
    if 18.5 <= imb_num <= 25:
        print('Оптимальная масса')
    elif imb_num > 25:
        print('Избыточная масса')
    else:
        print('Недостаточная масса')


weight = float(input())
height = float(input())

imb(weight, height)
