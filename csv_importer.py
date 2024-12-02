import pandas as pd
from sqlalchemy import create_engine

class CSVImporter:
    def __init__(self, db_config):
        """
        データベース接続情報を初期化
        """
        self.engine = create_engine(
            f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
        )

    def import_to_database(self, df, table_name, if_exists='append'):
        """
        データフレームを指定したテーブルにインポート
        """
        try:
            df.to_sql(table_name, con=self.engine, if_exists=if_exists, index=False)
            print(f"データがテーブル '{table_name}' にインポートされました。")
        except Exception as e:
            print(f"データベースへのインポートエラー: {e}")

    def read_csv(self, file_path):
        """
        CSVファイルを読み込む
        """
        try:
            df = pd.read_csv(file_path)
            print(f"CSVファイル '{file_path}' を読み込みました。")
            return df
        except Exception as e:
            print(f"CSV読み込みエラー: {e}")
            return None