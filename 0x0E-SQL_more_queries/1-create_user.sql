-- Create user with password & all PRIVILEGES


CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* To 'user_0d_1'@'localhost'
WITH GRANT OPTION;
FLUSH PRIVILEGES;
