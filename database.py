import psycopg2


def insert_transaction(sender: str, recipient: str, amount: int):
    conn = psycopg2.connect(database="postgres", user="postgres", password="Ruslan5655",
                            host="127.0.0.1", port="5432")
    if sender == "" or recipient == "" or amount == 0:
        print("Enter wrong transaction data")

    cursor = conn.cursor()

    sqlInsert = "INSERT INTO Transactions(sender,recipient,amount) VALUES(%s,%s,%s);"
    records = (sender,recipient,amount)
    cursor.execute(sqlInsert, records)
    conn.commit()

    count_records = cursor.rowcount
    print(count_records," Records Success added")

    cursor.close()
    conn.close()
