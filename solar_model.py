# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.fx = body.fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!

        dx = body.x - obj.x
        dy = body.y - obj.y

        r = ((dx)**2 + (dy)**2)**0.5

        cos = -dx / r
        sin = -dy / r

        body.fx += body.m*obj.m/r**2*gravitational_constant*cos
        body.fy += body.m*obj.m/r**2*gravitational_constant*sin


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    dt = dt*10000
    ax = body.fx/body.m
    body.x += body.vx*dt
    print(body.vy)
    body.vx += ax*dt

    ay = body.fy/body.m
    body.y += body.vy*dt
    body.vy += ay*dt



def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)

    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
