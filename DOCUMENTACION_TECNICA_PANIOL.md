# Documentación Técnica - Sistema de Pañol

## Índice
1. [Arquitectura General](#arquitectura-general)
2. [Diagrama de Base de Datos](#diagrama-de-base-de-datos)
3. [API Endpoints](#api-endpoints)
4. [Estructura de Archivos](#estructura-de-archivos)
5. [Modelos de Datos](#modelos-de-datos)
6. [Lógica de Negocio](#lógica-de-negocio)
7. [Frontend](#frontend)
8. [Validaciones](#validaciones)
9. [Configuración y Deployment](#configuración-y-deployment)
10. [Testing](#testing)

---

## Arquitectura General

### Stack Tecnológico

**Backend:**
- Python 3.12
- Flask 2.3.2
- SQLite 3 (con extensiones de fechas)
- Blueprints para modularización

**Frontend:**
- HTML5 + CSS3 (Variables CSS, Grid, Flexbox)
- JavaScript ES6+ (Async/Await, Fetch API)
- Chart.js 4.x para gráficos
- Modal-based UI pattern

**Integración:**
- RESTful API (JSON)
- Arquitectura SPA (Single Page Application) con navegación por hash
- AJAX para todas las operaciones

### Patrón de Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                     CLIENTE (Navegador)                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   HTML/CSS   │  │  paniol.js   │  │  Chart.js    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────┬───────────────────────────────┘
                          │ HTTP REST API (JSON)
┌─────────────────────────┴───────────────────────────────┐
│                    SERVIDOR (Flask)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  empleados   │  │ herramientas │  │  validators  │  │
│  │  blueprint   │  │  blueprint   │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────┬───────────────────────────────┘
                          │ SQL Queries
┌─────────────────────────┴───────────────────────────────┐
│               BASE DE DATOS (SQLite)                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   empleados  │  │ herramientas │  │ movimientos  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│  ┌──────────────┐  ┌──────────────┐                    │
│  │ mantenimiento│  │    planes    │                    │
│  └──────────────┘  └──────────────┘                    │
└─────────────────────────────────────────────────────────┘
```

---

## Diagrama de Base de Datos

### Esquema Relacional

```sql
┌─────────────────────────────────┐
│          empleados              │
├─────────────────────────────────┤
│ PK  id                          │
│ UNQ numero_empleado             │
│     nombre                      │
│     rut                         │
│     cargo                       │
│     departamento                │
│     email                       │
│     telefono                    │
│     activo                      │
│     fecha_creacion              │
└─────────────────────────────────┘
            │
            │ (1:N)
            ▼
┌─────────────────────────────────┐
│   herramientas_movimientos      │
├─────────────────────────────────┤
│ PK  id                          │
│ FK  empleado_id                 │
│ FK  herramienta_id              │
│     tipo                        │◄──────┐
│     cantidad                    │       │
│     fecha_prestamo              │       │
│     fecha_devolucion            │       │
│     estado_devolucion           │       │
│     observaciones_prestamo      │       │
│     observaciones_devolucion    │       │
└─────────────────────────────────┘       │
                                           │
                                           │ (N:1)
┌─────────────────────────────────┐       │
│         herramientas            │───────┘
├─────────────────────────────────┤
│ PK  id                          │
│ UNQ sku                         │
│     nombre                      │
│     categoria                   │
│     marca                       │
│     modelo                      │
│     numero_serie                │
│     cantidad                    │
│     ubicacion                   │
│     estado                      │
│     valor_unitario              │
│     requiere_calibracion        │
│     frecuencia_calibracion      │
│     ultima_calibracion          │
│     descripcion                 │
│     fecha_creacion              │
└─────────────────────────────────┘
            │
            │ (1:N)
            ▼
┌─────────────────────────────────┐
│  herramientas_mantenimiento     │
├─────────────────────────────────┤
│ PK  id                          │
│ FK  herramienta_id              │
│     tipo                        │
│     fecha                       │
│     descripcion                 │
│     costo                       │
│     realizado_por               │
│     observaciones               │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ herramientas_planes_mant        │
├─────────────────────────────────┤
│ PK  id                          │
│ FK  herramienta_id              │
│     tipo                        │
│     frecuencia_dias             │
│     activo                      │
│     fecha_creacion              │
└─────────────────────────────────┘
```

### Índices Creados

```sql
-- Empleados
CREATE INDEX idx_empleados_numero ON empleados(numero_empleado)
CREATE INDEX idx_empleados_nombre ON empleados(nombre)
CREATE INDEX idx_empleados_activo ON empleados(activo)
CREATE INDEX idx_empleados_dept ON empleados(departamento)
CREATE INDEX idx_empleados_cargo ON empleados(cargo)

-- Herramientas
CREATE INDEX idx_herramientas_sku ON herramientas(sku)
CREATE INDEX idx_herramientas_nombre ON herramientas(nombre)
CREATE INDEX idx_herramientas_estado ON herramientas(estado)
CREATE INDEX idx_herramientas_categoria ON herramientas(categoria)
CREATE INDEX idx_herramientas_ubicacion ON herramientas(ubicacion)
CREATE INDEX idx_herramientas_calibracion ON herramientas(requiere_calibracion)

-- Movimientos
CREATE INDEX idx_movimientos_empleado ON herramientas_movimientos(empleado_id)
CREATE INDEX idx_movimientos_herramienta ON herramientas_movimientos(herramienta_id)
CREATE INDEX idx_movimientos_tipo ON herramientas_movimientos(tipo)
CREATE INDEX idx_movimientos_fecha_prest ON herramientas_movimientos(fecha_prestamo)
CREATE INDEX idx_movimientos_fecha_dev ON herramientas_movimientos(fecha_devolucion)
CREATE INDEX idx_movimientos_activos ON herramientas_movimientos(fecha_devolucion) 
    WHERE fecha_devolucion IS NULL

-- Mantenimiento
CREATE INDEX idx_mant_herramienta ON herramientas_mantenimiento(herramienta_id)
CREATE INDEX idx_mant_tipo ON herramientas_mantenimiento(tipo)
CREATE INDEX idx_mant_fecha ON herramientas_mantenimiento(fecha)

-- Planes
CREATE INDEX idx_planes_herramienta ON herramientas_planes_mantenimiento(herramienta_id)
CREATE INDEX idx_planes_activo ON herramientas_planes_mantenimiento(activo)
```

### Relaciones y Cardinalidad

- **empleados** 1:N **movimientos** (un empleado puede tener múltiples préstamos)
- **herramientas** 1:N **movimientos** (una herramienta puede prestarse múltiples veces)
- **herramientas** 1:N **mantenimiento** (historial completo de mantenciones)
- **herramientas** 1:N **planes_mantenimiento** (puede tener varios planes activos)

### Integridad Referencial

**CASCADE DELETE:**
- Al eliminar empleado → NO se permiten si tiene préstamos activos
- Al eliminar herramienta → CASCADE elimina movimientos, mantenimientos y planes
- Al eliminar plan → NO afecta a otros registros

**NULL Handling:**
- `fecha_devolucion IS NULL` = préstamo activo
- `fecha_devolucion NOT NULL` = préstamo cerrado

---

## API Endpoints

### Empleados

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/empleados` | Lista empleados con paginación, filtros y búsqueda |
| POST | `/api/empleados` | Crea nuevo empleado |
| GET | `/api/empleados/:id` | Obtiene empleado específico |
| PUT | `/api/empleados/:id` | Actualiza datos de empleado |
| DELETE | `/api/empleados/:id` | Elimina empleado (valida préstamos activos) |
| GET | `/api/empleados/suggest-numero` | Sugiere próximo número de empleado |
| GET | `/api/empleados/search` | Búsqueda rápida por texto |

**Parámetros de consulta GET /api/empleados:**
```
?page=1                    # Página actual
&per_page=50               # Items por página
&search=texto              # Búsqueda en nombre, número, cargo
&departamento=Mantención   # Filtro por departamento
&cargo=Técnico             # Filtro por cargo
&activo=1                  # Filtro por estado
```

**Respuesta ejemplo:**
```json
{
  "empleados": [...],
  "total": 20,
  "page": 1,
  "pages": 1,
  "departamentos": ["Mantención", "Producción"],
  "cargos": ["Técnico", "Operario", "Supervisor"]
}
```

### Herramientas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/herramientas` | Lista herramientas con filtros |
| POST | `/api/herramientas` | Crea nueva herramienta |
| GET | `/api/herramientas/:id` | Obtiene herramienta específica |
| PUT | `/api/herramientas/:id` | Actualiza herramienta |
| DELETE | `/api/herramientas/:id` | Elimina herramienta |
| GET | `/api/herramientas/suggest-sku` | Sugiere próximo SKU |
| GET | `/api/herramientas/search` | Búsqueda rápida |
| GET | `/api/herramientas/stats` | Estadísticas generales |
| GET | `/api/herramientas/:id/kardex` | Historial de movimientos |

**Parámetros GET /api/herramientas:**
```
?page=1
&per_page=50
&search=texto              # Búsqueda en SKU, nombre, categoría
&estado=operativa          # Filtro por estado
&categoria=Eléctricas      # Filtro por categoría
```

**Respuesta /api/herramientas/stats:**
```json
{
  "total_herramientas": 50,
  "operativas": 47,
  "en_mantenimiento": 1,
  "defectuosas": 2,
  "dadas_baja": 0,
  "prestamos_activos": 10,
  "calibraciones_vencidas": 4,
  "mantenimientos_vencidos": 0,
  "por_condicion": {
    "operativa": 47,
    "mantenimiento": 1,
    "defectuosa": 2
  }
}
```

### Préstamos (Checkout/Checkin)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/herramientas/checkout` | Préstamo batch de herramientas |
| POST | `/api/herramientas/checkin` | Devolución de herramienta |
| GET | `/api/herramientas/prestamos-activos` | Lista préstamos sin devolución |

**POST /api/herramientas/checkout:**
```json
{
  "fecha": "2026-03-09",
  "empleado": "EMP001",
  "observaciones": "Proyecto Línea 3",
  "herramientas": [
    {
      "herramienta_id": 15,
      "cantidad": 2
    },
    {
      "herramienta_id": 23,
      "cantidad": 1
    }
  ]
}
```

**POST /api/herramientas/checkin:**
```json
{
  "movimiento_id": 145,
  "fecha_devolucion": "2026-03-15",
  "estado_devolucion": "operativa",
  "observaciones_devolucion": "En perfectas condiciones"
}
```

**Estados válidos en checkin:**
- `operativa`: Sin problemas
- `mantenimiento`: Requiere revisión
- `defectuosa`: No funciona

### Mantenimiento

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/herramientas/mantenimiento` | Registra mantenimiento |
| GET | `/api/herramientas/mantenimientos-vencidos` | Lista mant. atrasados |
| GET | `/api/herramientas/calibraciones-vencidas` | Lista calib. expiradas |
| GET | `/api/herramientas/costos-mantenimiento` | Reporte de costos |

**POST /api/herramientas/mantenimiento:**
```json
{
  "herramienta_id": 23,
  "tipo": "preventivo",
  "fecha": "2026-03-09",
  "descripcion": "Cambio de filtro y lubricación",
  "costo": 15000,
  "realizado_por": "Juan Técnico",
  "observaciones": "Repuestos OEM"
}
```

**Tipos válidos:**
- `preventivo`
- `correctivo`
- `calibracion`

**GET /api/herramientas/costos-mantenimiento?meses=6:**
```json
{
  "costos": [
    {"mes": "2025-09", "total": 125000, "cantidad": 8},
    {"mes": "2025-10", "total": 89000, "cantidad": 5},
    ...
  ],
  "total_periodo": 654000
}
```

### Planes de Mantenimiento

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/herramientas/planes-mantenimiento` | Lista todos los planes |
| POST | `/api/herramientas/planes-mantenimiento` | Crea nuevo plan |
| DELETE | `/api/herramientas/planes-mantenimiento/:id` | Elimina plan |

**POST /api/herramientas/planes-mantenimiento:**
```json
{
  "herramienta_id": 45,
  "tipo": "preventivo",
  "frecuencia_dias": 90
}
```

---

## Estructura de Archivos

```
north_chrome/
├── app/
│   ├── __init__.py                    # Registro de blueprints
│   ├── db.py                          # Conexión DB
│   └── routes/
│       ├── empleados.py               # API empleados (423 líneas)
│       └── herramientas.py            # API herramientas (1387 líneas)
│
├── js/
│   ├── core.js                        # Funciones base (go, api, toast)
│   ├── paniol.js                      # Frontend pañol (700+ líneas)
│   ├── pagination.js                  # Sistema de paginación
│   └── ...
│
├── css/
│   ├── modules.css                    # Estilos pañol (~450 líneas)
│   ├── theme.css                      # Variables CSS
│   └── ...
│
├── tests/
│   ├── conftest.py                    # Fixtures pytest
│   ├── test_paniol.py                 # Tests del pañol (30+ tests)
│   └── ...
│
├── crear_tablas_paniol.py             # Migración + datos demo
├── validators.py                      # Validaciones centralizadas
├── index.html                         # SPA principal
├── servidor.py                        # Entry point Flask
├── run.py                             # Script de inicio
└── app.db                             # Base de datos SQLite
```

---

## Modelos de Datos

### Empleado

```python
{
    "id": 1,
    "numero_empleado": "EMP001",        # Único, requerido
    "nombre": "Juan Pérez",             # Requerido
    "rut": "12345678-9",                # Opcional
    "cargo": "Técnico",                 # Opcional
    "departamento": "Mantención",       # Opcional
    "email": "juan@empresa.cl",         # Opcional
    "telefono": "+56912345678",         # Opcional
    "activo": 1,                        # 1=Activo, 0=Inactivo
    "fecha_creacion": "2026-01-15"
}
```

### Herramienta

```python
{
    "id": 1,
    "sku": "HERR001",                   # Único, requerido
    "nombre": "Taladro Bosch",          # Requerido
    "categoria": "Herramientas Eléctricas",
    "marca": "Bosch",
    "modelo": "GSB 13 RE",
    "numero_serie": "ABC123XYZ",
    "cantidad": 10,                     # Total en inventario
    "cantidad_prestada": 3,             # Calculado en consultas
    "ubicacion": "Pañol A-12",
    "estado": "operativa",              # operativa|mantenimiento|defectuosa|baja
    "valor_unitario": 85000,
    "requiere_calibracion": 1,          # 1=Sí, 0=No
    "frecuencia_calibracion": 365,      # Días entre calibraciones
    "ultima_calibracion": "2025-03-09",
    "proxima_calibracion": "2026-03-09", # Calculado
    "descripcion": "Taladro percutor...",
    "fecha_creacion": "2025-01-10"
}
```

### Movimiento

```python
{
    "id": 145,
    "empleado_id": 5,
    "empleado_nombre": "Juan Pérez",     # JOIN
    "herramienta_id": 15,
    "herramienta_nombre": "Taladro",     # JOIN
    "herramienta_sku": "HERR015",        # JOIN
    "tipo": "prestamo",                  # prestamo|devolucion
    "cantidad": 2,
    "fecha_prestamo": "2026-03-01",
    "fecha_devolucion": null,            # NULL = activo
    "estado_devolucion": null,           # operativa|mantenimiento|defectuosa
    "observaciones_prestamo": "Proyecto X",
    "observaciones_devolucion": null
}
```

### Mantenimiento

```python
{
    "id": 78,
    "herramienta_id": 23,
    "tipo": "preventivo",                # preventivo|correctivo|calibracion
    "fecha": "2026-03-09",
    "descripcion": "Cambio de filtro...",
    "costo": 15000,
    "realizado_por": "Juan Técnico",
    "observaciones": "Repuestos OEM"
}
```

### Plan de Mantenimiento

```python
{
    "id": 12,
    "herramienta_id": 45,
    "herramienta_nombre": "Torquímetro", # JOIN
    "tipo": "calibracion",
    "frecuencia_dias": 365,
    "ultimo_mantenimiento": "2025-03-09", # Calculado
    "proximo_mantenimiento": "2026-03-09",# Calculado
    "dias_hasta_proximo": 0,             # Calculado
    "estado": "vencido",                 # al_dia|vencido
    "activo": 1,
    "fecha_creacion": "2025-01-15"
}
```

---

## Lógica de Negocio

### Cálculo de Disponibilidad

```python
disponible = cantidad_total - SUM(cantidad_prestada WHERE fecha_devolucion IS NULL)
```

**Implementación SQL:**
```sql
SELECT 
    h.*,
    COALESCE(SUM(CASE WHEN hm.fecha_devolucion IS NULL 
                 THEN hm.cantidad ELSE 0 END), 0) as cantidad_prestada
FROM herramientas h
LEFT JOIN herramientas_movimientos hm ON h.id = hm.herramienta_id
GROUP BY h.id
```

### Validación de Checkout

**Reglas:**
1. ✅ Empleado debe existir y estar activo
2. ✅ Herramienta debe existir
3. ✅ Estado de herramienta debe ser "operativa"
4. ✅ Cantidad solicitada ≤ Cantidad disponible
5. ✅ Fecha no puede ser futura
6. ✅ Al menos una herramienta en el array

**Código en `herramientas.py`:**
```python
# Validar disponibilidad
disponible = herramienta['cantidad'] - cantidad_prestada
if item['cantidad'] > disponible:
    return jsonify({
        'ok': False,
        'msg': f'Solo hay {disponible} unidades disponibles'
    }), 400
```

### Validación de Checkin

**Reglas:**
1. ✅ Movimiento debe existir y estar activo (fecha_devolucion IS NULL)
2. ✅ Fecha devolución ≥ Fecha préstamo
3. ✅ Estado devolucion debe ser válido (operativa|mantenimiento|defectuosa)
4. ✅ Si estado ≠ operativa → observaciones obligatorias

**Código:**
```python
# Validar observaciones según estado
if estado_devolucion != 'operativa' and not observaciones_devolucion:
    return jsonify({
        'ok': False,
        'msg': 'Las observaciones son obligatorias si el estado no es operativa'
    }), 400
```

### Cálculo de Próxima Calibración

**Fórmula:**
```python
proxima_calibracion = ultima_calibracion + frecuencia_calibracion (días)
```

**Implementación SQL:**
```sql
SELECT 
    h.*,
    date(h.ultima_calibracion, '+' || h.frecuencia_calibracion || ' days') 
        as proxima_calibracion
FROM herramientas h
WHERE h.requiere_calibracion = 1
```

### Detección de Calibraciones Vencidas

**Query:**
```sql
SELECT h.*, 
       julianday('now') - julianday(date(h.ultima_calibracion, 
           '+' || h.frecuencia_calibracion || ' days'))
       as dias_vencido
FROM herramientas h
WHERE h.requiere_calibracion = 1
  AND h.ultima_calibracion IS NOT NULL
  AND date(h.ultima_calibracion, 
           '+' || h.frecuencia_calibracion || ' days') < date('now')
ORDER BY dias_vencido DESC
```

### Cálculo de Planes Vencidos

**Lógica:**
1. Buscar último mantenimiento del tipo especificado
2. Sumar frecuencia_dias a esa fecha
3. Comparar con fecha actual
4. Si `proximo_mant < hoy` → VENCIDO

**Query:**
```sql
WITH ultimo_mant AS (
    SELECT 
        hm.herramienta_id,
        MAX(hm.fecha) as ultima_fecha
    FROM herramientas_mantenimiento hm
    WHERE hm.tipo = p.tipo
    GROUP BY hm.herramienta_id
)
SELECT 
    p.*,
    date(um.ultima_fecha, '+' || p.frecuencia_dias || ' days') as proximo,
    julianday('now') - julianday(...) as dias_vencido
FROM herramientas_planes_mantenimiento p
LEFT JOIN ultimo_mant um ON p.herramienta_id = um.herramienta_id
WHERE proximo < date('now')
```

### Actualización Automática de Estado

**Al registrar mantenimiento correctivo/calibración:**
```python
# Si es calibración, actualizar última_calibracion
if tipo == 'calibracion':
    cur.execute("""
        UPDATE herramientas 
        SET ultima_calibracion = ?
        WHERE id = ?
    """, (fecha, herramienta_id))
```

**Al hacer checkin con estado diferente:**
```python
# Actualizar estado de herramienta según devolución
cur.execute("""
    UPDATE herramientas 
    SET estado = ?
    WHERE id = (
        SELECT herramienta_id 
        FROM herramientas_movimientos 
        WHERE id = ?
    )
""", (estado_devolucion, movimiento_id))
```

---

## Frontend

### Arquitectura JavaScript

**Patrón:** Module Pattern + Estado Global

```javascript
// Estados globales por módulo
let empS = { p: 1 };              // Estado paginación empleados
let herrS = { p: 1 };             // Estado paginación herramientas
let checkoutItems = [];            // Carrito temporal de checkout

// Funciones principales por recurso
async function lEmpleados() { }   // Lista empleados
async function lHerramientas() { }// Lista herramientas
async function loadPaniolDashboard() { } // Dashboard completo
```

### Flujo de Navegación

```javascript
// core.js - función go()
function go(page) {
    // 1. Ocultar todas las páginas
    document.querySelectorAll('.pg').forEach(s => s.classList.remove('on'));
    
    // 2. Mostrar página seleccionada
    document.getElementById('p-' + page).classList.add('on');
    
    // 3. Cargar datos según página
    if (page === 'paniol') loadPaniolDashboard();
    if (page === 'empleados') lEmpleados();
    if (page === 'herramientas') lHerramientas();
}
```

### Sistema de Modales

**Apertura:**
```javascript
function oM(id) { 
    document.getElementById(id).classList.add('on'); 
}
```

**Cierre:**
```javascript
function cM(id) { 
    document.getElementById(id).classList.remove('on'); 
}
```

**CSS:**
```css
.mb { 
    display: none; /* Por defecto oculto */
}
.mb.on { 
    display: flex; /* Visible cuando tiene clase 'on' */
}
```

### Sistema de Toasts

```javascript
function toast(mensaje, tipo = 'ok') {
    const elemento = document.createElement('div');
    elemento.className = 'toast t-' + tipo;
    elemento.textContent = mensaje;
    document.getElementById('tc').appendChild(elemento);
    
    setTimeout(() => {
        elemento.style.opacity = '0';
        setTimeout(() => elemento.remove(), 300);
    }, 3500);
}
```

**Tipos:**
- `ok`: Verde, éxito
- `err`: Rojo, error
- `warn`: Naranja, advertencia

### AJAX con Fetch API

```javascript
async function api(url, options) {
    try {
        const response = await fetch(url, options);
        return await response.json();
    } catch (error) {
        toast('Error de conexión', 'err');
        return null;
    }
}
```

**Uso:**
```javascript
// GET
const data = await api('/api/herramientas');

// POST
const result = await api('/api/empleados', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(datos)
});
```

### Paginación

**Estado:**
```javascript
let empS = { p: 1 };  // Página actual
```

**Render:**
```javascript
function rP(containerId, data, state, loadFunction) {
    const container = document.getElementById(containerId);
    container.innerHTML = `
        <button onclick="${loadFunction}(); ${state}.p--">Anterior</button>
        <span>Página ${data.page} de ${data.pages}</span>
        <button onclick="${loadFunction}(); ${state}.p++">Siguiente</button>
    `;
}
```

### Chart.js Integration

```javascript
// Destruir chart anterior si existe
if (chartTopEmpleados) chartTopEmpleados.destroy();

// Crear nuevo chart
chartTopEmpleados = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [...],
        datasets: [{
            label: 'Préstamos Activos',
            data: [...],
            backgroundColor: 'rgba(40, 167, 69, 0.6)'
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});
```

---

## Validaciones

### Backend (validators.py)

**validate_empleado_data(data):**
```python
errors = []

# Nombre mínimo 3 caracteres
if len(nombre) < 3:
    errors.append('Nombre debe tener al menos 3 caracteres')

# Número de empleado único
if db_has_empleado(numero_empleado):
    errors.append('Número de empleado ya existe')

return errors if errors else None
```

**validate_herramienta_data(data):**
```python
# Si requiere calibración → frecuencia obligatoria
if requiere_calibracion and not frecuencia_calibracion:
    errors.append('Frecuencia de calibración es obligatoria')

# Cantidad mayor a 0
if cantidad <= 0:
    errors.append('Cantidad debe ser mayor a cero')
```

**validate_checkout_data(data):**
```python
# Empleado requerido (ID o nombre)
if not empleado_id and not empleado_numero:
    errors.append('Empleado es obligatorio')

# Array de herramientas no vacío
if not herramientas or len(herramientas) == 0:
    errors.append('Debe incluir al menos una herramienta')

# Cada herramienta con cantidad > 0
for item in herramientas:
    if item['cantidad'] <= 0:
        errors.append('Cantidad debe ser mayor a cero')
```

**validate_checkin_data(data):**
```python
# Estado devolucion obligatorio
if not estado_devolucion:
    errors.append('Estado de devolución es obligatorio')

# Si estado != operativa → observaciones obligatorias
if estado_devolucion != 'operativa' and not observaciones:
    errors.append('Observaciones obligatorias si estado no es operativo')
```

### Frontend (paniol.js)

**Validaciones previas a API call:**
```javascript
async function saveEmpleado() {
    const nombre = $('memp-nom').value.trim();
    const numero = $('memp-num').value.trim();
    
    // Validación local
    if (!nombre || !numero) {
        return toast('Nombre y número obligatorios', 'err');
    }
    
    // Continuar con API...
}
```

**Validación de disponibilidad en checkout:**
```javascript
function addCheckoutItem() {
    const disponible = herramienta.cantidad - herramienta.cantidad_prestada;
    
    if (disponible < cantidadSolicitada) {
        $('mco-info').textContent = `Solo hay ${disponible} disponibles`;
        return;
    }
    
    // Agregar al carrito...
}
```

---

## Configuración y Deployment

### Requisitos

```
Python >= 3.12
Flask >= 2.3.2
```

### Instalación

```bash
# Clonar repositorio
git clone <repo>
cd north_chrome

# Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Crear base de datos (si no existe)
python crear_tablas_paniol.py

# Iniciar servidor
python run.py
```

### Variables de Entorno

No requiere configuración especial. El sistema usa:
- Base de datos: `app.db` (SQLite local)
- Puerto: 5000 (Flask default)
- Debug: Activado en desarrollo

### Estructura de Deployment

**Desarrollo:**
```
python run.py
# http://localhost:5000
```

**Producción (con Gunicorn):**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 servidor:app
```

**Producción (con Nginx reverse proxy):**
```nginx
server {
    listen 80;
    server_name paniol.empresa.cl;
    
    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Backup de Base de Datos

```bash
# Backup manual
cp app.db backups/app_$(date +%Y%m%d_%H%M%S).db

# Backup automático (cron)
0 2 * * * cd /ruta/north_chrome && cp app.db backups/app_$(date +\%Y\%m\%d).db
```

---

## Testing

### Ejecutar Tests

```bash
# Todos los tests
pytest

# Solo tests del pañol
pytest tests/test_paniol.py

# Con coverage
pytest --cov=app/routes --cov-report=html

# Test específico
pytest tests/test_paniol.py::test_empleados_create -v
```

### Cobertura de Tests

**test_paniol.py incluye:**
- ✅ CRUD completo de empleados (create, read, update, delete)
- ✅ CRUD completo de herramientas
- ✅ Sugerencias automáticas (numero_empleado, SKU)
- ✅ Estadísticas y reportes
- ✅ Checkout con validación de disponibilidad
- ✅ Checkin con validación de estado
- ✅ Registro de mantenimiento
- ✅ Planes de mantenimiento
- ✅ Calibraciones y mantenimientos vencidos
- ✅ Costos de mantenimiento
- ✅ Kardex de herramienta
- ✅ Validaciones de campos obligatorios

**Total:** 30+ casos de prueba

### Fixtures (conftest.py)

```python
@pytest.fixture
def client():
    """Cliente de prueba con DB temporal"""
    db_fd, db_path = tempfile.mkstemp()
    app.config['DATABASE'] = db_path
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        with app.app_context():
            init_test_db(db_path)
        yield client
    
    os.unlink(db_path)
```

### Datos de Prueba

El script `crear_tablas_paniol.py` incluye:
- 20 empleados de diferentes departamentos
- 50 herramientas en diversas categorías
- 30 movimientos (10 préstamos activos)
- 40 registros de mantenimiento
- 15 planes de mantenimiento

---

## Troubleshooting

### Error: "No module named 'app'"

**Solución:**
```bash
# Asegurarse de estar en el directorio correcto
cd north_chrome
python run.py
```

### Error: "Database is locked"

**Causa:** SQLite no permite múltiples escrituras concurrentes

**Solución:**
```python
# Usar timeout largo
conn = sqlite3.connect('app.db', timeout=30.0)
```

### Error: "Herramientas no disponibles después de checkin"

**Causa:** Estado de herramienta quedó en "mantenimiento" o "defectuosa"

**Solución:**
```sql
-- Verificar estado
SELECT id, sku, nombre, estado FROM herramientas WHERE id = ?;

-- Cambiar a operativa si corresponde
UPDATE herramientas SET estado = 'operativa' WHERE id = ?;
```

### Performance lento con muchos registros

**Solución:**
```sql
-- Verificar que existan los índices
.indices herramientas
.indices herramientas_movimientos

-- Recrear índices si faltan
python crear_tablas_paniol.py
```

---

## Extensiones Futuras

**Funcionalidades potenciales:**
1. **QR Codes**: Generar códigos QR para herramientas
2. **Fotos**: Subir imágenes de herramientas
3. **Notificaciones**: Email cuando vence calibración
4. **Reportes PDF**: Generar informes de préstamos
5. **Dashboard móvil**: App nativa o PWA
6. **Firma digital**: Empleado firma al retirar
7. **Integración con ERP**: Sincronizar con sistema central
8. **Geolocalización**: Trackear ubicación de herramientas prestadas
9. **Historial de reparaciones**: Costo acumulado por herramienta
10. **Reservas**: Empleados pueden reservar herramientas

---

## Referencias

**Documentos relacionados:**
- `MANUAL_USUARIO_PANIOL.md`: Manual de usuario final
- `LEEME.md`: Guía general del sistema
- `CHANGELOG.md`: Historial de cambios

**APIs externas:**
- Chart.js: https://www.chartjs.org/docs/latest/
- Flask: https://flask.palletsprojects.com/
- SQLite: https://www.sqlite.org/docs.html

---

**Versión**: 1.0  
**Autor**: Sistema North Chrome  
**Última actualización**: Marzo 2026
