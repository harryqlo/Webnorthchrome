# PHASE 1 - AUTENTICACIÓN JWT
**Semanas 3-4: Implementar autenticación segura con JWT tokens**

---

## 📋 OBJETIVOS PHASE 1

```
ANTES: Sistema abierto (anyone puede acceder)
DESPUÉS: Autenticación multi-usuario con JWT tokens
```

**Resultados esperados:**
- ✅ Sistema de login/logout funcional
- ✅ JWT tokens con expiración
- ✅ Endpoints protegidos con @jwt_required()
- ✅ Tabla users en BD
- ✅ Audit log de accesos
- ✅ Tests de autenticación
- ✅ RBAC básico (próximamente)

---

## 🎯 PLAN SEMANA 3 (JWT Implementation)

### Día 1-2: Estructura Base
1. Crear auth.py module (AUTH_CONFIG, funciones helper)
2. Agregar tabla users a BD
3. Crear endpoint POST /api/login
4. Crear endpoint POST /api/logout
5. Tests para login/logout

### Día 3-4: Protección de Rutas
1. Crear decorador @jwt_required()
2. Aplicar a 5 endpoints críticos
3. Manejar excepciones (token expirado, inválido)
4. Tests de acceso denegado

### Día 5: Hardening
1. Refresh tokens
2. Blacklist de tokens revocados
3. Rate limiting en login
4. Audit log completo

---

## 💻 IMPLEMENTATION GUIDE

### Paso 1: Instalar dependencias

```bash
pip install Flask-JWT-Extended bcrypt
pip install -U requirements.txt
```

### Paso 2: Crear auth.py

```python
"""
Módulo de autenticación JWT
"""
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from datetime import datetime, timedelta
import bcrypt
from functools import wraps

# Configuración
HASH_ROUNDS = 12
TOKEN_EXPIRATION = timedelta(hours=24)
REFRESH_TOKEN_EXPIRATION = timedelta(days=30)

def hash_password(password):
    """Hashear contraseña con bcrypt"""
    salt = bcrypt.gensalt(rounds=HASH_ROUNDS)
    return bcrypt.hashpw(password.encode(), salt).decode()

def verify_password(password, hashed):
    """Verificar contraseña"""
    return bcrypt.checkpw(password.encode(), hashed.encode())

def create_jwt_token(user_id, username, role='user'):
    """Crear JWT token con claims"""
    return create_access_token(
        identity=user_id,
        additional_claims={
            'username': username,
            'role': role,
            'created_at': datetime.utcnow().isoformat()
        }
    )
```

### Paso 3: Migración BD (agregar tabla users)

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    email TEXT UNIQUE,
    role TEXT DEFAULT 'user',  -- 'admin', 'operator', 'viewer'
    active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    login_count INTEGER DEFAULT 0
);

CREATE TABLE audit_log (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    action TEXT,  -- 'LOGIN', 'LOGOUT', 'CREATE_ITEM', 'DELETE_ITEM'
    resource TEXT,  -- 'items', 'ingresos', 'consumos'
    resource_id TEXT,
    status TEXT,  -- 'SUCCESS', 'FAILURE'
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE token_blacklist (
    id INTEGER PRIMARY KEY,
    token_jti TEXT UNIQUE,
    revoked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Paso 4: Crear endpoint /api/login

```python
@app.route('/api/login', methods=['POST'])
def api_login():
    """
    Inicia sesión y retorna JWT token
    
    Body JSON:
    {
        "username": string (requerido),
        "password": string (requerido)
    }
    
    Respuesta exitosa (200):
    {
        "access_token": string,
        "refresh_token": string,
        "user": {
            "id": number,
            "username": string,
            "role": string
        }
    }
    
    Errores:
    - 401: Credenciales inválidas
    - 400: Request inválido
    """
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '')
    
    if not username or not password:
        return jsonify({'error': 'Username y password requeridos'}), 400
    
    # Buscar usuario en BD
    c = get_db()
    user = c.execute(
        'SELECT id, username, password_hash, role FROM users WHERE username=?',
        [username]
    ).fetchone()
    c.close()
    
    if not user or not verify_password(password, user[2]):
        log_security_event('LOGIN_FAILED', username, 'FAILURE')
        return jsonify({'error': 'Username o password inválidos'}), 401
    
    # Generar tokens
    access_token = create_jwt_token(user[0], user[1], user[3])
    
    # Actualizar BD
    c = get_db()
    c.execute(
        'UPDATE users SET last_login=?, login_count=login_count+1 WHERE id=?',
        [datetime.utcnow().isoformat(), user[0]]
    )
    c.commit()
    c.close()
    
    log_security_event('LOGIN_SUCCESS', username, 'SUCCESS')
    
    return jsonify({
        'access_token': access_token,
        'user': {
            'id': user[0],
            'username': user[1],
            'role': user[3]
        }
    }), 200
```

### Paso 5: Proteger endpoints

```python
from flask_jwt_extended import get_jwt_identity, get_jwt

@app.route('/api/items', methods=['POST'])
@jwt_required()
def api_create_item():
    """
    Crear item (PROTEGIDO - requiere autenticación)
    
    Headers requeridos:
    Authorization: Bearer <access_token>
    """
    current_user_id = get_jwt_identity()
    claims = get_jwt()
    
    # Verificar rol (ejemplo)
    if claims.get('role') not in ['admin', 'operator']:
        return jsonify({'error': 'Permiso denegado'}), 403
    
    # ... resto del código
```

### Paso 6: Tests de autenticación

```python
def test_login_success(client):
    """Test login con credenciales válidas"""
    payload = {
        'username': 'admin',
        'password': 'admin123'
    }
    response = client.post('/api/login', json=payload)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'access_token' in data

def test_login_invalid_credentials(client):
    """Test login con credenciales inválidas"""
    payload = {
        'username': 'noexiste',
        'password': 'wrong'
    }
    response = client.post('/api/login', json=payload)
    assert response.status_code == 401

def test_protected_endpoint_without_token(client):
    """Test acceso a endpoint protegido sin token"""
    response = client.post('/api/items', json={})
    assert response.status_code == 401

def test_protected_endpoint_with_token(client):
    """Test acceso a endpoint protegido con token válido"""
    # Login
    login_resp = client.post('/api/login', json={
        'username': 'admin',
        'password': 'admin123'
    })
    token = json.loads(login_resp.data)['access_token']
    
    # Usar token
    headers = {'Authorization': f'Bearer {token}'}
    response = client.post('/api/items',
                          json={'sku': 'TEST', 'nombre': 'Test'},
                          headers=headers)
    assert response.status_code in [200, 201]
```

---

## 📊 ARCHITECTURE

```
FLUJO DE AUTENTICACIÓN:

┌─────────────┐
│  Frontend   │
└──────┬──────┘
       │
       │ 1. POST /api/login
       │    (username, password)
       │
       ▼
┌──────────────┐         ┌─────────────┐
│  servidor.py │◄────────┤ auth.py     │
│ (app.py)     │         │ • hash_pwd  │
└──────┬───────┘         │ • create_jwt│
       │                 └─────────────┘
       │ 2. Retorna JWT
       │
       ▼
┌─────────────┐
│  Frontend   │ (guardar token en localStorage)
└──────┬──────┘
       │
       │ 3. Próximas requests: Authorization: Bearer <token>
       │
       ▼
┌──────────────────────────┐
│ @jwt_required()          │
│ • Verificar firma        │
│ • Verificar expiración   │
│ • Extraer user_id        │
└──────────┬───────────────┘
           │
           ▼
    ┌──────────────┐
    │ Endpoint     │
    │ (protegido)  │
    └──────────────┘
```

---

## 🔐 SECURITY BEST PRACTICES

1. **Token Storage (Frontend)**
   ```javascript
   // ✅ CORRECTO: localStorage o sessionStorage
   localStorage.setItem('token', jwtToken);
   
   // ❌ INCORRECTO: Variable global (vulnerable a XSS)
   window.token = jwtToken;
   ```

2. **Token Refresh**
   ```python
   # Generar cortos lived tokens (15 min)
   # + long lived refresh tokens (30 días)
   # Rotar refresh necesita nuevo login
   ```

3. **HTTPS Obligatorio**
   ```
   ❌ NUNCA enviar tokens por HTTP
   ✅ SIEMPRE usar HTTPS en producción
   ```

4. **Rate Limiting en Login**
   ```python
   # Limitar intentos fallidos a 5 por IP
   # Lockout de 15 minutos después
   # Logging de todos los intentos
   ```

5. **Audit Log Completo**
   ```
   Registrar:
   - Cada login (éxito/fallo)
   - Cada acción de usuario
   - Cambios de datos críticos
   - Accesos denegados
   ```

---

## 📅 TIMELINE SUGERIDO

### Semana 3 (5-6 horas)
- **Lunes:** Crear auth.py + tabla users (2h)
- **Martes:** Endpoint login + tests (2h)
- **Miércoles:** Proteger 5 endpoints (1-2h)
- **Jueves-Viernes:** Tests + debugging

### Semana 4 (4-5 horas)
- **Lunes:** Refresh tokens (1-2h)
- **Martes:** Token blacklist (1h)
- **Miércoles:** Rate limiting (1h)
- **Jueves:** RBAC básico (roles) (1h)
- **Viernes:** Testing final + docs

---

## ✅ DEFINITION OF DONE (PHASE 1)

- [ ] auth.py creado y funcional
- [ ] Tabla users en BD
- [ ] Tabla audit_log en BD
- [ ] POST /api/login funciona
- [ ] POST /api/logout funciona
- [ ] 5 endpoints protegidos
- [ ] Refresh tokens implementado
- [ ] Tests de autenticación completos (>10 tests)
- [ ] Audit log loguea todos los eventos
- [ ] Documentación de API auth updated
- [ ] Servidor sigue 100% operacional
- [ ] Cero regresiones en endpoints existentes

---

## 🚀 SIGUIENTES FASES (Después de PHASE 1)

### PHASE 2: RBAC (Role-Based Access Control)
```
Roles:
- ADMIN: Acceso total
- OPERATOR: CRUD items, ingresos, consumos
- VIEWER: Solo lectura
- AUDITOR: Audits logs

Implementación:
- Tabla roles_permissions
- Decorador @roles_required('admin')
- Validación en cada endpoint
```

### PHASE 3: PostgreSQL + Docker
```
- Migración a PostgreSQL
- Docker + docker-compose
- CI/CD en GitHub Actions
- Deployment a servidor
```

---

## 📞 REFERENCIA RÁPIDA

### JWT Tokens
```python
# Crear
access_token = create_access_token(identity=user_id)

# Verificar en endpoint
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    claims = get_jwt()

# En frontend
headers = {'Authorization': f'Bearer {token}'}
```

### Bcrypt Passwords
```python
# Hash
hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Verify
if bcrypt.checkpw(password.encode(), hash):
    # ✅ Válido
```

### Audit Logging
```python
c = get_db()
c.execute(
    'INSERT INTO audit_log (user_id, action, status) VALUES (?, ?, ?)',
    [user_id, 'CREATE_ITEM', 'SUCCESS']
)
c.commit()
```

---

## 🎯 RECURSOS RECOMENDADOS

- Flask-JWT-Extended docs: https://flask-jwt-extended.readthedocs.io/
- JWT.io: https://jwt.io/ (prueba tokens)
- OWASP Authentication Cheat Sheet
- Bcrypt: https://github.com/pyca/bcrypt

---

**Status:** Listos para PHASE 1 ✅
**Start Date:** Semana 3
**Estimated Duration:** 8-10 horas (2 semanas)
**Next Milestone:** Autenticación completa + RBAC

¡Adelante! 🚀
