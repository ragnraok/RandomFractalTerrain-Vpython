import argparse


SIZE = 60
Z_SCALE = 70 
SMOOTHNESS = 1 

def parser_arg(arg):
    global SIZE, Z_SCALE, SMOOTHNESS
    parser = argparse.ArgumentParser(
            description="the visualization of random fractal terrain with vpython")
    parser.add_argument("--size", default=40, nargs="?", 
    help="the size of the terrain, default is 40")
    parser.add_argument("--z_scale", default=70, nargs="?",
            help="this value affect the maximum and minimum height of terrain, default is 70")
    parser.add_argument("--smoothness", default=1, nargs="?",
            help="the smoothness of the terrain, higher this value, smoother the terrain, default is 1")
    name_space = parser.parse_args(arg)
    SIZE = int(name_space.size)
    Z_SCALE = int(name_space.z_scale)
    SMOOTHNESS = float(name_space.smoothness)

def main_loop():
    from visual import scene, vector, rate
    scene.width = scene.height = 700
    
    from grid_generator import create_grid, grid_frame, update_curves_height
    from alg import random_fractal
    
    scene.forward = vector(-100, -60, -100)

    print "size is %d, z_scale is %d, smoothness is %d" % (SIZE, Z_SCALE,
            SMOOTHNESS)

    height = random_fractal(SIZE, z_scale=Z_SCALE, smoothness=SMOOTHNESS)
    horizontal_curves, vertical_curves = create_grid(SIZE, height)
    
    while True:
        rate(100)
        grid_frame.rotate(angle=0.005, axis=(0, 1, 0), origin=(0, 0, 0))
        if scene.kb.keys:
            key = scene.kb.getkey()
            if key == "f5":
                height = random_fractal(SIZE, z_scale=Z_SCALE, smoothness=SMOOTHNESS)
                update_curves_height(horizontal_curves, vertical_curves, SIZE,  
                        height)
            

if __name__ == '__main__':
    import sys
    parser_arg(sys.argv[1:])
    main_loop()
