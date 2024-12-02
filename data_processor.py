import pandas as pd

class DataProcessor:
    def __init__(self, config=None):
        self.config = config or {}

    def clean_data(self, df):
        """
        データのクレンジング処理
        - 欠損値補完
        - 型変換
        - 不正データの削除
        """
        # 空白やNULLの処理
        df = df.fillna(value=self.config.get('fillna_values', {}))

        # 型変換
        for column, dtype in self.config.get('dtypes', {}).items():
            if dtype == 'numeric':
                df[column] = pd.to_numeric(df[column], errors='coerce')
            elif dtype == 'datetime':
                df[column] = pd.to_datetime(df[column], errors='coerce')
            else:
                df[column] = df[column].astype(dtype)

        # 不正データの削除
        if 'filters' in self.config:
            for column, condition in self.config['filters'].items():
                df = df.query(condition)

        # df = df.dropna()  # NaNが残っている行を削除
        return df