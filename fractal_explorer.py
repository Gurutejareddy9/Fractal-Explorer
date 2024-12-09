import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def julia(z, c, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def draw_fractal(xmin,xmax,ymin,ymax,width,height,fractal_type, c=None, max_iter=256):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1,r2,np.array([[fractal_type(complex(r, i), c, max_iter) for r in r1] for i in r2]))

def main():
    print("Fractal Explorer")
    print("1. Mandelbrot Set")
    print("2. Julia Set (with c=-0.8+0.156i)")
    choice = input("Choose a fractal (1/2): ")
    
    if choice == "1":
        d = draw_fractal(-2.0,1.0,-1.5,1.5,1000,1000,mandelbrot)
    elif choice == "2":
        c = complex(-0.8, 0.156)
        d = draw_fractal(-1.5,1.5,-1.5,1.5,1000,1000,julia, c)
    else:
        print("Invalid choice. Exiting.")
        return
    
    plt.imshow(d[2], extent=(d[0].min(), d[0].max(), d[1].min(), d[1].max()))
    plt.show()

if __name__ == "__main__":
    main()
