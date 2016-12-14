import os

def resolve_env_var(env, mapping):
    return os.getenv(mapping.get(env, env))
