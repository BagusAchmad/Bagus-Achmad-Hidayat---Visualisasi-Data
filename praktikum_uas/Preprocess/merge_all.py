import pandas as pd

btc = pd.read_csv("Output/btc_cleaned.csv")
eth = pd.read_csv("Output/eth_cleaned.csv")
bnb = pd.read_csv("Output/bnb_cleaned.csv")

df = pd.concat([btc, eth, bnb], ignore_index=True)

# urutkan
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["coin", "date"])

# transformasi: daily return (untuk volatilitas)
df["daily_return"] = df.groupby("coin")["close"].pct_change() * 100

df.to_csv("Output/crypto_merged.csv", index=False)
print("✅ Output/crypto_merged.csv berhasil dibuat")
