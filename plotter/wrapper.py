import matplotlib.pyplot as plt


def wrap_plot(x_data, y_data, plot_type="line", color="#007acc"):
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#0c1c23')

    if plot_type == "line":
        ax.plot(x_data, y_data, color=color, alpha=0.6)
    elif plot_type == "bar":
        ax.bar(x_data, y_data, color=color, alpha=0.6)
    elif plot_type == "scatter":
        ax.scatter(x_data, y_data, color=color, alpha=0.6)

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
    plt.tight_layout()
    plt.show()
