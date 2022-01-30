import pandas as pd


class DataframeManager:

    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def get_df(self):
        return self.df

    def get_n_rows_from(self, row, n, df=None):
        df = self.df if df is None else df
        return df[row: row + n]

    def split_to_dataframes_by_genre(self):
        uniq = self.df.Genre.unique()
        res = {}
        for v in uniq:
            res[v] = self.df[self.df['Genre'] == v]
        return res


def main():
    dm = DataframeManager('dataset.csv')
    df = dm.get_n_rows_from(0, 5)
    print(df)

    genre_frames = dm.split_to_dataframes_by_genre()
    for genre in genre_frames:
        df = genre_frames[genre]
        df = df.sort_values('Year')
        df = df.reset_index(drop=True)
        filename = '{0}.csv'.format(genre.lower())
        df.to_csv(filename)
        print('write file: {0}'.format(filename))


if __name__ == '__main__':
    main()
