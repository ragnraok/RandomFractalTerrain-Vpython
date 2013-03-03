import random
import math

def random_fractal(size, smoothness=1, z_scale=50):
    final_size = 1
    while final_size < size:
        final_size <<= 1
    tmp_result = [[0 for i in xrange(final_size  + 1)] for i in
            xrange(final_size + 1)]
    iterate(tmp_result, smoothness, z_scale)
    final_result = [0 for i in xrange(size)]
    for row in xrange(size):
        final_result[row] = tmp_result[row][:size] 
    
    return final_result

def iterate(height, smoothness, z_scale):
    count = 0
    iter_num = math.log(len(height) - 1, 2)
    while count < iter_num:
        count += 1
        diamond(height, count, smoothness, z_scale)
        squre(height, count, smoothness, z_scale)

def diamond(height, count, smoothness, z_scale):
    """
        a -- b -- c
        |    |    |
        d -- e -- f
        |    |    |
        g -- h -- i
    """
    terrain_size = len(height) - 1
    num_seg = 1 << (count - 1)
    span = terrain_size / num_seg
    half = span >> 1
    for x in xrange(0, terrain_size, span):
        for y in xrange(0, terrain_size, span):
            a = [x, y]
            c = [x + span, y]
            g = [x, y + span]
            i = [x + span, y + span]
            e = [x + half, y + half]

            tmp = [height[v[1]][v[0]] for v in [a, c, g, i] ]
            avg = sum(tmp) / len(tmp)

            random_val = generate_random_num(count, smoothness, z_scale)
            height[e[1]][e[0]] = avg + random_val

def squre(height, count, smoothness, z_scale):
    """
        a -- b -- c
        |    |    |
        d -- e -- f
        |    |    |
        g -- h -- i
    """
    terrain_size = len(height) - 1
    num_seg = 1 << (count - 1)
    span = terrain_size / num_seg
    half = span >> 1
    for x in xrange(0, terrain_size, span):
        for y in xrange(0, terrain_size, span):
            a = [x, y]
            b = [x + half, y]
            c = [x + span, y]
            d = [x, y + half]
            e = [x + half, y + half]
            f = [x + span, y + half]
            g = [x, y + span]
            h = [x + half, y + span]
            i = [x + span, y + span]

            above_b = [x + half, (y - half >= 0 and y - half or terrain_size -
                half)]
            left_d = [(x - half >= 0 and x - half or terrain_size - half), y +
                    half]
            right_f = [(x + half * 3 <= terrain_size and x + half * 3 or half),
                    y + half]
            below_h = [x + half, (y + half * 3 <= terrain_size and y + half * 3
                or half)]

            # the four diamonds
            _square_calculator(height, count, smoothness, z_scale, a, e, g, left_d, d)
            _square_calculator(height, count, smoothness, z_scale, a, e, c, above_b, b)
            _square_calculator(height, count, smoothness, z_scale, c, e, i, right_f, f)
            _square_calculator(height, count, smoothness, z_scale, g, e, i, below_h, h)

    for y in xrange(0, terrain_size, span):
        height[y][terrain_size] = height[y][0]

    for x in xrange(0, terrain_size, span):
        height[terrain_size][x] = height[0][x]

def _square_calculator(height, count, smoothness, z_scale, a, b, c, d, center_point):
    tmp = [height[v[1]][v[0]] for v in [a, b, c, d]]
    avg = sum(tmp) / len(tmp)
    random_val = generate_random_num(count, smoothness, z_scale)
    height[center_point[1]][center_point[0]] = avg + random_val


def generate_random_num(count, smoothness, z_scale):
    sign = random.random() > 0.5 and 1 or -1
    _reduce = 1
    for i in xrange(count):
        _reduce *= math.pow(2, -smoothness)
    return _reduce * random.randint(-z_scale, z_scale)
