#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import put
from fabric.api import env
from fabric.api import local
from fabric.api import run

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
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
    if local("tar -cvzf {} web_static".format(fil)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """Archive distributd to a web server"""
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    n = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(n)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(n)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, n)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(n, n)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(n)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(n)).failed is True:
        return False
    return True


def deploy():
    """Distribute & create an archive to web server"""
    fil = do_pack()
    if fil is None:
        return False
    return do_deploy(fil)
