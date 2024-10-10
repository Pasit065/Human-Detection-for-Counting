class SqlQueries():
    def __init__(self):
        self.CREATE_INTRUDERS_TABLE_IF_NOT_EXISTS = """
            CREATE TABLE IF NOT EXISTS intruders(
            no INTEGER PRIMARY KEY AUTOINCREASEMENT,
            the_amount_of_intruders INTEGER,
            date TEXT,
            time TEXT
            )"""

        self.INSERT_NEW_INTRUDER_STATEMENT = f"""
                INSERT INTO intruders (the_amount_of_intruders, date, time)
                VALUES """