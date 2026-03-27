import sqlite3, tempfile, os
from tests.conftest import init_test_db

fd, path = tempfile.mkstemp()
print('db path', path)
init_test_db(path)
conn = sqlite3.connect(path)
c = conn.cursor()
try:
    c.execute("INSERT INTO movimientos_consumo (fecha_consumo,item_sku,cantidad_consumida,categoria_item) VALUES ('2023-01-15','ABC',1,'Cat1')")
    conn.commit()
    print('insert succeeded')
except Exception as e:
    print('insert failed', e)
finally:
    conn.close()
    os.close(fd)
    os.unlink(path)
