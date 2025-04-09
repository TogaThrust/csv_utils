import pandas as pd


def rchop(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s

def main():
    path = "./SAP_GL_ITEM_Adjustments_2017-2022.csv"
    date_columns = ["DATE_PERIOD", "POSTING_DATE", "DOCUMENT_DATE"]

    df = pd.read_csv(path)

    for col in date_columns:
        df[col] = pd.to_datetime(df[col], format="%d/%m/%Y")

    df.to_csv(rchop(path, ".csv") + "converted.csv")

if __name__ == "__main__":
    main()