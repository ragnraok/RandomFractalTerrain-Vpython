from visual import curve, frame
import random

# from -GRID_SIZE to GRID_SIZE
GRID_SIZE = 50
grid_frame = frame()

def create_grid(size, height):
    has_height = (height != None and len(height) != 0)
    row_step = (GRID_SIZE - (-GRID_SIZE)) / float(size - 1)
    col_step = (GRID_SIZE - (-GRID_SIZE)) / float(size - 1)

    # first calculate all points
    points = [(GRID_SIZE - col * col_step, has_height and height[row][col] or 0, GRID_SIZE - row * row_step) for
            row in xrange(size) for col in xrange(size)]

    horizontal_curves = []
    vertical_curves = []
    # horizontal lines
    for i in xrange(0, len(points), size):
        for j in xrange(size - 1):
            horizontal_curves.append(curve(frame=grid_frame, pos=[
                points[i + j],
                points[i + j + 1]
                ]))

    # vertical lines
    for i in xrange(0, size):
        #print "i=%d" % i
        for j in xrange(0, len(points) - size, size):
            #print "j=%d" % j
            #print "i+j=%d" % (i+j)
            #print "i+j+size=%d" % (i+j+size)
            if i + j < len(points) and i + j + size < len(points):
                vertical_curves.append(curve(frame=grid_frame, pos=[
                    points[i + j],
                    points[i + j + size]
                    ]))
    
    return (horizontal_curves, vertical_curves)

def update_curves_height(horizontal_curves, vertical_curves, size, height):
    # first calculate all points
    points = [elem for row in height for elem in row]

    # horizontal lines
    index = 0
    for i in xrange(0, len(points), size):
        for j in xrange(size - 1):
            horizontal_curves[index].y = [points[i + j], points[i + j + 1]]
            index += 1

    # vertical lines
    index = 0
    for i in xrange(0, size):
        for j in xrange(0, len(points) - size, size):
            if i + j < len(points) and i + j + size < len(points):
                vertical_curves[index].y = [points[i + j], points[i + j +
                    size]]
                index += 1

# test grid_generator.py
if __name__ == '__main__':
    from visual import scene, vector, rate
    #scene.width = scene.height = 640
    scene.forward = vector(-100, -40, -100)
    SIZE =50
    RANGE = 10
    horizontal_curves, vertical_curves = create_grid(SIZE, None)
    #update_curves_height(horizontal_curves, vertical_curves, SIZE,  
    #        [[random.randint(-RANGE, RANGE) for i in range(SIZE)] for i in range(SIZE)])
    while True:
        rate(100)
        grid_frame.rotate(angle=0.005, axis=(0, 1, 0), origin=(0, 0, 0))
    #scene.remove_renderable(
    #horizontal_curves[0])
