# Aurelia

Aurelia is a dream-and-poetry platform where users log dreams, tag symbols, and write poems inspired by those dreams.

## Tech
- Python
- PyMySQL
- Requests (for console frontend)
- Uvicorn
- MySQL
- Layered architecture (models, data access, app)

## Setup
1. Create DB:
   - Run `sql/01_create_tables.sql`
   - Run `sql/02_insert_test_data.sql`
2. Install deps:
   - `pip install -r backend/requirements.txt`
3. Run:
   - `python backend/test_harness.py`

## Architecture
- models/ = domain objects
- data/ = repository / data access layer
- app_api.py = API client
- output.txt = test_frontend.py console output

# 🔁 Features Implemented

## ✅ Full CRUD Operations

For:

* Users
* Dreams
* Symbols
* Poems
* DreamSymbols

Each entity supports:

* Create
* Read (Single + All)
* Update
* Delete

---

## 🖥 Console-Based Front End

`console_frontend.py` acts as an interactive console application that:

* Displays menus for each entity
* Allows users to navigate between:

  * User menu
  * Dreams menu
  * Symbols menu
  * Poems menu
  * DreamSymbols menu
* Performs CRUD actions
* Displays updated data after each action

---

## 🛡 Input Validation Added

The console front end includes:

* Menu input validation
* Integer ID validation
* Empty field validation
* Safe handling of invalid selections
* Graceful handling of server errors

---

# 💻 Running Locally

## 1️⃣ Create Virtual Environment

```
python -m venv .venv
```

Activate:

Windows:

```
.venv\Scripts\activate
```

Mac/Linux:

```
source .venv/bin/activate
```

---

## 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 3️⃣ Configure MySQL

Ensure MySQL is running locally.

Update your connection string if using local MySQL:

```
mysql+pymysql://username:password@localhost/databasename
```

Or set environment variable:

```
DATABASE_URL=mysql+pymysql://username:password@localhost/databasename
```

---

## 4️⃣ Run the API

```
python app_api.py
```

Default:

```
http://127.0.0.1:5000
```

---

## 5️⃣ Run Console Front End

In a separate terminal:

```
python console_frontend.py
```

---

# 📂 Project Structure

```
/aurelia
│
├── app_api.py
├── test_frontend.py
├── models.py
├── requirements.txt
└── README.md
```

---

# 🧪 Testing

Testing is performed using:

* Interactive console-based frontend
* Manual endpoint verification
* Read-all verification before and after CRUD operations

All entities and relationships were verified through:

* Creation
* Retrieval
* Update
* Deletion
* Relationship integrity

---

# 🎯 Learning Outcomes

This project demonstrates:

* REST API design
* Relational database modeling
* Error handling and debugging
* Environment variable configuration
* Backend system architecture principles

---

# 🔮 Future Improvements

* Web-based frontend
* Authentication (JWT)
* Role-based access control
* Pagination for large datasets
* Automated unit tests
* Full cloud deployment with managed MySQL
