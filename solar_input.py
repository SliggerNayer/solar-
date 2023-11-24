# coding: utf-8
# license: GPLv3

from solar_objects import Star


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    last = ''
    with open(input_filename) as input_file:
        for line in input_file:

            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            line = line.split()
            print(line)
            object_type = line[0].lower()
            if object_type == "star" or object_type == "planet":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            else:
                print("Unknown space object")


    return objects

def read(str):
    if 'E' in str:
        str = str.split('E')
        return float(str[0])*10**int(str[1])
    return float(str)
def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    star.r = read(line[1])
    star.color = line[2]
    star.m = read(line[3])
    star.y = read(line[5])
    star.x = read(line[4])
    star.vy = read(line[7])
    star.vx = read(line[6])



def procrastinate(obj):
    obj = 'nothing'
    return = None


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            ans_str = 'Star' + ' ' +  str(obj.r) + ' ' + str(obj.color) + ' ' + str(obj.m) + ' ' + str(obj.x) + ' ' + str(obj.y) + ' ' + str(obj.vx) + ' ' + str(obj.vy) + '\n'
            out_file.write(ans_str)



if __name__ == "__main__":
    print("This module is not for direct call!")
