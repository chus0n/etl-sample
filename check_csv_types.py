import pandas as pd
import sys

def check_csv_column_types_with_chunks(csv_file_path, chunk_size=100000):
    inferred_types = None

    try:
        # チャンクごとに読み込む
        for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
            current_types = chunk.dtypes
            
            # 初回は型を記録
            if inferred_types is None:
                inferred_types = current_types
            else:
                # 型が一致するか確認
                if not current_types.equals(inferred_types):
                    print("Warning: Inconsistent column types detected across chunks.")
                    print("Previous types:")
                    print(inferred_types)
                    print("Current types:")
                    print(current_types)
                    analyze_object_columns(chunk)
                    return

        print("Column Type Check Result (All Chunks Consistent):")
        for column, dtype in inferred_types.items():
            print(f"Column: {column}, Data Type: {dtype}")

    except Exception as e:
        print(f"Error: {e}")

def analyze_object_columns(df):
    """
    すべてのobject型列について、詳細情報を一括で確認する
    """
    object_columns = df.select_dtypes(include=['object']).columns
    for col in object_columns:
        print(f"\nAnalysis for column: {col}")
        unique_types = df[col].map(type).value_counts()
        print(f"- Unique data types:\n{unique_types}")
        print(f"- Non-string values:\n{df[col][~df[col].apply(lambda x: isinstance(x, str))].head()}")
        if df[col].apply(lambda x: isinstance(x, str)).all():
            print(f"- Max string length: {df[col].dropna().apply(len).max()}")
        print(f"- Sample values:\n{df[col].head()}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python check_csv_types.py <csv_file_path>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    # check_csv_column_types_with_chunks(csv_file_path)
    df = pd.read_csv(csv_file_path)
    analyze_object_columns(df)