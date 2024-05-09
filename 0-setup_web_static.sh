#!/usr/bin/env  bash
#Install Nginx is it is not installed and configure the files.
# Check if Nginx is installed
if ! [ -x "$(command -v nginx)" ]; then
  sudo apt-get update
  sudo apt-get install -y nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing
sudo echo "<html><head><title>Test Page</title></head><body><h1>This is a test page</h1></body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link for test directory named current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ubuntu user and group ownership of /data
sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration if necessary
nginx_config="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" $nginx_config; then
  sudo sed -i '/^server {/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $nginx_config
  sudo service nginx restart
fi