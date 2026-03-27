# North Chrome — Sistema de Gestión de Bodega

## Estructura de Archivos
```
north_chrome/
├── instalar.bat        ← Ejecutar UNA vez (instala dependencias)
├── iniciar.bat         ← Ejecutar cada vez que quieras usar el sistema
├── servidor.py         ← El servidor (no tocar)
├── index.html          ← La interfaz web (no tocar)
└── system/
    └── system.db       ← Tu base de datos (aquí se lee y escribe todo)
```

## Instalación Paso a Paso

### 1. Instalar Python (solo una vez)
- Ve a https://www.python.org/downloads/
- Descarga la versión más reciente
- **MUY IMPORTANTE**: Marca la casilla **"Add Python to PATH"** durante la instalación

### 2. Preparar la carpeta
- Copia toda la carpeta `north_chrome` a donde quieras (ej: `C:\NorthChrome\`)
- Verifica que tu archivo `system.db` esté dentro de `system/`

### 3. Instalar dependencias (solo una vez)
- Haz doble clic en `instalar.bat`
- Esto instalará Flask automáticamente

### 4. Usar el sistema (cada día)
- Haz doble clic en `iniciar.bat`
- Se abrirá automáticamente en tu navegador
- Dirección: http://localhost:5000

### 5. Para detener el sistema
- En la ventana negra (terminal), presiona `Ctrl + C`

## Funcionalidades
- **Dashboard**: Vista general con KPIs, top consumidos, stock crítico
- **Inventario**: 4675 productos con filtros, búsqueda y ordenamiento
- **Ingresos**: Registro de entradas con proveedor, factura, OC
- **Consumos**: Registro de salidas con solicitante y OT
- **Órdenes de Trabajo**: Gestión completa de OTs
- **Exportar CSV**: Descarga el inventario completo

## Respaldos
Tu base de datos está en `system/system.db`. Para respaldar:
- Copia el archivo `system.db` a otra ubicación periódicamente
- Puedes usar un pendrive o carpeta de respaldo
