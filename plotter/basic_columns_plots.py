import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

from .wrapper import wrap_plot as plot
from .wrapper import wrap_plots as mplot


def plot_source(df):
    group = df.groupby(by="source").size().reset_index(name='count')
    group = group.sort_values(by="count", ascending=False).head(10)

    plot(group["source"], group["count"] / len(df), plot_type="bar", color="#ff7f00")


def plot_dates(df):
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["created_at"] = df["created_at"].dt.round('15min')

    group2021_30 = df[df["created_at"].dt.day == 30].groupby(by="created_at").size().reset_index(name="count")
    group2021_31 = df[df["created_at"].dt.day == 31].groupby(by="created_at").size().reset_index(name="count")
    group2022_01 = df[df["created_at"].dt.day == 1].groupby(by="created_at").size().reset_index(name="count")
    group2022_02 = df[df["created_at"].dt.day == 2].groupby(by="created_at").size().reset_index(name="count")

    mplot(group2021_30["created_at"], y_datas=[
        group2021_30["count"],
        group2021_31["count"],
        group2022_01["count"],
        group2022_02["count"]
    ], colors=["#ff7f00", "red", "green", "#007acc"], plot_type="line", grid="--")

