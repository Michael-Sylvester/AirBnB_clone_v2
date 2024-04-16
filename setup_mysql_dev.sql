-- Prepares a MySQL server for AireBnB_v2
-- New Database: hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- New User: hbnb_dev with password: hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- All privileges on databse to new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
