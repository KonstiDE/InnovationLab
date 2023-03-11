import pandas as pd
import matplotlib.pyplot as plt
import datetime

from .wrapper import wrap_plot as plot


def plot_source(df):
    group = df.groupby(by="source").size().reset_index(name='count')
    group = group.sort_values(by="count", ascending=False).head(10)

    plot(group["source"], group["count"] / len(df), plot_type="bar", color="#ff7f00")


def plot_dates(df):
    df["created_at"] = datetime.datetime.fromisoformat(df["created_at"])



