import matplotlib.pyplot as plt
import numpy as np

import shutup
shutup.please()


def wrap_plot(x_data, y_data, plot_type="line", color="#007acc", alpha=1, xticks=None, grid=None):
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#0c1c23')

    if plot_type == "line":
        ax.plot(x_data, y_data, color=color, alpha=alpha)
    elif plot_type == "bar":
        ax.bar(x_data, y_data, color=color, alpha=alpha)
    elif plot_type == "scatter":
        ax.scatter(x_data, y_data, color=color, alpha=alpha)

    ax.set_facecolor('#122229')
    ax.spines['left'].set_color('#FFFFFF')
    ax.spines['left'].set_linewidth(0.5)

    ax.spines['bottom'].set_color("#3C494F")
    ax.spines['bottom'].set_linewidth(0.3)
    ax.spines['top'].set_color("#3C494F")
    ax.spines['top'].set_linewidth(0.3)
    ax.spines['right'].set_color("#3C494F")
    ax.spines['right'].set_linewidth(0.3)

    ax.tick_params(axis='both', colors='#FFFFFF')

    if xticks is not None:
        ax.set_xticklabels(xticks)

    if grid is not None:
        plt.grid(color="#3C494F", linestyle=grid, linewidth=0.3)

    plt.xticks(rotation=45, ha='right', color="white")
    plt.yticks(color="white")
    plt.tight_layout()
    plt.show()


def wrap_plots(x_data, y_datas, colors, plot_type="line", alpha=1, xticks=None, grid=None):
    assert len(colors) == len(y_datas)

    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#0c1c23')

    if plot_type == "line":
        for idx, y_data in enumerate(y_datas):
            ax.plot(x_data, y_data, color=colors[idx], alpha=alpha)
    elif plot_type == "bar":
        for idx, y_data in enumerate(y_datas):
            ax.bar(x_data, y_data, color=colors[idx], alpha=alpha)
    elif plot_type == "scatter":
        for idx, y_data in enumerate(y_datas):
            ax.scatter(x_data, y_data, color=colors[idx], alpha=alpha)

    ax.set_facecolor('#122229')
    ax.spines['left'].set_color('#FFFFFF')
    ax.spines['left'].set_linewidth(0.5)

    ax.spines['bottom'].set_color("#3C494F")
    ax.spines['bottom'].set_linewidth(0.3)
    ax.spines['top'].set_color("#3C494F")
    ax.spines['top'].set_linewidth(0.3)
    ax.spines['right'].set_color("#3C494F")
    ax.spines['right'].set_linewidth(0.3)

    ax.tick_params(axis='both', colors='#FFFFFF')

    plt.xticks(rotation=45, ha='right', color="white")
    plt.yticks(color="white")

    if xticks is not None:
        ax.set_xticklabels(xticks)

    if grid is not None:
        plt.grid(color="#3C494F", linestyle=grid, linewidth=0.3)

    plt.tight_layout()
    plt.show()
