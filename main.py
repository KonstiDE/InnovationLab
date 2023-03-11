import pandas as pd
import numpy as np

from loader import (
    read_xlsx,
    read_csv,
    xlsx_to_csv
)

from plotter.basic_columns_plots import (
    plot_source,
    plot_dates
)


def tweet(path):
    df = read_csv(path)

    plot_dates(df)


if __name__ == '__main__':
    tweet("data/raw/Tweets_ny_newyears_all_cols.csv")
