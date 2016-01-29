import os, json

def load(path):
    env = os.environ.get("PYTHON_ENV") or "development"
    return json.loads(open(path, "r").read()).get(env)

        
