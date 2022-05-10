# Import modules.
import snowflake.connector
import sys

# Get Snowflake connector version.
username = input("Type your Snowflake username: ")
password = input("Type your Snowflake password: ")
accountname = input("Type your Snowflake account name: ")

try:
    ctx = snowflake.connector.connect(
        user = username,
        password = password,
        account = accountname
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