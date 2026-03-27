import sqlite3, tempfile, os

fd, path = tempfile.mkstemp()
conn = sqlite3.connect(path)
c = conn.cursor()
c.executescript("""
        CREATE TABLE IF NOT EXISTS items (
            c1 INTEGER PRIMARY KEY,
            sku TEXT UNIQUE NOT NULL,
            nombre TEXT NOT NULL,
            stock_actual INTEGER DEFAULT 0,
            unidad_medida_nombre TEXT,
            ubicacion_nombre TEXT,
            categoria_nombre TEXT,
            subcategoria_nombre TEXT,
            proveedor_principal_nombre TEXT,
            precio_unitario_promedio REAL DEFAULT 0,
            ingresos_totales_historicos INTEGER DEFAULT 0,
            consumos_totales_historicos INTEGER DEFAULT 0,
            ajuste_total_historico INTEGER DEFAULT 0,
            valor_stock_final REAL DEFAULT 0
        );
        
        CREATE TABLE IF NOT EXISTS movimientos_ingreso (
            c1 INTEGER PRIMARY KEY,
            mes TEXT,
            fecha_orden TEXT,
            item_sku TEXT,
            cantidad INTEGER,
            descripcion_item TEXT,
            categoria_item TEXT,
            unidad_medida_item TEXT,
            precio_unitario REAL,
            descuento_monto REAL,
            descuento_porcentaje REAL,
            total_ingreso REAL,
            proveedor_nombre TEXT,
            numero_factura TEXT,
            numero_guia_despacho TEXT,
            numero_orden_compra TEXT,
            transportista_nombre TEXT,
            observaciones TEXT
        );
        
        CREATE TABLE IF NOT EXISTS movimientos_consumo (
            c1 INTEGER PRIMARY KEY,
            item_sku TEXT,
            descripcion_item TEXT,
            fecha_consumo TEXT,
            solicitante_nombre TEXT,
            cantidad_consumida INTEGER,
            precio_unitario REAL,
            total_consumo REAL,
            orden_trabajo_id INTEGER,
            stock_actual_en_consumo INTEGER,
            observaciones TEXT,
            categoria_item TEXT
        );
        
        CREATE TABLE IF NOT EXISTS ordenes_trabajo (
            id INTEGER PRIMARY KEY,
            estado_ingreso TEXT,
            registro_referencia TEXT,
            descripcion_componente TEXT,
            cliente_nombre TEXT,
            fecha_ot TEXT,
            codigo_referencia TEXT,
            listado_materiales TEXT
        );
    """
)
conn.commit()
infos = conn.execute("PRAGMA table_info(movimientos_consumo)").fetchall()
print('infos', infos)
conn.close()
os.close(fd)
