#!/usr/bin/python3
# Out-of-date archives deletd by fabfile.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """Out-of-date archives deletd"""
    n = 1 if int(number) == 0 else int(number)

    archi5 = sorted(os.listdir("versions"))
    [archi5.pop() for k in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archi5 = run("ls -tr").split()
        archi5 = [a for a in archives if "web_static_" in a]
        [archi5.pop() for k in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
