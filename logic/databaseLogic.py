from PyQt5.QtSql import QSql, QSqlQuery, QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMessageBox

def modifyDB(query):

    con = QSqlDatabase.addDatabase('QPSQL')
    con.setHostName("135.148.13.227")
    con.setPort(5432)
    con.setDatabaseName("postgres")
    con.setUserName("postgres")
    con.setPassword("password")

    if not con.isValid():
        print("Error:", con.lastError().text())
        return False

    createTableQuery = QSqlQuery(con)
    createTableQuery.exec("""
        CREATE TABLE IF NOT EXISTS currentInventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            itemName VARCHAR(255) NOT NULL,
            itemDescription TEXT NOT NULL,
            itemType VARCHAR(255) NOT NULL,
            itemAge VARCHAR(255) NOT NULL,
            itemPrice VARCHAR(255) NOT NULL,
            itemImageUpload BYTEA
        );
    """)

    print("Table exists")
    userInsertQuery = QSqlQuery(con)
    userInsertQuery.exec()

    con.commit()
    con.close()

def getInfo(query):
    con = QSqlDatabase.addDatabase('QPSQL')
    con.setHostName("135.148.13.227")
    con.setPort(5432)
    con.setDatabaseName("postgres")
    con.setUserName("postgres")
    con.setPassword("password")

    if not con.isValid():
        print("Error:", con.lastError().text())
        return False

    infoQuery = QSqlQuery(con)
    infoQuery.exec(query)

    info = []
    while infoQuery.next():
        id = infoQuery.value(0)
        itemName = infoQuery.value(1)
        itemDescription = infoQuery.value(2)
        itemType = infoQuery.value(3)
        itemAge = infoQuery.value(4)
        itemPrice = infoQuery.value(5)
        itemImageUpload = infoQuery.value(6)
        info.append([id, itemName, itemDescription, itemType, itemAge, itemPrice, itemImageUpload])

    con.commit()
    con.close()
    return info


# TEST CASES TO BE REMOVED

# modifyDB("""
#     INSERT INTO currentInventory (id, itemName, itemDescription, itemType, itemAge, itemPrice, itemImageUpload)
#     VALUES (DEFAULT, 'TestName', 'TestDesc', 'TestType', '25 years', '$25.25', '../assets/antique.png');
# """)

# results = getInfo("""
#    SELECT id, itemName, itemDescription, itemType, itemAge, itemPrice, itemImageUpload FROM currentInventory;
# """)
# if not results:
#     print("Nothing Found, Query Unsuccessful")
# for i in results:
#     print(i)