# 🔧 SOPORTE TÉCNICO: Panel de Configuraciones

## 🆘 Centro de Ayuda

### Problema: El botón ⚙️ no aparece

#### ❌ Síntoma
No veo el botón de configuraciones en la barra superior

#### ✅ Solución
```bash
Paso 1: Recarga la página
        → F5 o Ctrl+R

Paso 2: Limpia caché agresivamente
        → Ctrl+Shift+Del
        → Marca todas las opciones
        → Rango: "Todo" o "Última hora"
        → Borrar

Paso 3: Reinicia el navegador
        → Cierra completamente Chrome/Firefox/Edge
        → Abre nuevamente
        → Navega a http://localhost:5000

Paso 4: Verifica que servidor está corriendo
        → Terminal: python servidor.py
        → Busca: "Running on http://localhost:5000"
```

#### 🔍 Verificar en Consola (F12)
```javascript
// Abre: F12 → Console
SettingsManager  // Debe decir: "SettingsManager {}"
SettingsManager.settings  // Debe mostrar las configuraciones
```

---

### Problema: Los cambios no se aplican

#### ❌ Síntoma
Cambio el tamaño de letra pero no se ve diferente

#### ✅ Solución
```bash
Paso 1: Recarga la página
        → F5

Paso 2: Abre las configuraciones nuevamente
        → Botón ⚙️
        → Verifica que el tamaño está guardado

Paso 3: Limpia localStorage
        → F12 → Console
        → Escribe: localStorage.clear()
        → Presiona Enter
        → Recarga: F5

Paso 4: Prueba nuevamente
        → Abre ⚙️
        → Cambia tamaño a "Grande" (↑)
        → Debería verse diferente inmediatamente
```

#### 🔍 Debug Avanzado
```javascript
// En la consola (F12):

// Ver configuración actual
console.log(SettingsManager.settings)

// Aplicar manualmente
SettingsManager.applyFontSize('large')

// Ver CSS inyectado
document.getElementById('nc-font-size').textContent
```

---

### Problema: El modal de configuraciones no abre

#### ❌ Síntoma
Hago clic en ⚙️ pero no pasa nada

#### ✅ Solución
```bash
Paso 1: Abre consola del navegador (F12)
        → Busca errores de JavaScript (en rojo)

Paso 2: Si hay errores, anota qué dice

Paso 3: Recarga la página con consola abierta
        → F5 con F12 ya abierto
        → Busca nuevamente errores

Paso 4: Intenta abrir desde consola
        → Escribe: SettingsManager.openSettings()
        → Presiona Enter
        → Debería abrir el modal

Paso 5: Si aparece el modal, recarga todo
        → Ctrl+Shift+Del (limpiar caché)
        → F5 (recargar)
```

#### 🔍 Mensajes de Error Comunes
```
Error: SettingsManager is not defined
    → settings.js no se cargó
    → Solución: Recarga la página (F5)

Error: Cannot read property 'settings' of undefined
    → SettingsManager no inicializó
    → Solución: Espera a que cargue, recarga

SyntaxError in settings.js:123
    → Error en el código
    → Solución: Contacta a soporte
```

---

### Problema: Los cambios se pierden después de cerrar

#### ❌ Síntoma
Cambio el tamaño de letra, cierro y vuelvo a abrir → vuelve al original

#### ✅ Solución
```bash
Paso 1: Verifica que localStorage está habilitado
        → F12 → Application → LocalStorage
        → Busca: "http://localhost:5000"
        → Debe existir "nc_settings"

Paso 2: Si no existe, localStorage está deshabilitado
        → Privacidad del navegador
        → En Chrome: Configuración → Privacidad
        → Debe permitir cookies y datos locales para localhost

Paso 3: Intenta en Modo Incógnito
        → Si funciona en incógnito, problema de privacidad
        → Si no funciona, problema del servidor

Paso 4: Verifica sincronización con servidor
        → F12 → Network
        → Cambia un ajuste
        → Busca: POST /api/user/settings
        → Debe devolver 200 OK
```

#### Solución por Navegador

**Chrome/Edge:**
```
Configuración → Privacidad → Cookies
→ Permitir cookies de terceros
→ Localhost debe estar en lista blanca
```

**Firefox:**
```
about:config → dom.storage.enabled = true
Luego: Preferencias → Privacidad → Cookies = Aceptar
```

**Safari:**
```
Preferencias → Privacidad → Control de sitios web
→ Permitir almacenamiento local
```

---

### Problema: El servidor no sincroniza

#### ❌ Síntoma
Cambio un ajuste pero el servidor no lo guarda (no veo POST request)

#### ✅ Solución
```bash
Paso 1: Verifica que el servidor está corriendo
        → Terminal: python servidor.py
        → Busca mensaje: "Running on http://localhost:5000"
        → Si no lo ves, el servidor cayó

Paso 2: Si no está corriendo, inicía nuevamente
        → Abre Terminal
        → Navega a la carpeta del proyecto
        → Escribe: python servidor.py
        → Espera a que inicie

Paso 3: Verifica que el módulo user_settings.py existe
        → Carpeta del proyecto
        → Busca archivo: user_settings.py
        → Debe estar ahí

Paso 4: Verifica en Network (F12)
        → F12 → Network → XHR
        → Cambia un ajuste
        → Busca: POST /api/user/settings
        → Verifica status: 200 = OK, 500 = Error

Paso 5: Si hay error 500, revisa logs del servidor
        → Terminal donde corre python
        → Busca: "ERROR" en rojo
        → Anota el mensaje
```

#### 🔍 Log del Servidor
```
Verifica estos mensajes en la terminal:
✅ "✓ SettingsManager initialized"     ← OK
❌ "Error initializing settings DB"    ← Problema BD
❌ "Error saving settings"              ← Problema al guardar
✅ "POST /api/user/settings - 200"     ← Guardado exitoso
```

---

### Problema: Base de datos corrupta

#### ❌ Síntoma
Errores persistentes de "usuario no encontrado" o "error BD"

#### ✅ Solución
```bash
Paso 1: Detén el servidor
        → En la terminal: Ctrl+C

Paso 2: Borra la base de datos
        → Abre File Explorer
        → Navega: proyecto/system/
        → Busca: system.db (o system.db-wal)
        → Elimina AMBOS archivos

Paso 3: Reinicia el servidor
        → python servidor.py
        → Creará una BD nueva automáticamente

Paso 4: Prueba nuevamente
        → Abre http://localhost:5000
        → Verifica ⚙️ panel
```

**ADVERTENCIA**: Esto borrará TODOS los datos. Haz backup primero si es importante.

---

### Problema: Las fuentes no se ven diferente

#### ❌ Síntoma
Cambio de "System" a "Serif" pero se ve igual

#### ✅ Solución
```bash
Paso 1: Verifica CSS inyectado
        → F12 → Elements
        → Busca: <style id="nc-font-family">
        → Debe contener cambios de font-family

Paso 2: Si no está, recarga
        → F5
        → Abre configuraciones nuevamente
        → Cambia fuente
        → Verifica HTML nuevamente

Paso 3: Verifica que fuentes están cargadas
        → F12 → Network → Fonts
        → Busca: IBM Plex Sans, IBM Plex Serif, IBM Plex Mono
        → Todos deben estar "200 OK"

Paso 4: Si no están cargadas
        → Problema de Google Fonts
        → Recarga la página
        → Intenta en navegador diferente
```

---

### Problema: Modal se abre pero se ve roto

#### ❌ Síntoma
El panel de configuraciones aparece pero botones están desalineados

#### ✅ Solución
```bash
Paso 1: Limpia caché CSS
        → Ctrl+Shift+Del
        → Marca: "Imágenes y archivos en caché"
        → Rango: "Todo"
        → Borrar

Paso 2: Recarga agresivamente
        → Ctrl+Shift+F5 (recarga con caché limpio)

Paso 3: Verifica CSS se cargó
        → F12 → Elements
        → Busca: <link rel="stylesheet" href="settings-styles.css">
        → Debe existir y estar con estado 200

Paso 4: Si CSS no se cargó
        → Verifica archivo existe en carpeta del proyecto
        → Archivo: settings-styles.css
        → Tamaño debe ser: ~15KB

Paso 5: Prueba en navegador diferente
        → Si funciona en otro navegador = problema caché
        → Si falla en todos = problema archivo
```

---

### Problema: Error "SyntaxError in settings.js"

#### ❌ Síntoma
Consola muestra error de JavaScript en settings.js

#### ✅ Solución
```bash
Paso 1: Nota el número de línea del error
        → Ej: "settings.js:234"

Paso 2: Redownload el archivo
        → settings.js puede estar corrupto
        → Vuelve a descargarlo o cópialo de backup

Paso 3: Verifica que archivo existe
        → Carpeta del proyecto
        → Archivo: settings.js
        → Tamaño debe ser: ~150KB

Paso 4: Limpiar e intentar
        → Caché: Ctrl+Shift+Del
        → Recarga: F5

Paso 5: Si persiste, contacta soporte
        → Mensaje: "Error en settings.js línea X"
        → Proporciona mensaje completo del error
```

---

## 📋 Checklist de Verificación

### Antes de Reportar un Problema

```
☐ ¿Recargué la página? (F5)
☐ ¿Limpié caché? (Ctrl+Shift+Del)
☐ ¿Reinicié el navegador?
☐ ¿El servidor está corriendo? (python servidor.py)
☐ ¿Usé Firefox/Chrome/Edge actualizado?
☐ ¿Probé en navegador diferente?
☐ ¿Limpié localStorage? (consola: localStorage.clear())
☐ ¿Verificé consola (F12) para errores?
☐ ¿Probé el preset recomendado?
```

---

## 🐛 Reporte de Bugs

Si después de todo aún falla, recolecta esta información:

```
1. ERROR EXACTO (copia de consola):
   → 

2. PASOS PARA REPRODUCIR:
   → 1. 
   → 2. 
   → 3. 

3. QUE ESPERABAS VER:
   → 

4. QUE VES EN REALIDAD:
   → 

5. NAVEGADOR Y VERSIÓN:
   → Ej: Chrome 120.0

6. SISTEMA OPERATIVO:
   → Ej: Windows 11

7. HASD INTENTADO (marca):
   ☐ Recargar página
   ☐ Limpiar caché
   ☐ Reiniciar navegador
   ☐ Reiniciar servidor
   ☐ Probar en otro navegador
```

---

## 🔍 Diagnosticar en Consola

```javascript
// Abre: F12 → Console (pestaña)

// 1. Ver TODAS las configuraciones
console.log(SettingsManager.settings)

// 2. Ver localStorage
console.log(localStorage.getItem('nc_settings'))

// 3. Cambiar tamaño directamente
SettingsManager.setSetting('fontSize', 'xlarge')

// 4. Cambiar tema directamente
SettingsManager.setSetting('colorScheme', 'dark')

// 5. Cambiar color acento directamente
SettingsManager.setSetting('accentColor', 'blue')

// 6. Restaurar TODO a valores por defecto
SettingsManager.resetSettings()

// 7. Abrir modal manualmente
SettingsManager.openSettings()

// 8. Cerrar modal manualmente
SettingsManager.closeSettings()

// 9. Ver si se sincroniza con servidor
SettingsManager.sendToServer()

// 10. Limpiar TODA la configuración local
localStorage.clear()

// 11. Forzar recarga con F5 después
```

---

## 🆘 Contacto de Soporte

Si nada funciona:

1. **Recolecta info** (ver sección "Reporte de Bugs")
2. **Abre consola** (F12)
3. **Copia el error**
4. **Incluye pasos** para recrear
5. **Contacta al administrador**

Información útil a proporcionar:
- Navegador y versión
- Sistema operativo
- Mensaje de error exacto
- Pasos para reproducir
- Qué ya intentaste

---

## 📊 Tabla de Solución Rápida

| Problema | Solución Rápida |
|----------|-----------------|
| No veo ⚙️ | F5 + Ctrl+Shift+Del |
| Cambios no aplican | F5 + localStorage.clear() |
| Modal no abre | F12 + ejecutar SettingsManager.openSettings() |
| Cambios se pierden | F12 + ejecutar SettingsManager.sendToServer() |
| BD corrupta | Detener servidor + eliminar system.db |
| CSS roto | Ctrl+Shift+F5 (reload con caché limpio) |
| Error de JS | Recarga + limpiar caché + reiniciar |
| Fuentes no cambian | Network tab + verificar CSS inyectado |

---

**¡Espero que esto resuelva tu problema! 😊**

*Si no, no dudes en contactar a soporte con la información del bug.*

---

North Chrome v2 — Soporte Técnico ✨
