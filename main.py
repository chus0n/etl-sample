from csv_importer import CSVImporter
from data_processor import DataProcessor
from config_manager import ConfigManager

# デフォルト設定
default_config = {
    'fillna_values': {},
    'dtypes': {},
    'filters': {}
}

# 設定管理クラスを初期化
config_manager = ConfigManager(default_config, config_dir="configs")

# データベース接続情報
db_config = {
    'host': 'localhost',
    'user': 'test_user',
    'password': 'test_password',
    'database': 'test_db',
    'port': 3306
}

def process_csv_files(file_table_map):
    """
    複数CSVファイルを処理し、対応するテーブルにインポート
    """
    importer = CSVImporter(db_config)

    for file_path, table_name in file_table_map.items():
        # テーブルごとの設定を取得
        config = config_manager.load_table_config(table_name)
        processor = DataProcessor(config)

        # CSVを読み込み、処理してインポート
        for df in importer.read_csv(file_path, 10000, config.get('dtypes', {})):
            if df is not None:
                clean_df = processor.clean_data(df)
                importer.import_to_database(clean_df, table_name)

# メイン処理
if __name__ == '__main__':
    file_table_map = {
        './data/sample.csv': 'sample',
    }

    process_csv_files(file_table_map)