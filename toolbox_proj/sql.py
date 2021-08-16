import sqlite3

def get_data_with_sql(database, fieldnames, table_name, conditions):
    #executes SQL query and returns every selected lines
    ##fieldnames have to be provided within a list
    fieldnames_string = ','.join(fieldnames)
    query = 'SELECT '+ fieldnames_string +' from '+ table_name +' WHERE '+ conditions

    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results