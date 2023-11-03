import sqlite3

try:
    sqlite_connection = sqlite3.connect('menu_db.db')
    cursor = sqlite_connection.cursor()

    sqlite_query = '''
    CREATE TABLE IF NOT EXISTS menu_db (
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price TEXT NOT NULL
    );
    '''

    cursor.execute(sqlite_query)

    print('success')

    cursor.close()
except sqlite3.Error as error:
    print('An error was occured: ', error)
finally:
    if(sqlite_connection):
        sqlite_connection.close()
        print('connection is closed')



def insert_query(name, description, price):
    try:
        sqlite_connection2 = sqlite3.connect('menu_db.db')
        cursor = sqlite_connection2.cursor()

        sqlite_query2 = '''
        INSERT INTO menu_db (name, description, price)
        VALUES (?,?,?);
        '''

        data_tuple = (name, description, price)

        cursor.execute(sqlite_query2, data_tuple)
        sqlite_connection2.commit()
    except sqlite3.Error as error:
        print('An error was occured: ', error)
    finally:
        if (sqlite_connection2):
            sqlite_connection2.close()
            print('connection is closed')


insert_query('Барбекю', 'соус барбекю; оливки; кукурудза; бекон; твердий сир; копчений сир', '234 грн')
insert_query('Маргарита', 'томатний соус, сир моцарела, помідори і базилік', '220 грн')
insert_query('Техас', 'Cоуc томатний, сир моцарела, куряче філе, шинка, помідори, соус солодкий чилі', '260 грн')
