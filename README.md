RandomFractalTerrain-Vpython
============================

random fractal terrain demo with vpython

this demo was inspired by [qiao/fractal-terrain-generator][1], but use vpython instead

# Dependence:

- [VPython][2], in ubuntu, you can install it with this command: 
``sudo apt-get install python-visual``

# Usage
```Shell
usage: main.py [-h] [--size [SIZE]] [--z_scale [Z_SCALE]]
               [--smoothness [SMOOTHNESS]]

               the visualization of randomfractal terrain with vpython

               optional arguments:
               -h, --help            show this help message and exit
               --size [SIZE]         the size of the terrain, default is 40
               --z_scale [Z_SCALE]   this value affect the maximum and minimum height of terrain, default is 70
               --smoothness [SMOOTHNESS] the smoothness of the terrain, higher this value, smoother the terrain default is 1
```

You can import ``alg.py`` in your project to generate the reandom fractal terrain elevation:

```Python
from alg import *
height = random_fractal(size=size, z_scale=z_scale, smoothness=smoothness)
```
then ``height`` is a ``size x size`` array contains the elevation of terrain


[1]: https://github.com/qiao/fractal-terrain-generator
[2]: http://vpython.org/
