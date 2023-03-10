from loader import read_excel


def tweet(path, file_name):
    df = read_excel(path, sheet_name=file_name)

    print(df.columns)


if __name__ == '__main__':
    tweet("data/raw", "Tweets_ny_newyears_all_cols.xlsx")
