import pandas as pd

from xlsx2csv import Xlsx2csv
from io import StringIO


def read_excel(path: str, sheet_name: str):
    buffer = StringIO()
    Xlsx2csv(path, outputencoding="utf-8", sheet_name=sheet_name).convert(buffer)
    buffer.seek(0)
    return pd.read_csv(buffer)
