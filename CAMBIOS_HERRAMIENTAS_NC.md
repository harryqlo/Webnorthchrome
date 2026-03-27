# 🔧 Cambios en Sistema de Herramientas - Prefijo NC y Acciones Profesionales

**Fecha:** March 10, 2026  
**Versión:** v2.1.0  
**Estado:** ✅ Implementado

---

## 📋 Resumen Ejecutivo

Se han realizado mejoras significativas al sistema de gestión de herramientas del pañol:

1. **✅ Prefijo NC Estandarizado** - Todas las herramientas usan prefijo `NC` (North Chrome)
2. **✅ Acciones Avanzadas de Préstamos** - 6 nuevas operaciones profesionales
3. **✅ Historial de Préstamos Profesional** - Sistema robusto de auditoría y trazabilidad
4. **✅ Endpoints API Completos** - Integración total con interfaz frontend

---

## 🎯 1. PREFIJO NC PARA HERRAMIENTAS

### Configuración Central
**Archivo:** `config.py` (lineas 59-60)

```python
HERRAMIENTAS_PREFIX_DEFAULT = 'NC'  # North Chrome - prefijo automático
HERRAMIENTAS_SKU_SEPARATOR = '-'    # Separador para SKU (NC-001, NC-002, etc)
```

### Formato de SKU
- **Ejemplo:** `NC-001`, `NC-002`, `NC-150`, etc.
- **Generación Automática:** Al crear herramienta sin SKU, se asigna el siguiente número disponible
- **Validación Única:** Previene duplicados en la base de datos

### Endpoints para SKU
```
GET /api/herramientas/suggest-sku?prefix=NC
→ Sugiere próximo SKU disponible: "NC-051"

POST /api/herramientas
{
  "nombre": "Taladro Bosch 850W",
  "categoria": "Herramientas Eléctricas"
  // SKU se genera automáticamente: NC-051
}
```

---

## 🚀 2. ACCIONES AVANZADAS DE PRÉSTAMOS (NUEVAS)

### 2.1 Renovar Préstamo
**Función:** Extiende el plazo de un préstamo activo sin devolución física

**Endpoint:**
```
POST /api/herramientas/prestamo/{movimiento_id}/renovar
Content-Type: application/json

{
  "dias_extension": 14,
  "observaciones": "Trabajo prolongado en reparación"
}

Response:
{
  "ok": true,
  "msg": "Préstamo renovado por 14 días",
  "movimiento_id": 123,
  "empleado": "Juan Pérez",
  "dias_extension": 14
}
```

**Casos de Uso:**
- Trabajo que se extiende más tiempo del previsto
- Retención temporal justificada de herramientas
- Mantenimiento continuado de activos

---

### 2.2 Cambiar Responsable de Préstamo
**Función:** Transfiere la responsabilidad del préstamo a otro empleado

**Endpoint:**
```
POST /api/herramientas/prestamo/{movimiento_id}/cambiar-responsable
Content-Type: application/json

{
  "nuevo_empleado_id": 5,
  "nuevo_empleado_nombre": "María González",
  "motivo": "Cambio de turno"
}

Response:
{
  "ok": true,
  "msg": "Responsable cambiado a María González",
  "movimiento_id": 123,
  "responsable_anterior": "Juan Pérez",
  "responsable_nuevo": "María González"
}
```

**Auditoría:**
```
[CAMBIO RESPONSABLE 2026-03-10 14:30:00] 
De: Juan Pérez. A: María González. Motivo: Cambio de turno
```

**Casos de Uso:**
- Cambios de turno
- Transferencia de proyectos
- Cambios de departamento

---

### 2.3 Devoluciones (total y parcial) unificadas
**Función:** Las devoluciones se centralizan en un único endpoint. Ya no
existen tipos distintos de retorno; el sistema calcula internamente si se
trata de un cierre total o una devolución parcial y segmenta los movimientos
cuando corresponde.

**Endpoint recomendado:**
```
POST /api/herramientas/checkin
Content-Type: application/json

{
  "devoluciones": [
    {
      "movimiento_id": 123,
      "cantidad_devuelta": 2,           # opcional, 1 por defecto
      "estado_retorno": "operativa",
      "observaciones_retorno": "Herramientas usadas correctamente",
      "fecha_devolucion": "2026-03-10"  # opcional
    }
  ]
}

Response:
{
  "ok": true,
  "msg": "Devolución parcial: 2 unidades. Pendiente: 3"
}
```

- Si `cantidad_devuelta` equivale al total prestado, el movimiento se cierra.
- Si es menor se crea automáticamente un nuevo movimiento con la cantidad
  restante.
- Los inventarios y condiciones se actualizan en una sola transacción.

> **Nota:** el antiguo endpoint `/api/herramientas/prestamo/{id}/devolucion-parcial`
> se mantiene sólo para compatibilidad y redirige internamente a la misma
> lógica de `checkin`.

**Casos de Uso:**
- Devoluciones progresivas de sets de herramientas
- Retorno completo directo
- Operaciones masivas de múltiples movimientos
- Registra el historial completo

**Casos de Uso:**
- Devoluciones progresivas de sets de herramientas
- Ajustes de cantidades en préstamos múltiples
- Control de herramientas críticas

---

### 2.4 Obtener Préstamos Vencidos
**Función:** Identifica préstamos que exceden el tiempo límite permitido

**Endpoint:**
```
GET /api/herramientas/prestamos-vencidos?dias_limite=30

Response:
{
  "ok": true,
  "prestamos_vencidos": [
    {
      "movimiento_id": 12,
      "herramienta_sku": "NC-045",
      "herramienta_nombre": "Amoladora Angular 7\"",
      "empleado_nombre": "Carlos Rodríguez",
      "fecha_salida": "2026-01-20",
      "dias_vencidos": 50,
      "nivel_alerta": "critico"  // 'critico' | 'alto' | 'medio'
    }
  ],
  "total": 5,
  "dias_limite": 30
}
```

**Niveles de Alerta:**
- **Crítico:** Más del doble del límite (> 60 días)
- **Alto:** Entre límite y doble (30-60 días)
- **Medio:** Dentro del límite

**Caso de Uso:**
- Dashboard de alertas
- Reporte ejecutivo de activos retenidos
- Auditoría y cumplimiento

---

### 2.5 Registrar Observación en Préstamo
**Función:** Agregar notas/seguimiento a un préstamo activo con timestamp y tipo

**Endpoint:**
```
POST /api/herramientas/prestamo/{movimiento_id}/observacion
Content-Type: application/json

{
  "observacion": "Herramienta necesita calibración antes de devolución",
  "tipo": "requerimiento"  // 'general' | 'requerimiento' | 'incidencia' | 'visita'
}

Response:
{
  "ok": true,
  "msg": "Observación registrada correctamente",
  "movimiento_id": 123,
  "tipo": "requerimiento"
}
```

**Registro en BD:**
```
[2026-03-10 14:45:22] [REQUERIMIENTO] 
Herramienta necesita calibración antes de devolución
```

**Tipos de Observaciones:**
- `general` - Notas generales
- `requerimiento` - Acciones requeridas
- `incidencia` - Problemas reportados
- `visita` - Registros de supervisión/inspección

**Casos de Uso:**
- Seguimiento de condiciones
- Registro de incidencias
- Documentación de visitas de supervisión
- Requisitos de mantenimiento

---

### 2.6 Historial Completo de Préstamo
**Función:** Obtiene información detallada y completa de un préstamo (movimiento)

**Endpoint:**
```
GET /api/herramientas/prestamo/{movimiento_id}/historial-completo

Response:
{
  "ok": true,
  "movimiento": {
    "id": 123,
    "herramienta_id": 45,
    "empleado_id": 8,
    "empleado_nombre": "Juan Pérez Contreras",
    "fecha_salida": "2026-02-15",
    "fecha_retorno": null,
    "cantidad": 5,
    "estado_salida": "operativa",
    "estado_retorno": null,
    "observaciones_salida": "Trabajo en taller principal...",
    "observaciones_retorno": null,
    "orden_trabajo_id": 1542,
    "usuario_registro": "admin@system",
    "fecha_registro": "2026-02-15 09:30:00"
  },
  "herramienta": {
    "sku": "NC-045",
    "nombre": "Amoladora Angular 7\"",
    "modelo": "GWS2000",
    "condicion": "operativa"
  },
  "empleado": {
    "nombre": "Juan Pérez Contreras",
    "numero_identificacion": "E001",
    "departamento": "Mantención",
    "puesto": "Mecánico Senior"
  },
  "duracion": {
    "dias_prestamo": 24,
    "dias_pendiente": 24,
    "estado": "activo"
  }
}
```

**Información Incluida:**
- Detalles completos del movimiento
- Información de la herramienta
- Datos del empleado/responsable
- Cálculo de duración
- Todo el historial de observaciones

**Casos de Uso:**
- Auditoría completa de préstamo
- Investigación de discrepancias
- Reportes detallados
- Cumplimiento regulatorio

---

## 📊 3. ESTRUCTURA DE BD - TABLA HERRAMIENTAS_MOVIMIENTOS

### Campos Mejorados para Historial Profesional

```sql
CREATE TABLE herramientas_movimientos (
  id INTEGER PRIMARY KEY,
  
  -- Referencias
  herramienta_id INTEGER,           -- Qué se prestó
  empleado_id INTEGER,              -- A quién
  empleado_nombre TEXT,             -- Nombre del responsable
  
  -- Fechas
  fecha_salida TEXT,                -- Cuándo se prestó
  fecha_retorno TEXT,               -- Cuándo se devolvió (NULL = activo)
  
  -- Cantidad
  cantidad INTEGER DEFAULT 1,       -- Cuántas unidades
  
  -- Estados
  estado_salida TEXT,               -- Estado al salir ('operativa', etc)
  estado_retorno TEXT,              -- Estado al retornar
  
  -- Observaciones (Auditoría)
  observaciones_salida TEXT,        -- Notas iniciales + renovaciones + cambios
  observaciones_retorno TEXT,       -- Notas de devolución
  
  -- Trazabilidad
  orden_trabajo_id INTEGER,         -- Proyecto/Orden asociada
  usuario_registro TEXT,            -- Quién registró
  fecha_registro TEXT,              -- Cuándo se registró
  
  FOREIGN KEY (herramienta_id) REFERENCES herramientas(id),
  FOREIGN KEY (empleado_id) REFERENCES empleados(id),
  FOREIGN KEY (orden_trabajo_id) REFERENCES ordenes_trabajo(id)
);
```

### Campo de Observaciones - Historial Acumulativo

El campo `observaciones_salida` acumula todo el historial con timestamps:

```
[2026-02-15 09:30:00] Trabajo en taller principal
[2026-02-20 14:15:00] [RENOVACIÓN] +7 días. Se extiende trabajo
[2026-02-22 10:45:00] [CAMBIO RESPONSABLE] De: Juan Pérez. A: María González. Motivo: Cambio de turno
[2026-02-25 16:20:00] [REQUERIMIENTO] Herramienta necesita calibración antes de devolución
[2026-02-27 11:00:00] [INCIDENCIA] Pequeño daño cosmético en mango
```

---

## 🔐 4. AUDITORÍA Y VALIDACIONES

### Validaciones Implementadas

1. **Sobre Préstamos Activos:**
   - ✅ SKU único en sistema
   - ✅ Empleado debe estar activo
   - ✅ Herramienta debe estar operativa para checkout
   - ✅ Cantidad disponible debe ser suficiente
   - ✅ No se puede renovar préstamo ya devuelto

2. **Sobre Responsables:**
   - ✅ Validación de existencia de empleado
   - ✅ Validación de estado activo
   - ✅ Registro de quién hizo el cambio

3. **Sobre Devoluciones:**
   - ✅ Cantidad <= cantidad prestada
   - ✅ Validación de estado de retorno
   - ✅ Observaciones requeridas si no es operativa

### Auditoría Automática

Todos los cambios se registran con:
- **Timestamp:** Fecha y hora exacta
- **Usuario:** Quién hizo la acción
- **Tipo:** Categoría de la acción (RENOVACIÓN, CAMBIO, INCIDENCIA, etc.)
- **Contexto:** Detalles de qué cambió

**Registro en BD:**
```sql
-- Cada operación deja huella en observaciones_salida
-- Nunca se elimina historial, solo se acumula
-- Permite reconstruir la línea de tiempo completa
```

---

## 🌐 5. ENDPOINTS API COMPLETOS

### Resumen de Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/herramientas` | Listar herramientas con filtros |
| `POST` | `/api/herramientas` | Crear herramienta (SKU NC autogenerado) |
| `GET` | `/api/herramientas/suggest-sku` | Sugerir próximo SKU |
| `POST` | `/api/herramientas/checkout` | Préstamo batch |
| `POST` | `/api/herramientas/checkin` | Devolución |
| `GET` | `/api/herramientas/prestamos-activos` | Listado de préstamos |
| `GET` | `/api/herramientas/prestamos-vencidos` | Alertas de vencimiento |
| `POST` | `/api/herramientas/prestamo/{id}/renovar` | **NEW** Renovar préstamo |
| `POST` | `/api/herramientas/prestamo/{id}/cambiar-responsable` | **NEW** Cambiar responsable |
| `POST` | `/api/herramientas/prestamo/{id}/devolucion-parcial` | **NEW** Devolución parcial |
| `POST` | `/api/herramientas/prestamo/{id}/observacion` | **NEW** Agregar observación |
| `GET` | `/api/herramientas/prestamo/{id}/historial-completo` | **NEW** Historial detallado |

---

## 📝 6. EJEMPLOS DE USO PROFESIONAL

### Caso 1: Trabajo Prolongado con Renovación

```json
// 1. Préstamo inicial
POST /api/herramientas/checkout
{
  "empleado_id": 8,
  "herramientas": [
    {"herramienta_id": 45, "cantidad": 2, "observaciones": "Trabajo de soldadura"}
  ]
}
// Response: movimiento_id = 123

// 2. Se requiere más tiempo
POST /api/herramientas/prestamo/123/renovar
{
  "dias_extension": 14,
  "observaciones": "Soldadura más compleja de lo esperado"
}

// 3. Devolución parcial - se devuelven 1, se queda con 1
POST /api/herramientas/prestamo/123/devolucion-parcial
{
  "cantidad_devuelta": 1,
  "estado_devolucion": "operativa"
}

// 4. Cambio de responsable por cambio de turno
POST /api/herramientas/prestamo/123/cambiar-responsable
{
  "nuevo_empleado_id": 10,
  "nuevo_empleado_nombre": "Carlos Rodríguez",
  "motivo": "Cambio de turno nocturno"
}

// 5. Historial completo para auditoría
GET /api/herramientas/prestamo/123/historial-completo
```

### Caso 2: Gestión de Incidencias

```json
// Registrar problema durante préstamo
POST /api/herramientas/prestamo/456/observacion
{
  "observacion": "Herramienta con desgaste. Requiere calibración antes de devolución",
  "tipo": "incidencia"
}

// Registrar requerimiento
POST /api/herramientas/prestamo/456/observacion
{
  "observacion": "Requiere revisión de técnico de mantenimiento",
  "tipo": "requerimiento"
}

// Verificar préstamos con problemas
GET /api/herramientas/prestamo/456/historial-completo
→ Historial muestra:
  [2026-03-10 14:20:00] [INCIDENCIA] Herramienta con desgarre...
  [2026-03-10 14:25:00] [REQUERIMIENTO] Requiere revisión...
```

### Caso 3: Auditoría y Conformidad

```json
// Obtener todos los préstamos vencidos para reporte
GET /api/herramientas/prestamos-vencidos?dias_limite=30

// Para cada uno vencido, obtener historial completo
GET /api/herramientas/prestamo/123/historial-completo
GET /api/herramientas/prestamo/124/historial-completo

→ Genera reporte de:
  - Quién tiene qué
  - Desde cuándo
  - Qué cambios/renovaciones se hicieron
  - Si hay problemas registrados
```

---

## 🔄 7. MIGRACIÓN Y COMPATIBILIDAD

### Datos Existentes
- ✅ Todos los SKU existentes son **compatibles** (sin cambios)
- ✅ Las nuevas herramientas se crean con **prefijo NC**
- ✅ Historial de préstamos anterior se **mantiene intacto**

### Transición Recomendada

```python
# 1. Las herramientas antiguas mantienen sus SKU
SELECT sku FROM herramientas WHERE sku NOT LIKE 'NC-%'
→ Siguen siendo válidas

# 2. Nuevas herramientas usan NC
POST /api/herramientas
{ "nombre": "Nueva Herramienta" }
→ Asignado: "NC-051"

# 3. Las nuevas acciones funcionan con cualquier SKU
POST /api/herramientas/prestamo/123/renovar
→ Funciona con herramientas NC y no-NC
```

---

## 📈 8. BENEFICIOS POR FUNCIONALIDAD

### Beneficios de Usar Prefijo NC

| Beneficio | Descripción |
|-----------|------------|
| **Estandarización** | Identificación clara de herramientas North Chrome |
| **Escalabilidad** | Soporta hasta 999+ herramientas (NC-001 a NC-9999) |
| **Trazabilidad** | Fácil filtrado y reporte de activos NC |
| **Automatización** | SKU se genera sin intervención manual |
| **Cumplimiento** | Cumple estándares de gestión de activos |

### Beneficios de Acciones Avanzadas

| Acción | Beneficio |
|--------|----------|
| **Renovar** | Evita devoluciones/préstamos innecesarios |
| **Cambiar Responsable** | Flexibilidad operativa, cambios de turno |
| **Devolución Parcial** | Control fino de múltiples unidades |
| **Préstamos Vencidos** | Visibilidad de activos retenidos, alertas |
| **Observaciones** | Auditoría profesional, cumplimiento |
| **Historial Completo** | Trazabilidad total, investigaciones |

---

## 🚀 9. PRÓXIMOS PASOS SUGERIDOS

### Phase 2 - Mejoras Futuras

- [ ] Dashboard de alertas en tiempo real
- [ ] Notificaciones automáticas de vencimientos
- [ ] Reportes PDF/Excel profesionales
- [ ] Integración con sistema de órdenes de trabajo
- [ ] Análisis de tendencias de uso
- [ ] Costos de almacenamiento por préstamo

### Phase 3 - Automatización

- [ ] Recordatorios automáticos de devolución
- [ ] Escalamiento automático a supervisores
- [ ] Cargas de multas/penalizaciones
- [ ] API para integración ERP

---

## 📞 SOPORTE TÉCNICO

### Contacto
- **Módulo:** Sistema de Pañol (Herramientas)
- **Versión:** v2.1.0
- **Última Actualización:** March 10, 2026

### Archivos Modificados

```
✅ app/services/paniol_service.py - 6 nuevas funciones avanzadas (líneas 679-1060)
✅ app/routes/herramientas.py - 6 nuevos endpoints API (líneas 843-959)
✅ config.py - Configuración de prefijo NC (líneas 59-60)
```

### Validación

```bash
# Verificar que todo funciona
python -m pytest tests/test_paniol.py -v

# Probar endpoints
curl http://localhost:5000/api/herramientas/suggest-sku
curl http://localhost:5000/api/herramientas/prestamos-vencidos
```

---

## 📋 CHANGELOG RESUMIDO

```
v2.1.0 (2026-03-10)
✨ Operaciones avanzadas de préstamos
✨ Prefijo NC estandarizado
✨ Historial profesional de auditoría
✨ 6 nuevos endpoints API
🔒 Validaciones mejoradas
📊 Mejor trazabilidad
```

---

**Documento Generado:** March 10, 2026  
**Responsable:** Sistema North Chrome v2  
**Estado:** ✅ Producción
