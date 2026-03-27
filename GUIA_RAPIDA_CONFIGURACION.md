# ⚙️ GUÍA RÁPIDA: Panel de Configuraciones

## 🎯 Inicio en 30 segundos

```
1. Ejecuta:      python servidor.py
2. Abre:         http://localhost:5000
3. Busca:        Botón ⚙️ (esquina superior derecha)
4. Haz clic:     ¡Listo!
```

---

## 📋 ¿Qué puedo cambiar?

### 1️⃣ **Tamaño de Letra** 📝
```
↓ Pequeño (14px)    → Para monitores muy grandes
→ Normal (16px)     ← RECOMENDADO
↑ Grande (18px)     → Mejor legibilidad
⇧ Extra Grande (20px) → Máxima accesibilidad
```
**Afecta**: Todos los textos en la interfaz
**Resultado**: Todo se agranda proporcionalmente

### 2️⃣ **Esquema de Colores** 🎨
```
🔄 Automático   ← Sigue tu sistema operativo
🌙 Oscuro       ← Tema actual (profesional)
☀️ Claro        ← Para oficinas iluminadas
```
**Afecta**: Fondo y colores generales
**Resultado**: Interfaz completa en claro/oscuro

### 3️⃣ **Color de Acento** ✨
Elige el color principal para botones, iconos y highlights:
```
🟠 Naranja   🔵 Azul   🟣 Púrpura   🟢 Verde   🔴 Rojo   🩷 Rosa
```
**Afecta**: Botones primarios, iconos activos, enlace
**Resultado**: Brand colors personalizados

### 4️⃣ **Densidad de Contenido** 📊
```
◾ Compacta   → -20% espaciado (ver más datos)
◽ Normal     ← RECOMENDADO (balance)
⬜ Espaciosa → +20% espaciado (más aire)
```
**Afecta**: Padding, márgenes, alto de filas
**Resultado**: Interfaz más compacta o aireada

### 5️⃣ **Familia de Fuente** 🔤
```
◀ Sistema (IBM Plex Sans) ← profesional
📖 Serif (IBM Plex Serif)
⟡ Monoespaciada (IBM Plex Mono)
```
**Afecta**: Tipo de letra en toda la interfaz
**Resultado**: Diferente estilo visual

### 6️⃣ **Opciones Adicionales** ⚡
```
☑ Animaciones     → Transiciones suaves
☑ Notificaciones  → Mensajes tipo Toast
☑ Auto-actualizar → Datos se sincronizan automáticamente
```

---

## 🎬 Paso a Paso

### Para Cambiar Tamaño de Letra

```
1. Abre el panel ⚙️
2. Busca: "📝 Tamaño de Letra"
3. Haz clic en una opción:
   
   ANTES                      DESPUÉS
   ┌──────────────┐          ┌──────────────┐
   │ Pequeño      │    →    │ Grande       │
   │ Texto        │          │ TEXTO        │
   │ Botones      │          │ BOTONES      │
   └──────────────┘          └──────────────┘

4. ¡LISTO! Todos los textos se agrandan al instante
5. Recarga la página → Los cambios persisten
```

### Para Cambiar Tema

```
1. Panel ⚙️
2. Busca: "🎨 Esquema de Colores"
3. Elige: 🌙 Oscuro, ☀️ Claro o 🔄 Automático
4. ¡Cambia instantáneamente!
```

### Para Cambiar Color de Acento

```
1. Panel ⚙️
2. Busca: "✨ Color de Acento"
3. Elige: 🟠 🔵 🟣 🟢 🔴 🩷
4. Botones y iconos cambian al nuevo color
```

---

## 💾 ¿Los Cambios se Guardan?

### ✅ SÍ, AUTOMÁTICAMENTE
```
Usuario realiza cambio
        ↓
Se guarda en navegador (instantáneo)
        ↓
Se sincroniza con servidor (automático)
        ↓
✅ Cambios persisten incluso si cierras sesión
```

### Persistencia LOCAL (sin servidor)
```javascript
// Se guardan en el navegador
localStorage.nc_settings
```

### Persistencia SERVIDOR (base de datos)
```
Tabla: user_settings
Sincronización: Automática en background
```

---

## 🔄 Restablecer Valores por Defecto

```
1. Panel ⚙️
2. Botón abajo: "↻ Restablecer Predeterminados"
3. Confirmar en el diálogo
4. ¡Vuelve todo a lo estándar!
```

---

## 🎨 Presets Recomendados

### 👴 Persona Mayor (Accesibilidad)
```
Tamaño:          Extra Grande ⇧
Esquema:         Claro ☀️
Densidad:        Espaciosa ⬜
Animaciones:     OFF ☐
Color acento:    Verde 🟢
```

### 💼 Gerente Ocupado (Eficiencia)
```
Tamaño:          Normal →
Esquema:         Oscuro 🌙
Densidad:        Compacta ◾
Animaciones:     ON ☑
Color acento:    Azul 🔵
```

### 📱 Oficina Compartida (Estándar)
```
Tamaño:          Grande ↑
Esquema:         Automático 🔄
Densidad:        Normal ◽
Animaciones:     ON ☑
Color acento:    Naranja 🟠
```

### 🌙 Trabajo de Noche (Confort)
```
Tamaño:          Normal →
Esquema:         Oscuro 🌙
Densidad:        Normal ◽
Animaciones:     OFF ☐
Color acento:    Azul 🔵
```

---

## ❓ FAQ Rápidas

### P: ¿Dónde está el botón de configuraciones?
**R**: Esquina superior derecha, botón ⚙️

### P: ¿Si campio de tamaño, se ve mal?
**R**: No, todo se ajusta proporcionalmente. Es 100% profesional.

### P: ¿Los cambios se guardan si cierro la app?
**R**: Sí, automáticamente en el navegador Y en el servidor.

### P: ¿Puedo volver atrás?
**R**: Sí, con el botón "↻ Restablecer Predeterminados"

### P: ¿Funciona en móvil?
**R**: Sí, el panel es 100% responsivo.

### P: ¿Los otros usuarios ven mis cambios?
**R**: No, cada usuario tiene sus propias preferencias.

### P: ¿Qué pasa sin conexión de internet?
**R**: Los cambios se guardan igual en tu navegador. Sin problema.

---

## 🚨 Si Algo Falla

### No veo el botón ⚙️
```bash
1. Recarga la página: F5
2. Limpia caché: Ctrl+Shift+Del
3. Busca en la barra superior derecha
```

### Los cambios no se aplican
```bash
1. Recarga: F5
2. Si persiste, abre la consola: F12
3. Escribe: localStorage.clear()
4. Recarga nuevamente
```

### Error al guardar
```bash
# Los cambios se guardan en el navegador de todas formas
# Intenta nuevamente en unos segundos
# Se sincronizará automáticamente
```

---

## 📊 Combinaciones Populares

| Uso | Tamaño | Tema | Acento | Densidad |
|-----|--------|------|--------|----------|
| Oficina | Grande | Claro | Azul | Normal |
| Noche | Normal | Oscuro | Azul | Normal |
| Personas mayores | ExtraGrand | Claro | Verde | Espaciosa |
| Max productividad | Normal | Oscuro | Orange | Compacta |

---

## ⌨️ Atajos (Bonus)

```javascript
// Abrir consola (F12) y pegar:

// Ver configuración actual
SettingsManager.settings

// Cambiar tamaño (rápido)
SettingsManager.applyFontSize('large')

// Cambiar tema (rápido)
SettingsManager.applyColorScheme('dark')

// Restaurar todo
SettingsManager.resetSettings()

// Limpiar localStorage
localStorage.clear()
```

---

## 🎯 Resumen

```
✅ Abre el panel ⚙️
✅ Elige un tamaño de fuente (↓→↑⇧)
✅ Cambia el esquema de colores (🌙☀️🔄)
✅ Personaliza los acentos (🟠🔵🟣🟢🔴🩷)
✅ Ajusta la densidad (◾◽⬜)
✅ ¡Los cambios se guardan automáticamente!
✅ Recarga la página → Los cambios persisten
✅ ¡Disfruta! ✨
```

---

**¡Eso es todo! Ahora puedes personalizar tu experiencia completamente.**

*Panel de Configuraciones — North Chrome v2* 🚀
