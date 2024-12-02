# ELT SAMPLE

## overview

ETL学習用のスクリプト

- YAMLで定義した情報を元にCSVをインポートする

## requirements

- python3.9+
- pandas
- sqlalchemy
- pymysql
- pyyaml

## setup

```sh
python3 -m venv venv
pip install -r ./requirements.txt
```

## usage

1. configsに型チェック用のyamlを作成する
2. dataにcsvを配置
3. main.pyに取り込むファイルを設定
4. 下記を実行

```sh
python3 ./main.py
```

## todo

- [ ] CSVの読み込みをチャンクに変えたのでメッセージ周りを修正する
- [ ] 取り込みファイルの定義をmain.pyから外出しにする
- [ ] 接続文字列の外出し
- [ ] DBのドライバを変更できるようにする
