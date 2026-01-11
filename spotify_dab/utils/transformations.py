class reusable:

    def drop_columns(self, df, columns):
        df = df.drop(*columns)
        return df