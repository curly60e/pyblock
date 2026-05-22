# Roadmap: Astrolexis AI Backend for PyBLOCK

## Objetivo

Backend API que actúa como proxy inteligente entre PyBLOCK y los LLM providers (Anthropic, OpenAI). Acceso único: pago en sats via Lightning a través de Astrolexis.

---

## Estado Actual

### ✅ Fase 1: API Gateway MVP — COMPLETADO

**Desplegado en producción:** `https://api.astrolexis.space/v1`

**Stack:** Bun + Hono, SQLite, systemd service

**Endpoints operativos:**

```
POST /v1/chat            - Proxy a LLM (streaming SSE) con system prompt Bitcoin
POST /v1/auth/verify     - Verificar token y balance
POST /v1/topup           - Crear invoice Lightning para recargar
GET  /v1/topup/check/:h  - Verificar si invoice fue pagado
GET  /v1/usage           - Consultar uso del usuario
GET  /v1/models          - Modelos disponibles con pricing en sats
GET  /v1/health          - Health check
```

**Infraestructura:**
- Cloudflare Tunnel (HTTPS, sin origin cert necesario)
- systemd service (`astrolexis-api.service`) con auto-restart
- SQLite WAL mode para concurrencia

### ✅ Fase 2: Pagos Lightning — COMPLETADO

**Implementación:** AlbyHub via NWC (Nostr Wallet Connect)

- Invoice creation via `make_invoice` NWC
- Payment listener automático via `subscribeNotifications`
- Polling fallback via `/v1/topup/check/:payment_hash`
- Modelo prepago con balance (min 100, max 100,000 sats)
- Lightning node: `03cd787d7bfb97454aa1cd12a51a0c9d89136077187bcbd0b6705ab629e5c5264f`
- Lightning address: `pyblock@getalby.com`

**Flujo de recarga:**
```
1. PyBLOCK -> POST /v1/topup {amount: 1000}
2. Gateway -> crea invoice via AlbyHub NWC
3. Gateway <- devuelve bolt11 invoice
4. PyBLOCK -> muestra QR + bolt11 en terminal
5. Usuario paga desde cualquier wallet
6. AlbyHub -> NWC notification -> balance acreditado automáticamente
7. PyBLOCK <- GET /v1/topup/check/{hash} -> confirma en UI
```

### ✅ Fase 3: System Prompt Bitcoin — COMPLETADO

**System prompt inyectado automáticamente:**
```
You are PyBLOCK AI, a Bitcoin and Lightning Network assistant
running inside PyBLOCK terminal dashboard.
...
Current node context:
{node_context}
```

**Context injection:** PyBLOCK envía `node_context` en cada request, el gateway lo formatea e inyecta en el system prompt antes del proxy.

### Pricing en sats (operativo)

```
                    Costo por query típica (~500 in, ~1000 out tokens)
Claude Sonnet 4.6:  ~4 sats
Claude Haiku 4.5:   ~2 sats
Claude Opus 4.6:    ~18 sats
GPT-4o:             ~3 sats
GPT-4o Mini:        ~1 sat
```

---

## Pendiente

### 🔲 Fase 4: Seguridad y Rate Limiting (Semana 1-2)

#### 4.1 Rate limiting

```
Por token:       30 queries/hora, 500/dia
Burst:           Max 5 concurrent requests
Token size:      Max 4096 tokens output por query
Sin balance:     Rechazar con 402 + balance_sats + estimated_cost
```

#### 4.2 Seguridad

- HTTPS obligatorio (✅ ya via Cloudflare Tunnel)
- No almacenar contenido de queries (privacy) — ✅ ya implementado
- Log solo metadata: timestamp, model, token counts, user_id — ✅ ya implementado
- API keys de Anthropic/OpenAI en env vars del server — ✅ ya implementado
- Rate limit por IP + por token
- Hard limit de gasto diario por usuario

### 🔲 Fase 5: Dashboard Admin (Semana 2-3)

#### 5.1 Métricas

- Queries por dia/hora
- Revenue en sats (depósitos - costos API)
- Modelos más usados
- Top usuarios
- Costo vs revenue por modelo
- Error rate

#### 5.2 Panel

Web dashboard o Grafana:
- Total revenue
- Active users (7d/30d)
- API cost breakdown
- Margin tracking

---

## Integración con PyBLOCK (lado cliente)

### Base URL

```
https://api.astrolexis.space/v1
```

### Documentación completa de integración

Ver: [`astrolexis-api/docs/PYBLOCK_INTEGRATION.md`](../../astrolexis-api/docs/PYBLOCK_INTEGRATION.md)

Incluye:
- Todos los endpoints con request/response de ejemplo
- Códigos de error y cómo manejarlos
- Implementación completa en Python (`client.py`, `context.py`, `ui.py`)
- Flujo del usuario paso a paso

### Módulo `pybitblock/ai/`

```
ai/
  __init__.py       - chat(prompt, context) entry point
  client.py         - Astrolexis API client (auth, streaming, topup)
  context.py        - Gather node data for injection
  ui.py             - Terminal chat interface
```

### Configuración del usuario

Una sola variable:
```ini
ASTROLEXIS_TOKEN=astrolexis_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Menú en PyBLOCK

```
Main Menu > AI Assistant

  Powered by Astrolexis KCode
  Balance: 4,521 sats

  Type your question or:
  T. Top Up Balance
  U. Usage History
  Q. Quit

  > "what's happening with my mempool?"
```

---

## Timeline actualizado

```
Semana 1-2:   API Gateway MVP                    ✅ COMPLETADO
Semana 2-3:   Lightning payments (AlbyHub NWC)   ✅ COMPLETADO
Semana 3-4:   System prompt + context injection   ✅ COMPLETADO
Semana 4-5:   Security, rate limiting             🔲 PENDIENTE
Semana 5-6:   Admin dashboard + metrics           🔲 PENDIENTE
Semana 6-7:   PyBLOCK client module (ai/)         🔲 EQUIPO PYBLOCK
Semana 7-8:   Testing, docs, beta launch          🔲 CONJUNTO
```

---

## Branding

```
En PyBLOCK:     "AI powered by Astrolexis KCode"
En Astrolexis:  "Available on PyBLOCK - Bitcoin Terminal Dashboard"
Licencia:       PyBLOCK (GPL) usa Astrolexis API como servicio externo
                No hay conflicto de licencias (API boundary)
```

---

## Notas para el equipo de desarrollo

1. **No hace falta GPU** — todo se proxea a Anthropic/OpenAI cloud
2. **No hay modo gratuito** — toda query AI pasa por Astrolexis y se cobra en sats
3. **El valor está en el system prompt + contexto Bitcoin** — eso es el IP de Astrolexis
4. **Lightning payments son el diferenciador** — sin cuentas, sin email, sin KYC. Puro Bitcoin
5. **Empezar con Sonnet** — más barato, suficiente para queries de nodo. Opus como opción premium
6. **El proxy es stateless** — fácil de escalar horizontalmente si crece
7. **Privacy first** — no se guarda contenido de queries, solo metadata de billing
8. **Servidor propio** — sin costos de hosting, margen neto desde la primera query
9. **AlbyHub NWC** — pagos Lightning automáticos, sin polling necesario (con fallback)
10. **Ya está en producción** — `https://api.astrolexis.space/v1/health` para verificar
