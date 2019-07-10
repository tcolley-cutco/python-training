import sys

# Handles all the db2 connection stuff rather than having it right in the flask application

# TODO Is it possible to make a Connection program that handles the disparity between the midrange and local so
# TODO that you can actually do local testing as intended? Maybe load different drivers based on os.name and then
# TODO if you're on local, do an outbound connection? There's still a roadblock with connecting over the wire to the
# TODO 400 but that must be solvable if programs can be run from the Linux box targeting the 400 DB. If not, can I rip
# TODO the driver out of the 400 directly and then modify it to run in NT, or is there possibly an open-source driver?

on_400 = sys.platform == 'aix6'

conn = None
if on_400:
    # DB imports
    import ibm_db_dbi as dbi
    from ibm_db_dbi import SQL_ATTR_DBC_SYS_NAMING, SQL_TRUE
    from ibm_db_dbi import SQL_ATTR_TXN_ISOLATION, SQL_TXN_NO_COMMIT


def fetch_db2_connection():

    db2_conn = None
    if on_400:

        options = {
            SQL_ATTR_TXN_ISOLATION: SQL_TXN_NO_COMMIT,
            SQL_ATTR_DBC_SYS_NAMING: SQL_TRUE,
        }
        db2_conn = dbi.connect()
        db2_conn.set_option(options)

    return db2_conn


def fetch_db2_connection_with_credentials(username, password):
    """
    THROWS ibm_db_dbi.Error if the user and pass do not match the table
    Overloaded version of this, allows authentication against user/pass
    :param username: The provided 400 user
    :param password: The provided 400 password
    :return: A cursor for this connection. Throws exception on failure
    """
    return dbi.connect(user=username, password=password)




