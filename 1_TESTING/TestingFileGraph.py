from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import ast 
plt.rcParams["toolbar"] = "None"

fig, ax = plt.subplots()
fig.supxlabel("Time")
fig.supylabel("Depth (m)")
 

def calc(n):
    number = (((n*150)/4.5)-16.2079)*6894.76
    return (number/(997*9.81))

def main():
    f = open("receiveFile.txt", "r")
    current = f.read()
    x_values = ast.literal_eval(current)
    depth=map(calc, x_values)

    
    ax.plot(list(depth))
    plt.show()


if __name__ == "__main__":
    main()
