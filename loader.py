import os
import pandas as pd

from xlsx2csv import Xlsx2csv
from io import StringIO


def read_xlsx(path: str, sheet_name: str):
    buffer = StringIO()
    Xlsx2csv(path, outputencoding="utf-8", sheet_name=sheet_name).convert(buffer)
    buffer.seek(0)
    return pd.read_csv(buffer)


def read_csv(path: str):
    return pd.read_csv(path, sep=",")


def xlsx_to_csv(path: str, sheet_name: str):
    data_xls = pd.read_excel(path, sheet_name=sheet_name, dtype=str, index_col=None)
    data_xls.to_csv(path.replace(".xlsx", ".csv"), encoding='utf-8', index=False)
