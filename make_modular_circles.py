import numpy as np
import matplotlib.pyplot as plt
import math
from argparse import ArgumentParser
from pathlib import Path


def main(params):
    print("Main is running...")
    Path(params.path).mkdir(parents=True, exist_ok=True)

    radius = 1
    step_size = 2*math.pi/params.num_ticks
    thetas = np.arange(0, 2*math.pi, step_size)
    x_vals = radius * np.cos(thetas)
    y_vals = radius * np.sin(thetas)

    for index in range(params.num_samples):
        print("Index = ", index)
        multiple_to_use = index
        start_vals = np.arange(0, params.num_ticks-1, 1)
        end_vals = start_vals*multiple_to_use
        end_vals = end_vals % params.num_ticks

        plt.figure(figsize=(10, 10))
        plt.plot(x_vals, y_vals, 'k.')

        for i in range(len(start_vals)):
            plt.plot([x_vals[start_vals[i]], x_vals[end_vals[i]]],
                     [y_vals[start_vals[i]], y_vals[end_vals[i]]], 'k-', lw=0.5)

        plt.axis('off')
        plt.title("%s%i" % ("Multiple = ", index))
        plt.savefig("%s%i%s" %
                    (params.path, index, ".png"))
        plt.close()


if __name__ == "__main__":
    parser = ArgumentParser(add_help=False)
    parser.add_argument('--path', type=str, default="",
                        help='Path to folder where outputs will be saved')
    parser.add_argument('--num_samples', type=int, default=360,
                        help='Number of samples to process')
    parser.add_argument('--num_ticks', type=int, default=360,
                        help='Number of ticks to use (points around the circle)')
    params = parser.parse_args()

    main(params)
