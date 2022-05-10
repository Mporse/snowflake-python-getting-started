# Snowflake Quickstarts: Getting Started with Python
Code written during the "Getting Started with Python" Snowflake Quickstart Guide.

## Initial Setup
1. The Python version should be **3.5 or higher**. Run the following to check the version number:  
```bash
python --version
```

2. Then, install the Snowflake Connector for Python (along with the Jupyter Notebook packages):
```bash
pip install --upgrade snowflake-connector-python jupyterlab notebook
```

3. On Linux, you also need to install the following dependencies:
- `libm-devel`
- `openssl-devel`

4. Lastly, make sure to create a file `creds.txt` in the `files` folder (so `files/creds.txt`) that contains the login credentials for your account. It should contain the following, exactly as typed below:
```
username=xxx
password=yyy
accountname=zzz
```

Replace the `xxx` with your Snowflake username, the `yyy` with your Snowflake password, and the `zzz` with your Snowflake account name. The code in the script and Jupyter Notebook should then perform the login process automatically.

## Check the Installation of the Snowflake Connector Package
Make sure that the `snowflake-connector-python` package is installed correctly. To do so, run the script `validate_installation.py` in the `files` folder.

## Go Through the Code for the Tutorial
Finally, go through the various cells in the `snowflake-getting-started-with-python.ipynb` notebook to try out the tutorial!


## Supplementary Info
The script and notebook were tested on WSL running Ubuntu 20.04.4 LTS.
