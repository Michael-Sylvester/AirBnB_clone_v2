#!/usr/bin/env bash
#Install Nginx is not installed and prepare file structure
# Check if Nginx is installed
if ! [ -x "$(command -v nginx)" ]; then
  echo "Installing Nginx..."
  apt-get update
  apt-get install -y nginx
fi

# Create necessary directories if they don't exist
mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing
echo "<html><head><title>Test Page</title></head><body><h1>This is a test page</h1></body></html>" | tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data folder to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
sed -i '/^server {/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $nginx_config

# Restart Nginx
systemctl restart nginx
