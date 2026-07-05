from src.data_loader import load_and_prepare
import yaml

if __name__ == "__main__":
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    
    df = load_and_prepare(config['ticker'], config['start_date'], config['interval'])
    df.to_csv("data/raw_data.csv")
    print(f"Downloaded {len(df)} rows for {config['ticker']}")
