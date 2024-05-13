#!/usr/bin/python3
"""
Fabric script to deploy an archive to web servers.
"""
from fabric.api import env, put, run
import os

# Define the list of web servers
env.hosts = ['54.160.115.226', '100.25.139.174']
env.key_filename = '~/.ssh/0-RSA_public_key'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    Args:
        archive_path: Path to the archive to be deployed.
    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    if not os.path.exists(archive_path):
        print("Archive not found.")
        return False

    try:
        # Upload the archive to /tmp/ directory on the web servers
        put(archive_path, '/tmp/')

        archive_filename = os.path.basename(archive_path)
        release_folder = '/data/web_static/releases/{}'.format(
            archive_filename[:-4])
        run('sudo mkdir -p {}'.format(release_folder))
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        # Delete the archive from the web servers
        run('sudo rm /tmp/{}'.format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        current_link = '/data/web_static/current'
        run('if [ -L {} ]; then sud rm {}; fi'.format(current_link, current_link))

        # Create a new symbolic link for the new version
        run('sudo ln -s {} {}'.format(release_folder, current_link))

        print("New version deployed successfully.")
        return True
    except Exception as e:
        print("An error occurred:", e)
        return False
