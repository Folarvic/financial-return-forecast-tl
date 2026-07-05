# Financial Return Forecasting with Transfer Learning

Modern ML pipeline for forecasting asset returns using Time Series Foundation Models (TimesFM, FinCast, Kronos, etc.).

## Features
- Data collection (Yahoo Finance)
- Feature engineering
- Transfer learning / fine-tuning
- Walk-forward validation
- VectorBT backtesting
- MLflow tracking
- Docker support

## Quick Start
```bash
pip install -r requirements.txt
python scripts/download_data.py
python main.py
```

See `notebooks/` for EDA.
