from .errors import ConfigurationError


class ZengaPayConfig(object):

    def __init__(self, config):
        """
        config = {
            ENVIRONMENT: os.environ.get("APP_SETTINGS", "sandbox"),
            BASE_URL: os.environ.get("BASE_URL", "https://api.sandbox.zengapay.com/v1/"),
            API_TOKEN: os.environ.get("API_TOKEN")
        }
        """
        
        self.config = config
    
    @property
    def environment(self):
        env = self.config["ENVIRONMENT"]
        if not env:
            raise ConfigurationError("ENVIRONMENT is missing in configuration.")
        return env
    
    @property
    def base_url(self):
        base_url = self.config["BASEURL"]
        if not base_url:
            raise ConfigurationError("BASEURL is missing in configuration.")
        return base_url
    
    @property
    def api_token(self):
        token = self.config["API_TOKEN"]
        if not token:
            raise ConfigurationError("API_TOKEN is missing in configuration.")
        return 
