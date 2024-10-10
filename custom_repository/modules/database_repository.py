class DatabaseRepository():
    def create_table_if_not_exists(self, create_table_querie, cur, con):
        cur.execute(create_table_querie)
        con.commit()

    def insert_new_intruder(self, insert_new_intruder_querie, cur, con, new_intruder_data):
        inserted_data  = f"({new_intruder_data["total"]}, '{new_intruder_data["date"]}', '{new_intruder_data["time"]}')"
        cur.execute(insert_new_intruder_querie + inserted_data)
        con.commit()

    def get_total_intruders_in_specific_date(self, select_all_from_intruders_table_querie, cur, con, date):
        cur.execute(select_all_from_intruders_table_querie + f"\n\nWHERE date = '{date}'")
        con.commit()

        return cur.fetchall()[0][0]

