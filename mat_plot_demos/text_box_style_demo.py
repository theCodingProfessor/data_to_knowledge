import os

import matplotlib.pyplot as plt

plt.text(0.6, 0.7, "eggs", size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )

plt.text(0.55, 0.6, "spam", size=50, rotation=-25.,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )

# Citation to MatPlotLib for the source code
plt.text(0.5, -.1, 'Text Box Style: https://matplotlib.org/stable/gallery/text_labels_and_annotations/fancytextbox_demo.html#sphx-glr-gallery-text-labels-and-annotations-fancytextbox-demo-py', ha='center', va='center', fontsize=5, transform=plt.gca().transAxes)

# Show the plot
plt.grid(True)

# File path/name for the image
image_path = os.path.join('../static/img', 'text_box_demo.png')

# Save image to the static/images directory
plt.savefig(image_path)
plt.close()
