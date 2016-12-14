import os, sys, argparse, pickle, md5
import json

from sources import aws

sys.stdin = open('/dev/tty')

MD5_PATH = os.path.join(os.path.dirname(__file__), "..", "md5s.pkl")
MD5_DICT = {}

METHODS = {
    "aws": aws
}

try:
    MD5_DICT = pickle.load(open(MD5_PATH, 'rb'))
except:
    pass

def sync(mode):
    root, configs = _get_privvy_config()
    for _file, info in configs.items():
        source = info["source"]
        filepath, exists, changed = _check_file(root, info["path"], source)

        if exists and not changed and mode == "push":
            print("{filepath} exists and has not changed".format(filepath=filepath))
            continue

        if mode == "push":
            if not exists:
                continue

            reply = raw_input("[Privvy] Private file {path} has been changed. Push new changes?".format(
                path=filepath
            ))

            if reply.lower() in [ "n", "no", "q", "c" ]:
                continue

        method = _get_source_method(source)
        file_changed = getattr(method, mode)(filepath, source, mapping=info.get("env_mapping", {}))
        if file_changed:
            MD5_DICT[source] = md5.md5(open(filepath, "rb").read()).hexdigest()

    pickle.dump(MD5_DICT, open(MD5_PATH, 'wb'))
    return

def _get_source_method(source):
    # Hard coded to only support aws
    source_type = "aws"
    method = METHODS.get(source_type)
    if not method:
        raise NotImplementedError(source_type)
    return method

def _check_file(root, filepath, source):
    resolved = os.path.join(root, filepath)

    if not os.path.exists(resolved):
        return resolved, True, False

    current_md5 = md5.md5(open(resolved, "rb").read()).hexdigest()
    saved_md5 = MD5_DICT.get(source)

    return resolved, True, current_md5 != saved_md5

def _get_privvy_config():
    args = _parse_args()
    filepath = args.file or ".privvy"
    if not os.path.exists(filepath):
        if args.auto:
            sys.exit(0)
        else:
            print("{path} does not exist.".format(path=filepath))
            print("Could not find the privvy config")
            sys.exit(1)

    return os.path.dirname(filepath), json.load(open(filepath, "rb"))

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, help="privvy filepath")
    parser.add_argument("--auto", "-a", action="store_true", help="only used by git hooks")

    return parser.parse_args()
