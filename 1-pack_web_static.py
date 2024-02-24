#!/usr/bin/python3
# Fabfile that generate a .tgz archive from contents of web_static.
import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """Tar gzipped archive of the directory web_static creatd"""
    dat = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dat.year,
                                                         dat.month,
                                                         dat.day,
                                                         dat.hour,
                                                         dat.minute,
                                                         dat.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return filmport os.path
