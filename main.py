from src.data_loader import load_and_prepare
from src.features import engineer_features
from src.models import get_model
import yaml

if __name__ == "__main__":
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    
    df = load_and_prepare(config['ticker'], config['start_date'], config['interval'])
    df = engineer_features(df)
    
    print(f"Data shape: {df.shape}")
    print(df.tail())
    
    model = get_model(config['model_name'])
    print("✅ Model loaded successfully!")
    print("Ready for fine-tuning and forecasting.")
