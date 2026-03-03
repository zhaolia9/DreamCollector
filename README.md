# 🌙 Aurelia – Dream Journal Web Application

Aurelia is a full-stack Dream Journal application built with a layered architecture using FastAPI, MySQL, and a custom web client interface.

This project demonstrates:

* Service Layer architecture
* Full CRUD operations for multiple entities
* RESTful API design
* Console-based testing harness
* Web-based client layer
* Local MySQL database integration
* Themed UI implementation

---
# 🏗️ Project Architecture

The application follows a layered design pattern:

```
Client Layer (HTML/CSS/JS)
        ↓
FastAPI Controller Layer
        ↓
Service Layer
        ↓
Manager / Data Access Layer
        ↓
MySQL Database
```

### Layers Explained

### 1️⃣ Client Layer

* Built using HTML, CSS, and JavaScript
* Communicates with backend via REST API
* Fully styled Dream Journal aesthetic
* Calls ALL “GET” endpoints for ALL tables (per project requirements)

### 2️⃣ Controller Layer

* Implemented using FastAPI
* Defines REST endpoints for all entities
* Handles request/response serialization

### 3️⃣ Service Layer

* Contains business logic
* Delegates database operations to manager classes

### 4️⃣ Data Access Layer

* Handles direct interaction with MySQL
* Executes SQL queries
* Returns structured data

### 5️⃣ Database

* MySQL (hosted locally)
* Multiple related tables with foreign key relationships

---

# 🗄️ Database Schema

The system includes the following tables:

### Users

* id
* name
* email

### Dreams

* id
* user_id (FK → Users)
* title
* description
* date
* mood
* vividness

### Symbols

* id
* name
* description

### Poems

* id
* author_id (FK → Users)
* dream_id (FK → Dreams)
* content

### DreamSymbols (Link Table)

* dream_id (FK → Dreams)
* symbol_id (FK → Symbols)

---

# 🔌 API Endpoints

All endpoints are implemented with full CRUD functionality.

---

## USERS

```
POST    /users
GET     /users
GET     /users/{user_id}
PUT     /users/{user_id}
DELETE  /users/{user_id}
```

---

## DREAMS

```
POST    /dreams
GET     /dreams
GET     /dreams/{dream_id}
PUT     /dreams/{dream_id}
DELETE  /dreams/{dream_id}
```

---

## SYMBOLS

```
POST    /symbols
GET     /symbols
GET     /symbols/{symbol_id}
PUT     /symbols/{symbol_id}
DELETE  /symbols/{symbol_id}
```

---

## POEMS

```
POST    /poems
GET     /poems
GET     /poems/{poem_id}
PUT     /poems/{poem_id}
DELETE  /poems/{poem_id}
```

---

## DREAMSYMBOLS

```
POST    /dreamsymbols
GET     /dreamsymbols
GET     /dreamsymbols?dream_id=X
GET     /dreamsymbols/{link_id}
PUT     /dreamsymbols/{link_id}
DELETE  /dreamsymbols?dream_id=X&symbol_id=Y
```

---

# 🖥️ Console-Based Test Harness

A console front-end (`test_frontend.py`) was implemented for:

* Manual CRUD testing
* Menu-based navigation
* Input validation
* ReadAll before each action
* Entity-specific submenus (Users, Dreams, Symbols, Poems, DreamSymbols)

This allowed full service-layer verification before building the web client.

---

# 🌐 Web Client Layer

A fully functional web-based client was created using:

* HTML
* CSS
* JavaScript (Fetch API)

### Features

* Calls ALL “get” methods for ALL tables
* Performs full CRUD
* Section-based navigation
* Dynamic output display
* Themed UI (Dream Journal aesthetic)

---

# 🎨 UI Theme: Dream Journal Aesthetic

The client uses a custom `styles.css` with:

* Soft pastel gradient background
* Glassmorphism card styling
* Rounded UI elements
* Serif typography
* Navigation toggling between entities
* Always-visible response section
* Responsive layout

Sections include:

* Users
* Dreams
* Symbols
* Poems
* Dream Symbols
* Oracle Response (API output display)

---

# ⚙️ Running the Application Locally

## 1️⃣ Start MySQL

Ensure MySQL is running locally and the database is created.

---

## 2️⃣ Activate Virtual Environment

```
venv\Scripts\activate
```

---

## 3️⃣ Run FastAPI Backend

```
uvicorn aurelia.app_api:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## 4️⃣ Open Client

Open in browser:

```
http://127.0.0.1:8000/static/index.html
```

---

# 📦 Technologies Used

* Python
* FastAPI
* Uvicorn
* MySQL
* HTML
* CSS
* JavaScript (Fetch API)

---

# 🧪 Testing Performed

* Manual CRUD testing via console harness
* Endpoint validation via Swagger UI
* Client-to-backend integration testing
* MySQL connection validation
* Input validation for numeric fields
* Link-table relationship testing

---

# 🧠 Key Challenges Solved

* MySQL authentication issues
* JSON parsing errors
* Endpoint routing inconsistencies
* Linking dream-symbol relationships
* Static file hosting in FastAPI
* Section navigation state management
* Response container visibility fix

---

# 🚀 Hosting

Currently hosted locally using:

```
Uvicorn + FastAPI static file serving
```

No IIS or external hosting required for local deployment.

---

# 📸 Project Requirements Satisfied

✔ Client calls ALL GET endpoints
✔ Client hosted locally
✔ Full CRUD operations
✔ Layered architecture maintained
✔ Screenshots ready for submission

---

# 🌌 Future Enhancements

* Authentication layer
* User login system
* Rich dream visualization UI
* React-based frontend
* Deployment to cloud (Render, Railway, or Azure)
* Full UX redesign for portfolio use

---

# 👤 Author

Developed as part of a multi-phase service-layer and client-layer software architecture project.
