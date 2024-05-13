#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static
folder of the AirBnB Clone repo.
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns:
        Path to the generated archive if successful, None otherwise.
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate timestamp for archive name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Create the .tgz archive with the timestamp in its name
        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_name))

        return archive_name
    except Exception as e:
        print("An error occurred:", e)
        return None
