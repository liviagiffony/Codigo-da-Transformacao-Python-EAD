import sqlite3


conn = sqlite3.connect('alls_sall.db')
cursor = conn.cursor()


cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS tasks (
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    task_mane TEXT NOT NULL,
    data_fish NUMBER NOT NULL,
    data_star NUMBER NOT NULL,
    tarefa_about STRING NOT NULL
    )
'''
)
CONN.COMMIT