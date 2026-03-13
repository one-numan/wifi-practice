"""
task17_wifi_heatmap.py

Generate WiFi signal strength heatmap.
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_heatmap(data):
    """
    Create heatmap from RSSI grid.
    """

    data = np.array(data)

    plt.imshow(data, cmap="hot", interpolation="nearest")

    plt.colorbar(label="Signal Strength (dBm)")

    plt.title("WiFi Signal Heatmap")

    plt.xlabel("X Position")
    plt.ylabel("Y Position")

    plt.show()


def main():

    # Example RSSI measurements
    rssi_grid = [
        [-40, -45, -50],
        [-42, -48, -55],
        [-47, -52, -60]
    ]

    generate_heatmap(rssi_grid)


if __name__ == "__main__":
    main()
