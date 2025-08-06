from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from configs.databaseInfo import driver, hostName, port, databaseName, userName, password

def connectToDB(connection_name):
    connection_name = connection_name
    if QSqlDatabase.contains(connection_name):
        return QSqlDatabase.database(connection_name)
    con = QSqlDatabase.addDatabase(driver, connection_name)
    con.setHostName(hostName)
    con.setPort(port)
    con.setDatabaseName(databaseName)
    con.setUserName(userName)
    con.setPassword(password)

    if not con.open():
        print("Error connecting to database")
        return False
    else:
        return QSqlDatabase.database(connection_name)

def createDB():
    con = connectToDB(databaseName)

    createTableQuery = QSqlQuery(con)
    createTableQuery.exec("""
        CREATE TABLE IF NOT EXISTS currentInventory
        (
            identifier SERIAL PRIMARY KEY,
            itemName VARCHAR (255),
            itemDescription TEXT,
            itemType VARCHAR (255),
            itemAge VARCHAR (255),
            itemPrice VARCHAR (255),
            itemImageUpload BYTEA
        );
    """)

def modifyDB(connection, itemName, itemDescription, itemType, itemAge, itemPrice, imageBytes):
    query = QSqlQuery(connection)
    query.prepare("""
                  INSERT INTO currentInventory (itemname,
                                                itemdescription,
                                                itemtype,
                                                itemage,
                                                itemprice,
                                                itemimageupload)
                  VALUES (?, ?, ?, ?, ?, ?);
                  """)
    query.addBindValue(itemName)
    query.addBindValue(itemDescription)
    query.addBindValue(itemType)
    query.addBindValue(itemAge)
    query.addBindValue(itemPrice)
    query.addBindValue(imageBytes)

    if not query.exec():
        createDB()
        print("Attempt failed, attempting to create the table.")
        modifyDB(connection, itemName, itemDescription, itemType, itemAge, itemPrice, imageBytes)
        return True
    else:
        print("Query succeeded.")
        QSqlDatabase.removeDatabase(databaseName)
        return None

# TODO
def getInfo(connection):
    results = []
    query = QSqlQuery(connection)
    query.prepare("""SELECT * FROM currentInventory""")
    if query.exec():
        while query.next():
            # Get values by index (0-based)
            identifier = query.value(0)  # First column
            itemName = query.value(1)  # Second column
            itemDescription = query.value(2)
            itemType = query.value(3)
            itemAge = query.value(4)
            itemPrice = query.value(5)
            imageBytes = query.value(6)
            # COME BACK AND ADD IMAGEBYTES EXPORT SUPPORT
            results.append((identifier, itemName, itemDescription, itemType, itemAge, itemPrice))

    return results
