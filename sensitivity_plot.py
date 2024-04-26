import numpy as np
import matplotlib.pyplot as plt

def plot_sense(x,y,z,scale1,scale2, y_axis, x_axis, outputname):

    X, Y = np.meshgrid(y, x)
    fig = plt.figure(figsize=(7,5), dpi = 100)
    ax = fig.add_subplot(111)
    cp = ax.contourf(X, Y, z, 300, cmap='jet')
    fig.colorbar(cp) # Add a colorbar to a plot
    ax.set_title(outputname)

    # Setting scale conditions

    if scale1 == 'Exponential':
        ax.set_yscale('log')
    if scale2 == 'Exponential':
        ax.set_xscale('log')

    # Setting axis labels

    # Y axis

    y_label = y_axis

    # X axis
    x_label = x_axis

    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    plt.tight_layout()

    plt.show()