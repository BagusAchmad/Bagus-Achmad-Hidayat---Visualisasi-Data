import pandas as pd

def convert_to_number(x):
    """Convert string like 1.2B / 500M / 10K / 1,234 to float"""
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


df = pd.read_csv("Dataset/coin_Bitcoin.csv")

# rename columns -> lowercase
df.columns = df.columns.str.lower().str.replace(" ", "_")

# parse date
df["date"] = pd.to_datetime(df["date"])

# sort by date
df = df.sort_values("date")

# convert numeric columns
for col in ["open", "high", "low", "close", "volume", "marketcap"]:
    if col in df.columns:
        df[col] = df[col].apply(convert_to_number)

# drop missing essential
df = df.dropna(subset=["date", "close"])

# add coin label
df["coin"] = "Bitcoin"

df.to_csv("Output/btc_cleaned.csv", index=False)
print("✅ Output/btc_cleaned.csv berhasil dibuat")
