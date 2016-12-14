import re

from boto.s3.connection import S3Connection
import os

from . import resolve_env_var

S3_PATTERN = re.compile("s3:/+(?P<bucket>.*?)/(?P<path>.*)")

def pull(filepath, source, mapping):
    key = _connect(source, mapping)
    key.get_contents_to_filename(filepath)
    print("Pulled contents from {src} to {dst}".format(
        src=source,
        dst=filepath
    ))
    return True

def push(filepath, source, mapping):
    key = _connect(source, mapping)
    key.set_contents_from_filename(filepath)
    print("Pushed contents from {src} to {dst}".format(
        src=filepath,
        dst=source
    ))
    return True

def _connect(source, mapping):
    key_id = resolve_env_var("AWS_ACCESS_KEY_ID", mapping=mapping)
    secret_key = resolve_env_var("AWS_SECRET_ACCESS_KEY", mapping=mapping)
    conn = S3Connection(key_id, secret_key)
    bucket, path = _parse_bucket(source)
    bucket = conn.get_bucket(bucket)
    key = bucket.get_key(path, validate=False)
    return key

def _parse_bucket(source):
    matched = S3_PATTERN.match(source)
    if not matched:
        raise ValueError("{source} is not a valid s3 uri".format(source=source))

    return matched.group("bucket"), matched.group("path")
