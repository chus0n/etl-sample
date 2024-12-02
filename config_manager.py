import yaml

class ConfigManager:
    def __init__(self, default_config, config_dir):
        self.default_config = default_config
        self.config_dir = config_dir
    
    def load_table_config(self, table_name):
        config_file = f"{self.config_dir}/{table_name}.yaml"
        try:
            with open(config_file, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"設定ファイルが見つかりません: {config_file}")
            return {}