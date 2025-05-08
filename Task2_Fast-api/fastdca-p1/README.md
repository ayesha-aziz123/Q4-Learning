# 🚀 FastAPI Starter Project

A minimal FastAPI setup to kickstart your next Python web API project. This boilerplate is clean, async-ready, and easy to extend.

---

## ✨ Features

- **⚡ Fast & Async** – Built on `async`/`await` for maximum speed.
- **🧠 Type Safety** – Python type hints enable auto-validation and editor support.
- **📄 Interactive API Docs** – Swagger UI and ReDoc included by default.
- **🛠️ Dev Friendly** – Clear syntax, helpful errors, and easy testing.

---

## 📦 Project Setup

### 1. ✅ Prerequisites

Make sure Python 3.8+ is installed:

```bash
python --version
```



### 2. 📁 Create Project Folder

```bash
mkdir fastapi-starter
cd fastapi-starter
```

### 3. 🧪 Create & Activate Virtual Environment (using uv)

```bash
uv venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
```


### 4. 📥 Install Dependencies
```bash
uv pip install "fastapi[standard]"
 ```

Installs:

- `fastapi`: The main framework
- `uvicorn`: Runs the app
- `httpx`: For testing APIs


### 5. 🧪 (Optional) Install Testing Tools

```bash
uv pip install --dev pytest pytest-asyncio
```

