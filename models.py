import timesfm

def get_model(model_name: str):
    """Load pretrained time series foundation model."""
    if "timesfm" in model_name.lower():
        model = timesfm.TimesFM_2p5_200M_torch.from_pretrained(model_name)
        model.compile(timesfm.ForecastConfig(
            max_context=512,
            max_horizon=20,
            normalize_inputs=True
        ))
        return model
    else:
        raise ValueError(f"Model {model_name} not yet implemented. Add support for FinCast, Chronos, etc.")
