import os, json

def load(path="config.json"):
    config_envs = os.environ.get("CONFIG_ENVIRONMENTS")
    
    if config_envs is None:
        config_envs = [ "development", "qa", "production" ]
    else:
        config_envs = str.split(config_envs, ",")

    env = os.environ.get("PYTHON_ENV") or "development"
    config = json.loads(open(path, "r").read())
    config[env] = config.get(env) or {}

    for k in config.keys():
        if k not in config_envs:
            config[env][k] = config[k]
    
    return config[env]

        
