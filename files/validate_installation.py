# Import modules.
import snowflake.connector
import sys
import os.path as path

# Get current working directory.
file_dir = path.dirname(path.abspath(__file__))

# Get credentials from creds.txt file.
with open(f"{file_dir}/creds.txt", "r") as creds_file:
    creds = [cred.strip() for cred in creds_file.readlines()]
    creds = {cred.split("=")[0]:cred.split("=")[1] for cred in creds}

# Get Snowflake connector version.
try:
    ctx = snowflake.connector.connect(
        user = creds["username"],
        password = creds["password"],
        account = creds["accountname"]
    )
except:
    print("Couldn't connect to the account - did you type the correct credentials?")
    sys.exit()


cursor = ctx.cursor()

try:
    cursor.execute("SELECT current_version()")
    row = cursor.fetchone()
    print(row[0])
except:
    print("Couldn't retrieve current version.")
finally:
    cursor.close()

ctx.close()
