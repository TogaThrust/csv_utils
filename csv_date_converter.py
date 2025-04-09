import pandas as pd

def rchop(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s

def main():
    path = "./SAP_GL_ITEM_Adjustments_2017-2022.csv"
    date_columns = ["DATE_PERIOD", "POSTING_DATE", "DOCUMENT_DATE"]
    original_format = "%d/%m/%Y"
    # file read
    df = pd.read_csv(path)
    # transform
    df[date_columns] = df[date_columns].apply(lambda col: pd.to_datetime(col, format=original_format))
    # load
    df.to_csv(rchop(path, ".csv") + "converted.csv")

if __name__ == "__main__":
    main()