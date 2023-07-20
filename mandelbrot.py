xmin = -2
xmax = 1
ymin = -1.5
ymax = 1.5
width = 80
height = 40
threshhold = 1000

def in_mandelbrot(x0, y0, n):
    x, y = 0, 0
    while n > 0:
        xtemp = x*x - y*y + x0
        y = 2*x*y + y0
        x = xtemp
        n -= 1
        if x*x + y*y > 4:
            return False
    return True

def mandel():
    dx = (xmax - xmin) / width
    dy = (ymax - ymin) / height

    y = ymax

    while y >= ymin:
        x = xmin
        while x < xmax:
            if in_mandelbrot(x, y, threshhold):
                print('*', end='')
            else:
                print('.', end='')
            x = x + dx
        print()
        y = y - dy

    return 0

mandel()

