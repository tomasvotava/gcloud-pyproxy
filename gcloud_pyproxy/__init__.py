from subprocess import Popen, PIPE
import json
from shutil import which

class GCloudError(Exception):
    pass

def gcloud_proxy(command, *args, **kwargs):
    f = Popen(" ".join([
        "gcloud",
        command,
        *["\"{}\"".format(arg) for arg in args],
        *["--{key}=\"{value}\"".format(key=key, value=val) for key, val in kwargs.items()],
        "--format=json"
    ]),
    stdout=PIPE,
    stderr=PIPE,
    shell=True
    )
    if f.wait() == 0:
        return json.loads(f.stdout.read().decode("utf-8"))
    else:
        raise GCloudError(f.stderr.read().decode("utf-8"))

class GCloud:
    def __init__(self):
        pass
    def __getattribute__(self, attr):
        attributes = attr.split("_")
        if attributes[-1] == "":
            attributes.pop(-1)
        def run_gcloud(*args, **kwargs):
            return gcloud_proxy(*attributes, *args, **kwargs)
        return run_gcloud

if which("gcloud") == None:
    raise FileNotFoundError("\'gcloud\' command was not found in your environment. Ensure it is installed and set up properly.")

if __name__ == '__main__':
    gc = GCloud()
    print(gc.projects_list())

__all__ = [GCloud, GCloudError]