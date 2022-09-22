# Bank class
# user has name, phone number, pin
# user details are entered by user
# account number is generated automatically
# user details and transaction history are stored in mysql database
# user can create account, deposit, withdraw, transfer, 
# check balance, check history, and exit
# user can only withdraw if they have enough money in their account
# user can only transfer if they have enough money in their account
# user can only access their own account
# user can only access their own transaction history
# user can only access their own account number


# menu to 1.create, 2.login or 3.exit
# 1. create with name, phone, pin; create acc_number; create new bank instance and send new_user to bank table
# 2. login using account number and pin; compare to what's in the bank table and return data
# menu to 1.deposit, 2.withdraw, 3.transfer, 4.check balance, 5.check history
#   1. ask amount and add it to user instance and update bank,transactions tables
#   2. ask amount and remove it from user instance and update bank,transactions tables
#   3. ask amount and remove it from user instance; add it to other_user instance and update tables
#   4. query bank table for balance
#   5. query transactions table for rows
# 3. system exit

# The essence of using a class rather than a function or regular code is basically to avoid repetition in the work; so to create a self-contained and sustained model which will be recreated so many times, we need to bundle all this functionality (variables and functions) into one module.

# MODULES:
# PyMySQL - to connect to MySQL database
# mysql_connector_python - a self-contained Python driver for communicating with MySQL servers
# secrets - random numbers
# hashlib - to hash pin
# datetime - to record dates of transaction
# sys - to exit running program
# os.system - to clear cmd

# BANK CLASS
# attributes - name, phone number, pin, account_number, balance
# methods - create new bank account instance in db [create db, connect to db], deposit, withdraw, check balance, transfer, check history, login, exit

# MYSQL
# config = {
#   'user': 'scott',
#   'password': 'password',
#   'host': '127.0.0.1',
#   'database': 'employees',
#   'raise_on_warnings': True
# }
# conn = mysql.connector.connect(**config)
# conn.close()
# fetchone() retrieves a single item, when you know the result set contains a single row.
# fetchall() retrieves all the items, when you know the result set contains a limited number of rows that can fit comfortably into memory.
# fetchmany() is the general-purpose method when you cannot predict the size of the result set: you keep calling it and looping through the returned items, until there are no more results to process.
# use string literals to create sql statements
# after updating the db with insert or update, commit the conn

# From what has been established, when we login in, the program creates an empty instance that only interacts with the database when we want it to, we need an empty instance that doesn't immediately interact with the db to set the account_number_login parameter, which can only be updated after login.
# This instance won't interfere with the db but its existence will enable us to communicate with the db where all queries used will use the account_number_login parameter we set on login.
# We will also need its balance parameter which is what will keep changing after the transactions
# If we excluded this, to create a global variable, we would essentially abandon the whole class and use individual functions and variables, that will be hard to keep track of, and the code will be completely disorganised, lose the modular ability of python.