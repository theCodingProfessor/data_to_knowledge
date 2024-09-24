"""
MatPlotLib Demo
Data Demonstration using MatPlotLib and Python Stack
Clinton Garwood 2024
Code Assist via ChatGPT
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle
import os
import math


def names_as_colors():
    colors = mcolors
    ncols = 4
    sort_colors = True
    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        names = sorted(colors, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    width = cell_width * ncols + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin / width, margin / height, (width - margin) / width, (height - margin) / height)
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows - 0.5), -cell_height / 2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=14, horizontalalignment='left', verticalalignment='center')

        ax.add_patch(
                Rectangle(xy=(swatch_start_x, y - 9), width=swatch_width, height=18, facecolor=colors[name], edgecolor='0.7')
            )

        # return fig

    # File path/name for saving the image
    image_path = os.path.join('../static/img', 'group_graphs.png')

    plt.grid(True)

    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()
    return


def plot_lots():
    # File path/name for saving the image
    image_path = os.path.join('../static/img', 'group_graphs.png')

    f_blue = {'family': 'serif', 'color': 'blue', 'size': 12}
    f_red = {'family': 'serif', 'color': 'darkred', 'size': 9}

    # Left Plot:
    x = np.array([0, 1, 2, 3])
    y = np.array([3, 8, 1, 10])

    plt.subplot(1, 2, 1)
    plt.plot(x, y)
    plt.title("Left Table", fontdict=f_blue)
    plt.xlabel("For X Axis", fontdict=f_red)
    plt.ylabel("For Y Axis", fontdict=f_red)
    # Right Plot:
    x = np.array([0, 1, 2, 3])
    y = np.array([10, 20, 30, 40])

    plt.subplot(1, 2, 2)
    plt.plot(x, y)
    plt.title("Right Table", fontdict=f_blue)
    plt.xlabel("For X Axis", fontdict=f_red)
    plt.suptitle("Left and Right Tables")
    plt.grid(True)

    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()
    return


def multi_line():
    # File path/name for saving the image
    image_path = os.path.join('../static/img', 'multi_line.png')

    # Define the data for each line
    data_1 = [0, 1, 2, 1]  # Data for the first line
    data_2 = [1, 2, 3, 2]  # Data for the second line
    data_3 = [2, 3, 4, 3]  # Data for the third line

    # X-axis points (common for all lines)
    x = np.arange(len(data_1))

    # Create the figure and axis
    plt.figure()

    # Plot the first line (black, circle marker, solid line)
    plt.plot(x, data_1, marker='o', color='black', linestyle='-', label='Line 1: Black Circle')

    # Plot the second line (dark blue, dot marker, dashed line)
    plt.plot(x, data_2, marker='.', color='darkblue', linestyle='--', label='Line 2: Blue Dot')

    # Plot the third line (bluish red, diamond marker, dotted line)
    plt.plot(x, data_3, marker='D', color='indianred', linestyle=':', label='Line 3: Red Diamond')

    # Add title and labels
    plt.title('Explore Line Styles and Marker Design')
    plt.xlabel('Position in the List')
    plt.ylabel('Value in the List Position')

    # Add a grid and a legend
    plt.grid(True)
    plt.legend()

    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()

    return


def directed_line(node_data):
    node_points = np.array(node_data)
    # File path/name for saving the image
    image_path = os.path.join('../static/img', 'line_direct.png')

    # Plot and save image
    plt.figure()
    plt.plot(node_points, 'o-r')

    plt.title(f'Display data: {node_points}')
    plt.xlabel('Index Position')
    plt.ylabel('Value in List')
    plt.grid(True)

    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()

    return image_path


def array_figure(starting, ending):
    # Generate a simple plot with the input range
    fig_start = np.array([0, starting])
    fig_end = np.array([0, ending])

    # File path/name for saving the image
    image_path = os.path.join('../static/img', 'plot_array.png')

    # Plot and save image
    plt.figure()
    plt.plot(fig_start, fig_end)
    plt.title(f'Plot NP array as range [0: {fig_start} ] to  [0 - {fig_end}')
    plt.xlabel('Starting Data')
    plt.ylabel('Ending Data')
    plt.grid(True)

    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()

    return image_path


def generate_plot(start, end):
    # Generate a simple plot with the input range
    x = list(range(start, end+1))
    y = [i**2 for i in x]  # Example plot: y = x^2

    # File path/name for saving the image
    image_path = os.path.join('../static/img', 'plot.png')

    # Plot and save image
    plt.figure()
    plt.plot(x, y)
    plt.title(f'Plot for range {start} to {end}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)

    # Save image to the static/images directory
    plt.savefig(image_path)
    plt.close()

    return image_path


def testing():
    # list_data = [1, 2, 3, 4, 3, 2, 3, 4, 3, 2, 1, 1, 2.5, 2.5, 2.5]
    # img_path = directed_line(list_data)
    # multi_line()
    # plot_lots()
    return


testing()
