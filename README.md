# MySQL Cleanup
This is a simple Python script that creates a Bash script file with MySQL credentials as arguments, sets the file permissions, and runs the script.
The script cleans and archives MySQL logs. This script assumes you want ot rotate binary logs. Feel free to modifiy it based on the specific log types. 

## How to run it

`` python mysql_log_clean_up.py --username your_mysql_user --password your_mysql_password ``
