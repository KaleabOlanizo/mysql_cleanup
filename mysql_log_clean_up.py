import subprocess
import argparse

def clean_up_log(mysql_username:str, password:str):
    script_content = f"""
    #!/bin/bash

    # MySQL credentials
    MYSQL_USER="{mysql_username}"
    MYSQL_PASSWORD="{password}"

    # Directory to archive logs
    ARCHIVE_DIR="/path/to/archive"

    # MySQL binary log directory
    MYSQL_LOG_DIR="/var/lib/mysql"

    # Clean and archive binary logs
    mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e "PURGE BINARY LOGS BEFORE NOW() - INTERVAL 7 DAY;"
    tar -czvf "$ARCHIVE_DIR/mysql_logs_$(date +\%Y\%m\%d).tar.gz" "$MYSQL_LOG_DIR"

    # Remove old archived logs (optional)
    find "$ARCHIVE_DIR" -type f -name "mysql_logs_*" -mtime +7 -exec rm {{}} \;
    """

    # Save the script to a file
    script_path = "./script.sh"
    with open(script_path, "w") as script_file:
        script_file.write(script_content)

    # Set permissions
    subprocess.run(["chmod", "+x", script_path])

    # Run the script
    subprocess.run(["bash", script_path])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create and run MySQL log cleaning and archiving script.")
    parser.add_argument("--username", required=True, help="MySQL username")
    parser.add_argument("--password", required=True, help="MySQL password")

    args = parser.parse_args()

    clean_up_log(args.username, args.password)