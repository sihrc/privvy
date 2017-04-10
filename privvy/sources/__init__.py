import os

def resolve_env_var(env, mapping):
    env_var = mapping.get(env, env)
    if env_var not in os.environ:
        print("Warning: {env} environment variable is missing".format(env=env_var))
    return os.getenv(env_var)
