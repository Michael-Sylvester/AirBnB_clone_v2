-- Prepares a MySQL test server for AirBnB_v2
-- New Database: hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- New User: hbnb_test with password: hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- All privileges on databse to new user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
