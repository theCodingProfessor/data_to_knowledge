import os

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

text_style = dict(horizontalalignment='right', verticalalignment='center',
                  fontsize=12, fontfamily='monospace')
marker_style = dict(linestyle=':', color='0.8', markersize=10,
                    markerfacecolor="tab:blue", markeredgecolor="tab:blue")


def format_axes(this_ax):
    this_ax.margins(0.2)
    this_ax.set_axis_off()
    this_ax.invert_yaxis()


def split_list(a_list):
    i_half = len(a_list) // 2
    return a_list[:i_half], a_list[i_half:]


fig, axs = plt.subplots(ncols=2)
fig.suptitle('Filled markers', fontsize=14)
for ax, markers in zip(axs, split_list(Line2D.filled_markers)):
    for y, marker in enumerate(markers):
        ax.text(-0.5, y, repr(marker), **text_style)
        ax.plot([y] * 3, marker=marker, **marker_style)
    format_axes(ax)

# Citation to MatPlotLib for the source code
plt.text(0.2, -.02, 'Filled Markers: https: // matplotlib.org / stable / gallery / lines_bars_and_markers / marker_reference.html  # sphx-glr-gallery-lines-bars-and-markers-marker-reference-py', ha='center', va='center', fontsize=6, transform=plt.gca().transAxes)

# Show the plot
plt.grid(True)

# File path/name for the image
image_path = os.path.join('../static/img', 'filled_marker_demo.png')

# Save image to the static/images directory
plt.savefig(image_path)
plt.close()
