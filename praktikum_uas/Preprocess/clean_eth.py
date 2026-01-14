import pandas as pd

def convert_to_number(x):
    if pd.isna(x):
        return None
    x = str(x).replace(",", "").strip()

    if x.endswith("B"):
        return float(x[:-1]) * 1e9
    if x.endswith("M"):
        return float(x[:-1]) * 1e6
    if x.endswith("K"):
        return float(x[:-1]) * 1e3

    try:
        return float(x)
    except:
        return None


df = pd.read_csv("Dataset/coin_Ethereum.csv")

df.columns = df.columns.str.lower().str.replace(" ", "_")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

for col in ["open", "high", "low", "close", "volume", "marketcap"]:
    if col in df.columns:
        df[col] = df[col].apply(convert_to_number)

df = df.dropna(subset=["date", "close"])
df["coin"] = "Ethereum"

df.to_csv("Output/eth_cleaned.csv", index=False)
print("✅ Output/eth_cleaned.csv berhasil dibuat")
