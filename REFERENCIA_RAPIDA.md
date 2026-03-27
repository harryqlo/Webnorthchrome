# 📋 REFERENCIA RÁPIDA Y CHEATSHEET
**Guía de consulta rápida - Guardar para referencia futura**

---

## 🚨 EMERGENCIAS

### BD Corrupta o Perdida
```
RÁPIDO:
1. Ir a: system/backups/
2. Copiar último archivo system_*.backup
3. Pegarla como system.db
4. Reiniciar servidor

PREVENCIÓN: Ejecutar backup_automatico.ps1 diariamente
```

### Sistema muy lento
```
DIAGNOSTICAR:
1. Ver logs en: logs/app.log
2. Check BD: python -c "import sqlite3; sqlite3.connect('system/system.db').execute('ANALYZE')"
3. Ver usuarios conectados: No hay logging aún (implementar Fase 1)

SOLUCIONAR:
1. Agregar índices (ver MEJORAS_RAPIDAS_CODIGO.md #7)
2. Migrar a PostgreSQL (Fase 2)
3. Bajar tamaño de consultas (usar paginación)
```

### Alguien accedió sin permiso
```
VERIFICAR:
1. No hay autenticación todavía
2. Sistema local solamente

IMPLEMENTAR:
1. Ver AUDITORIA_PROFESIONAL.md #3 (Vulnerabilidades)
2. Fase 1: Implementar JWT (PLAN_ACCION_EJECUTABLE.md)
```

---

## 📊 TABLA DE PROBLEMAS Y SOLUCIONES

| Problema | Severidad | Solución | Tiempo | Costo |
|----------|-----------|----------|--------|-------|
| Sin backup | 🔴 CRÍTICO | backup_automatico.ps1 | 5 min | $0 |
| Sin autenticación | 🔴 CRÍTICO | JWT (Fase 1) | 4h | $200 |
| Performance lento | 🟠 ALTO | Índices SQL + PostgreSQL | 3h + 20h | $500 + $1000 |
| Sin logging | 🟠 ALTO | logger_config.py | 2h | $100 |
| Sin validación input | 🟠 ALTO | validators.py | 2h | $100 |
| Código difícil mantener | 🟡 MEDIO | Refactor (renombrar) | 2h | $100 |
| Sin tests | 🟡 MEDIO | pytest setup | 3h | $150 |
| Sin documentación API | 🟡 MEDIO | Swagger/OpenAPI | 2h | $100 |

---

## 🔧 ARCHIVOS A CREAR/MODIFICAR

### Crear estos archivos NUEVOS:
```
✓ .env                    (5 min)
✓ config.py               (10 min)
✓ validators.py           (30 min)
✓ logger_config.py        (20 min)
✓ tests/test_inventory.py (30 min)
✓ .gitignore              (5 min)
```

### Modificar estos archivos EXISTENTES:
```
✓ servidor.py         (Refactor: 1h)
✓ index.html          (Modularizar: 2h, opcional)
```

### Scripts listos para usar:
```
✓ backup_automatico.ps1
✓ backup_automatico.bat
```

---

## 🎯 DOCUMENTOS POR NECESIDAD

### Necesito entender qué está mal
→ [AUDITORIA_PROFESIONAL.md](AUDITORIA_PROFESIONAL.md) sección 2

### Necesito entender por qué es importante
→ [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md) sección "Análisis Costo-Beneficio"

### Necesito empezar ahora
→ [QUICK_START.md](QUICK_START.md)

### Necesito código listo
→ [MEJORAS_RAPIDAS_CODIGO.md](MEJORAS_RAPIDAS_CODIGO.md)

### Necesito entender el plan
→ [ROADMAP_VISUAL.md](ROADMAP_VISUAL.md)

### Necesito saber qué hacer cada día
→ [PLAN_ACCION_EJECUTABLE.md](PLAN_ACCION_EJECUTABLE.md)

### Necesito navegar todo
→ [INDICE_NAVEGACION.md](INDICE_NAVEGACION.md)

---

## 📞 PREGUNTAS COMUNES

**P: ¿Cuánto tiempo toma todo?**
A: 4h (mejoras rápidas) → 40h (seguridad) → 60h (escalabilidad) = 104h total

**P: ¿Puedo hacer solo backup y dejar así?**
A: Sí para 1-2 usuarios. No si necesitas multiusuario/crítico.

**P: ¿Necesito reescribir todo?**
A: No. Refactor progresivo/incremental.

**P: ¿Cuánto cuesta?**
A: $200 (solo mejoras) → $5,500 (profesional) según profundidad

**P: ¿Puedo hacer en paralelo con usuarios?**
A: Sí en Fase 0. No en Fase 1-2 (requieren parada mínima).

**P: ¿Qué es más urgente?**
A: 1. Backup, 2. Autenticación, 3. Performance

**P: ¿Necesito base de datos nueva?**
A: SQLite OK para ≤100 usuarios. PostgreSQL si creces más.

---

## 🚀 COMANDOS RÁPIDOS

```powershell
# Ejecutar backup AHORA
powershell -ExecutionPolicy Bypass -File backup_automatico.ps1

# Iniciar Git
git init
git add .
git commit -m "North Chrome baseline"

# Ver logs
type logs/app.log

# Instalar dependencias Python futura
# pip install -r requirements.txt

# Ejecutar tests futuro
# pytest tests/ -v

# Crear backup manual
cp system/system.db system/backups/system_manual_$(Get-Date -Format 'yyyyMMdd').db
```

---

## ✅ CHECKLISTS RÁPIDOS

### Backup Configurado ✓
- [ ] backup_automatico.ps1 ejecutado
- [ ] Archivo en system/backups/ existe
- [ ] Task Scheduler configurado (opcional)

### Proyecto Seguro ✓
- [ ] .gitignore creado (no commitear .env, DB)
- [ ] .env creado con secretos
- [ ] Git repo iniciado
- [ ] First commit hecho

### Código Mejorado ✓
- [ ] config.py creado
- [ ] validators.py creado
- [ ] logger_config.py creado
- [ ] Funciones renombradas
- [ ] Docstrings añadidos
- [ ] Índices SQL creados

### Listo para Producción (Fase 1)✓
- [ ] Autenticación JWT
- [ ] RBAC implementado
- [ ] Tests pasando
- [ ] API docs (Swagger)
- [ ] Encriptación de datos
- [ ] Logging completo

---

## 📊 SCORECARD ACTUAL vs META

```
┌─────────────────┬──────────┬─────────┐
│ Habilidad       │ Actual   │ Meta    │
├─────────────────┼──────────┼─────────┤
│ Seguridad       │ 1/10     │ 9/10    │
│ Performance     │ 5/10     │ 9/10    │
│ Mantenibilidad  │ 3/10     │ 8/10    │
│ Documentación   │ 2/10     │ 8/10    │
│ Testing         │ 0/10     │ 7/10    │
│ Escalabilidad   │ 2/10     │ 8/10    │
│ Confiabilidad   │ 2/10     │ 9/10    │
├─────────────────┼──────────┼─────────┤
│ PROMEDIO        │ 2.1/10   │ 8.3/10  │
└─────────────────┴──────────┴─────────┘
```

---

## 🎓 REFERENCIAS TÉCNICAS

### Tecnologías a implementar
```
Autenticación: Flask-JWT-Extended
Validación: Pydantic
Logging: Python logging + Winston
Testing: pytest
ORM: SQLAlchemy (opcional)
Cache: Redis (opcional)
Deployment: Docker + gunicorn
CI/CD: GitHub Actions / GitLab CI
```

### Estándares a seguir
```
Code style: PEP 8
Git flow: trunk-based development
Testing: 80%+ coverage
Security: OWASP Top 10
Documentation: Docstrings + Swagger API
```

---

## 💰 PRESUPUESTO ESTIMADO

```
Si lo hace equipo interno:
────────────────────────
Staff cost (150h @ $25/h):        $3,750
Herramientas/licencias:            $200
Infraestructura (cloud):           $500
────────────────────────
TOTAL:                            $4,450

Si lo contrata tercero:
────────────────────────
Consultoría (aceleración):         $500
Desarrollo (150h @ $50/h):       $7,500
Testing/QA:                     $1,000
────────────────────────
TOTAL:                           $9,000

ROI 12 meses:
────────────────────────
Prevención de issues:          +$10,000
Reducción de bugs (-80%):       +$8,000
Productivity (+30%):             +$5,000
Escalabilidad:                  +$3,000
────────────────────────
TOTAL BENEFITS:                +$26,000
ROI: 580%
```

---

## 🔐 SEGURIDAD CHECKLIST

Implementar en Fase 1:
- [ ] Autenticación múltiple usuarios
- [ ] Roles (Admin, Manager, Viewer)
- [ ] Hash de passwords (bcrypt)
- [ ] Encriptación datos sensibles
- [ ] HTTPS en producción
- [ ] CORS configuration
- [ ] Rate limiting en API
- [ ] Audit logging completo
- [ ] SQL injection prevention (parametrized)
- [ ] XSS prevention (sanitize output)

---

## 📈 PERFORMANCE TARGETS

| Métrica | Actual | Meta |
|---------|--------|------|
| Tiempo respuesta | >2s | <200ms |
| Usuarios simultáneos | 1 | 100+ |
| Uptime | ? | 99.5% |
| DB query avg | ? | <100ms |
| Memory usage | ? | <500MB |
| Disk space | <1GB | <10GB |

---

## 🎯 DECISION MATRIX

¿Qué gastar primero?

```
PRIORITARIO:
1. Backup automático ($0, 5 min)      → MÁXIMO IMPACTO
2. Autenticación ($200, 4h)            → CRÍTICO
3. Validación input ($100, 2h)         → CRÍTICO

IMPORTANTE:
4. Logging completo ($100, 2h)         → ALTO
5. PostgreSQL ($1000, 20h)             → ALTO
6. Tests ($150, 3h)                    → MEDIO

OPCIONAL:
7. Analytics dashboard ($200, 5h)     → MEDIO
8. PWA offline ($300, 8h)             → BAJO
9. Webhooks ($200, 4h)                → BAJO
```

---

**Última actualización:** 5 de Marzo de 2026  
**Mantener esta referencia para:** Decisiones futuras, emergencias, planning

¿Necesitas algo específico? Busca en [INDICE_NAVEGACION.md](INDICE_NAVEGACION.md)
