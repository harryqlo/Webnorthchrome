# Manual de Usuario - Sistema de Pañol

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Dashboard Pañol](#dashboard-pañol)
3. [Gestión de Empleados](#gestión-de-empleados)
4. [Gestión de Herramientas](#gestión-de-herramientas)
5. [Préstamo de Herramientas](#préstamo-de-herramientas)
6. [Devolución de Herramientas](#devolución-de-herramientas)
7. [Mantenimiento](#mantenimiento)
8. [Planes de Mantenimiento](#planes-de-mantenimiento)
9. [Reportes y Consultas](#reportes-y-consultas)

---

## Introducción

El **Sistema de Pañol** es un módulo integrado al sistema de bodega que permite:
- Control de herramientas y equipos
- Administración de préstamos y devoluciones
- Seguimiento de empleados autorizados
- Gestión de mantenimientos preventivos y correctivos
- Alertas de calibraciones vencidas
- Reportes de costos y utilización

### Acceso al Módulo

Para acceder al sistema de pañol:
1. Abra el menú lateral (☰) si está colapsado
2. Localice la sección **"Pañol"**
3. Encontrará tres opciones:
   - **Dashboard Pañol**: Vista general con KPIs y gráficos
   - **Empleados**: Gestión de personal autorizado
   - **Herramientas**: Inventario y control de herramientas

---

## Dashboard Pañol

### KPIs (Indicadores Clave)

El dashboard muestra 6 indicadores principales:

**🟢 Indicadores Normales:**
- **Total Herramientas**: Cantidad total en inventario
- **Prestadas Actualmente**: Herramientas en préstamo activo
- **En Mantenimiento**: Herramientas en reparación/mantención
- **Defectuosas**: Herramientas en mal estado

**🔴 Alertas Críticas:**
- **⚠️ Mant. Vencidos**: Mantenimientos atrasados (rojo)
- **🔧 Calib. Vencidas**: Calibraciones expiradas (naranja)

### Préstamos Activos

Tabla con todas las herramientas actualmente prestadas:
- Empleado que la tiene
- Herramienta y SKU
- Cantidad prestada
- Fecha de préstamo
- **Días prestados** (se resalta en rojo si supera 30 días)
- Botón **"Devolver"** para registrar la devolución

### Alertas de Mantenimiento

Si hay herramientas con mantenimiento o calibración vencida, aparecerá una sección de alertas mostrando:
- Nombre y SKU de la herramienta
- Tipo de alerta (mantenimiento o calibración)
- Días de retraso

### Gráficos de Análisis

**Top 5 Empleados con Más Préstamos**
- Gráfico de barras horizontal
- Muestra quiénes tienen más herramientas prestadas actualmente

**Herramientas Más Utilizadas**
- Gráfico de barras
- Indica las 5 herramientas más solicitadas

**Costos de Mantenimiento Últimos 6 Meses**
- Gráfico de línea
- Muestra evolución de gastos en mantenimiento mes a mes

---

## Gestión de Empleados

### Listar Empleados

**Filtros disponibles:**
- **Búsqueda por texto**: Nombre, número de empleado, RUT, cargo
- **Departamento**: Mantención, Producción, Electricidad, Mecánica, Bodegas
- **Cargo**: Técnico, Operario, Supervisor, Jefe de Mantención, etc.

**Columnas mostradas:**
- Nº Empleado
- Nombre completo
- RUT
- Cargo
- Departamento
- Email
- Estado (Activo/Inactivo con badge de color)
- Acciones (Editar ✎ / Eliminar ✕)

### Crear Nuevo Empleado

1. Click en **"+ Nuevo Empleado"**
2. Complete el formulario:
   - **Nº Empleado** *: Auto-sugerido (ej: EMP001)
   - **Nombre Completo** *: Nombre y apellido
   - **RUT**: Formato 12345678-9
   - **Email**: Correo electrónico
   - **Cargo**: Seleccione de lista o escriba uno nuevo
   - **Departamento**: Seleccione de lista o escriba uno nuevo
   - **Teléfono**: Con código de país (ej: +56912345678)
   - **Estado**: Activo o Inactivo
3. Click en **"Guardar"**

**Campos obligatorios:** Marcados con asterisco (*)

### Editar Empleado

1. Click en **✎** en la fila del empleado
2. Modifique los datos necesarios
3. Click en **"Guardar"**

**Nota**: El número de empleado no se puede cambiar una vez creado.

### Eliminar Empleado

1. Click en **✕** en la fila del empleado
2. Confirme la eliminación

**Restricción**: No se puede eliminar un empleado que tenga herramientas prestadas actualmente.

---

## Gestión de Herramientas

### Listar Herramientas

**Filtros disponibles:**
- **Búsqueda**: SKU, nombre, categoría, marca
- **Estado**: Operativa, Mantenimiento, Defectuosa, Baja
- **Categoría**: Herramientas Manuales, Eléctricas, Instrumentos de Medición, etc.

**Columnas mostradas:**
- SKU
- Nombre
- Categoría
- Cantidad Total
- **Disponible** (en verde si hay stock, rojo si está agotado)
- Estado (badge con color según condición)
- Calibración (próxima fecha o "Sin calibrar")
- Acciones:
  - 📊 **Kardex**: Historial de movimientos
  - 🔧 **Mantenimiento**: Registrar mantención
  - ✎ **Editar**: Modificar datos
  - ✕ **Eliminar**: Quitar del inventario

### Crear Nueva Herramienta

1. Click en **"+ Nueva Herramienta"**
2. Complete el formulario:

**Datos Básicos:**
- **SKU** *: Auto-sugerido (ej: HERR001)
- **Nombre** *: Descripción de la herramienta
- **Categoría**: Tipo de herramienta
- **Marca**: Fabricante
- **Modelo**: Modelo específico
- **Nº Serie**: Número de serie único

**Inventario:**
- **Cantidad Total** *: Cuántas unidades hay
- **Ubicación**: Estante/casillero (ej: Pañol A-12)

**Estado y Valor:**
- **Estado**: Operativa, Mantenimiento, Defectuosa, Baja
- **Valor Unitario**: Costo en pesos

**Calibración (opcional):**
- ☑️ **Requiere Calibración**: Marcar si la herramienta necesita calibración
  - **Frecuencia Calibración**: Cada cuántos días (ej: 365 para anual)
  - **Última Calibración**: Fecha de última calibración realizada

**Descripción:**
- Campo libre para notas adicionales

3. Click en **"Guardar"**

**Nota**: Si marca "Requiere Calibración", el sistema alertará automáticamente cuando expire.

### Editar Herramienta

1. Click en **✎** en la fila de la herramienta
2. Modifique los datos necesarios
3. Click en **"Guardar"**

**Nota**: El SKU no se puede cambiar una vez creado.

### Ver Kardex de Herramienta

1. Click en **📊** en la fila de la herramienta
2. Se abrirá un modal con timeline visual mostrando:
   - 📤 **Préstamos**: Salida a empleado
   - 📥 **Devoluciones**: Retorno con estado
   - Fecha de cada movimiento
   - Empleado involucrado
   - Cantidad
   - Observaciones

---

## Préstamo de Herramientas

### Proceso de Checkout (Préstamo)

**Acceso rápido:**
- Desde el Dashboard: Botón **"📤 Prestar Herramientas"**
- Desde Herramientas: Botón **"📤 Prestar"**

**Pasos:**

1. **Datos del Préstamo**
   - **Fecha**: Por defecto hoy (modificable)
   - **Empleado**: Escriba número o nombre, seleccione de la lista
   - **Observaciones**: Proyecto, ubicación, motivo, etc.

2. **Agregar Herramientas**
   - **Herramienta**: Escriba SKU o nombre
   - **Cantidad**: Cuántas unidades prestar
   - Click en **"+ Agregar"**
   
   Se mostrará:
   - Disponible actual
   - Validación de stock suficiente
   - Confirmación visual en tabla

3. **Revisar Resumen**
   - Total de Items (tipos de herramientas)
   - Total de Herramientas (suma de cantidades)
   - Lista completa con posibilidad de eliminar items (✕)

4. Click en **"✓ Registrar Préstamo"**

**Validaciones automáticas:**
- ✅ Empleado debe existir y estar activo
- ✅ Herramienta debe estar operativa
- ✅ No se puede prestar más de lo disponible
- ✅ Fecha no puede ser futura

### Préstamo Batch (Múltiples Herramientas)

Puede agregar todas las herramientas necesarias **antes de confirmar** el préstamo. Esto permite generar un solo registro de salida para un proyecto o tarea específica.

**Ventaja**: Registro histórico agrupado y trazabilidad completa.

---

## Devolución de Herramientas

### Proceso de Checkin (Devolución)

**Acceso:**
- Desde Dashboard: Tabla "Préstamos Activos" → Botón **"Devolver"**

**Pasos:**

1. **Revisar Datos Automáticos**
   - Herramienta (solo lectura)
   - Empleado (solo lectura)
   - Cantidad prestada (solo lectura)

2. **Completar Devolución**
   - **Fecha Devolución**: Por defecto hoy
   - **Estado al Devolver**: ¡IMPORTANTE!
     - **Operativa**: Herramienta en perfectas condiciones
     - **Requiere Mantenimiento**: Necesita revisión/reparación
     - **Defectuosa**: No funciona o está dañada
   - **Observaciones**: 
     - **Obligatorio si estado ≠ Operativa**
     - Describa daños, faltantes, condición, etc.

3. Click en **"Registrar Devolución"**

**¿Qué sucede al devolver?**
- ✅ El préstamo se marca como devuelto
- ✅ La cantidad vuelve al stock disponible
- ✅ Se actualiza el estado de la herramienta si cambió
- ✅ Queda registrado en el kardex

**Importante**: Si devuelve como "Defectuosa" o "Requiere Mantenimiento", la herramienta **NO estará disponible** para nuevos préstamos hasta que se repare o se cambie manualmente su estado.

---

## Mantenimiento

### Registrar Mantenimiento

**Acceso:**
- Desde Herramientas: Click en **🔧** en la fila de la herramienta

**Tipos de Mantenimiento:**
- **Preventivo**: Mantención programada (cambio de aceite, lubricación, ajustes)
- **Correctivo**: Reparación de falla o desperfecto
- **Calibración**: Certificación de precisión (instrumentos de medición)

**Pasos:**

1. **Datos del Mantenimiento**
   - Herramienta (automático)
   - **Tipo**: Seleccione preventivo, correctivo o calibración
   - **Fecha**: Cuándo se realizó
   - **Descripción**: Detalle del trabajo realizado (obligatorio)

2. **Costos y Responsable**
   - **Costo**: Monto gastado en pesos (opcional)
   - **Realizado Por**: Nombre del técnico o empresa
   
3. **Observaciones**
   - Notas adicionales, repuestos usados, recomendaciones

4. Click en **"Registrar Mantenimiento"**

**Efecto:**
- ✅ Se registra en historial de mantenimientos
- ✅ Si es calibración, actualiza la fecha de próxima calibración
- ✅ Si hay un plan de mantenimiento, actualiza las fechas
- ✅ Se contabiliza en estadísticas de costos

### Consultar Historial de Mantenimientos

**Opción 1**: Desde el kardex de la herramienta (📊)

**Opción 2**: API endpoints:
- Mantenimientos vencidos: `/api/herramientas/mantenimientos-vencidos`
- Calibraciones vencidas: `/api/herramientas/calibraciones-vencidas`
- Costos por período: `/api/herramientas/costos-mantenimiento?meses=6`

---

## Planes de Mantenimiento

### ¿Qué son los Planes de Mantenimiento?

Son **recordatorios automáticos** para realizar mantenimientos preventivos o calibraciones según frecuencia definida.

**Ejemplo**: Un torquímetro requiere calibración cada 365 días. El plan alertará cuando se acerque o pase la fecha.

### Crear Plan de Mantenimiento

**Acceso:**
- Menú Herramientas → (funcionalidad futura en interfaz)
- Actualmente vía API: `POST /api/herramientas/planes-mantenimiento`

**Datos necesarios:**
- **Herramienta**: SKU o ID
- **Tipo**: Preventivo o Calibración
- **Frecuencia**: Cada cuántos días (ej: 30, 90, 365)

**Funcionalidad:**
- El sistema calcula automáticamente la próxima fecha según el último mantenimiento
- Si no hay mantenimiento previo, usa la fecha de creación del plan
- Alerta cuando está vencido (aparece en Dashboard con badge rojo)

### Estados de Planes

- 🟢 **Al día**: Próximo mantenimiento aún no vence
- 🔴 **Vencido**: Ya pasó la fecha programada

### Listar Planes

`GET /api/herramientas/planes-mantenimiento`

Muestra:
- Herramienta
- Tipo de mantenimiento
- Frecuencia (días)
- Último mantenimiento realizado
- Próximo mantenimiento programado
- Estado actual

### Eliminar Plan

Si ya no se requiere el plan (herramienta dada de baja, cambio de política):
`DELETE /api/herramientas/planes-mantenimiento/:id`

---

## Reportes y Consultas

### Estadísticas Generales

**Endpoint**: `GET /api/herramientas/stats`

Retorna:
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

### Préstamos Activos

**Endpoint**: `GET /api/herramientas/prestamos-activos`

Lista todos los préstamos sin devolución, con:
- Empleado (nombre y número)
- Herramienta (nombre y SKU)
- Cantidad prestada
- Fecha de préstamo
- Días transcurridos (calculado)

### Calibraciones Vencidas

**Endpoint**: `GET /api/herramientas/calibraciones-vencidas`

Herramientas con calibración expirada:
- Nombre y SKU
- Fecha de última calibración
- Días de retraso

### Mantenimientos Vencidos

**Endpoint**: `GET /api/herramientas/mantenimientos-vencidos`

Herramientas con mantenimiento atrasado según su plan:
- Nombre y SKU
- Fecha programada
- Días de retraso

### Costos de Mantenimiento

**Endpoint**: `GET /api/herramientas/costos-mantenimiento?meses=6`

Resumen de gastos por mes:
```json
{
  "costos": [
    {"mes": "2025-09", "total": 125000},
    {"mes": "2025-10", "total": 89000},
    ...
  ],
  "total_periodo": 654000
}
```

### Búsqueda de Herramientas

**Endpoint**: `GET /api/herramientas/search?q=taladro`

Búsqueda rápida por:
- SKU
- Nombre
- Categoría
- Marca/modelo

---

## Flujo de Trabajo Típico

### Caso 1: Préstamo Sencillo

1. Empleado solicita un taladro
2. Pañolero abre **"📤 Prestar Herramientas"**
3. Selecciona empleado: "Juan Pérez"
4. Agrega herramienta: "HERR015 - Taladro Bosch"
5. Confirma préstamo
6. ✅ Sistema registra salida

### Caso 2: Préstamo Proyecto

1. Supervisor solicita kit completo para proyecto
2. Pañolero abre checkout
3. Selecciona empleado: "Pedro Supervisor"
4. Observaciones: "Proyecto Mantención Línea 3"
5. Agrega múltiples herramientas:
   - Taladro x1
   - Destornillador eléctrico x2
   - Multímetro x1
   - Escalera x1
6. Confirma préstamo batch
7. ✅ Todo registrado en un solo movimiento

### Caso 3: Devolución con Daño

1. Empleado devuelve herramienta dañada
2. Pañolero localiza préstamo en Dashboard
3. Click en **"Devolver"**
4. Estado: **"Defectuosa"**
5. Observaciones: "Cable cortado, necesita reemplazo"
6. Confirma devolución
7. ✅ Herramienta queda NO DISPONIBLE hasta reparación
8. Pañolero registra mantenimiento correctivo
9. Cambia estado manualmente a "Operativa"
10. ✅ Herramienta vuelve a estar disponible

### Caso 4: Mantenimiento Preventivo

1. Dashboard muestra alerta: "Calib. Vencidas: 3"
2. Pañolero revisa calibraciones vencidas
3. Identifica "Torquímetro Digital"
4. Envía a calibración externa
5. Cambia estado a "Mantenimiento"
6. Al recibir certificado, registra mantenimiento:
   - Tipo: Calibración
   - Costo: $35000
   - Realizado por: "Empresa Calibraciones Chile"
7. Cambia estado a "Operativa"
8. ✅ Sistema actualiza próxima calibración automáticamente

---

## Mejores Prácticas

### ✅ DO - Haga esto:

- **Registre observaciones detalladas** en préstamos y devoluciones
- **Verifique el estado** de herramientas al devolver
- **Mantenga actualizado** el campo de ubicación
- **Cree planes de mantenimiento** para herramientas críticas
- **Revise diariamente** las alertas del dashboard
- **Documente daños** en observaciones de devolución
- **Use SKUs consistentes** (ej: HERR001, HERR002...)

### ❌ DON'T - Evite esto:

- **No ignore alertas** de calibraciones vencidas
- **No preste herramientas defectuosas** sin antes repararlas
- **No omita observaciones** en devoluciones con problemas
- **No elimine empleados** con préstamos activos
- **No modifique estados** sin registrar el motivo
- **No duplique SKUs** de herramientas

### 🔧 Mantenimiento del Sistema

**Diario:**
- Revisar préstamos activos
- Verificar alertas del dashboard

**Semanal:**
- Revisar herramientas con préstamos > 30 días
- Verificar calibraciones próximas a vencer

**Mensual:**
- Análisis de costos de mantenimiento
- Revisión de empleados con más préstamos
- Limpieza de herramientas dadas de baja

---

## Soporte y Contacto

Para problemas técnicos o dudas sobre el sistema:
- Consulte este manual primero
- Revise la documentación técnica (`DOCUMENTACION_TECNICA_PANIOL.md`)
- Contacte al administrador del sistema

---

**Versión**: 1.0  
**Última actualización**: Marzo 2026  
**Sistema**: North Chrome Warehouse Management
