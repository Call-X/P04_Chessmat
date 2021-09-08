import sqlite3
from Controls.control_player import Player

class DataBaseService:
    def __init__(self):
        self.connection = sqlite3.connect("base_db.db")
        self.cursor = self.connection.cursor()

        try:

            player_list = {}
            # tournament_list = []

            req = self.cursor.executemany("INSERT INTO table_players VALUES({},{},{},{},{})", player_list)
            self.connection.commit()
            print("{ New Player ADD }")
            for row in req.fetchall():
                print(row[1])

        except Exception as e:
            print("[ERREUR]", e)
            self.connection.rollback()
        finally:
            self.connection.close()










# try:
#     conn = MC.connect(host="localhost", database="datest", user="root", pasword="")
#     cursor = conn.cursor()
#     req = "Select * From playertable"
#     cursor.execute(req)
#
#     playerlist = cursor.fetchall()
#
#     for player in playerlist:
#
# except MC.Error as err:
#     print(err)
# finally:
#     if(conn.is_connected()):
#         cursor.close()
#         conn.close()
