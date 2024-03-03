import yaml


def load_config():
    """Load configuration from the YAML file.

    Returns:
        dict: Configuration data.
    """
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)


config = load_config()


def get_api_key():
    """Get the alphaVantage API Key stored in config.yaml

    Returns:
        str: API Key for alphaVantage API
    """
    return config["alphavantageAPI"]["key"]
