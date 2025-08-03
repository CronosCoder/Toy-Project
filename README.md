
# Toy Project: Payment Gateway Integration & Shop API

![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-API-blue)
![Python](https://img.shields.io/badge/Python-3.12-blue)

## 🚀 Overview
A smart Django project featuring a custom user model, payment gateway integration, and modular APIs for shop, orders, and transactions using Django REST Framework. Designed for learning, rapid prototyping, and real-world e-commerce scenarios.

---

## 📦 Features
- **Custom User Model** (email as username)
- **Shop API**: Products, Categories, Stock, and more
- **Order API**: Place and view orders
- **Transaction API**: Payment gateway integration
- **Role-based Permissions**: Admin-only product creation, authenticated order/transaction
- **Service Layer**: Clean business logic separation
- **Unit Tests**: API endpoints covered
- **Modular Structure**: Easy to extend

---

## 🛠️ Tech Stack
- Python 3.12
- Django 5.x
- Django REST Framework
- Djoser & SimpleJWT (auth)
- SQLite (default, easy to swap)
- Stripe (payment integration)

---

## 🏁 Quickstart


<!-- Clone the repo (with copy button) -->
<div align="left" style="padding:5px;">
  <code>git clone https://github.com/CronosCoder/Toy-Project.git</code>
  <button onclick="navigator.clipboard.writeText('git clone https://github.com/CronosCoder/Toy-Project.git')" style="margin-left:10px;">Copy</button>
</div>

<div align="left" style="margin-top:8px; padding:5px;">
  <code>cd Toy-Project</code>
  <button onclick="navigator.clipboard.writeText('cd Toy-Project')" style="margin-left:10px;">Copy</button>
</div>


# Create and activate a virtual environment
# Linux/Mac:
python3.12 -m venv .venv

source .venv/bin/activate

# Windows (cmd):
python3.12 -m venv .venv

.venv\Scripts\activate

# Windows (PowerShell):
python3.12 -m venv .venv

.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (see .env.example)

# Run migrations
python3.12 manage.py migrate

# Run tests
python3.12 manage.py test shop

# Start the server
python3.12 manage.py runserver
```

---

## 🔑 Authentication & Permissions
- Custom user model (`core.User`) with email login
- Admin users can create products
- Authenticated users can place orders and create transactions
- Public can view products and categories

---

## 📚 API Endpoints
| Method | Endpoint                | Description                | Permissions      |
|--------|------------------------|----------------------------|------------------|
| GET    | `/api/v1/products/`    | List all products          | Public           |
| POST   | `/api/v1/products/`    | Create a new product       | Admin only       |
| GET    | `/api/v1/orders/`      | List user orders           | Authenticated    |
| POST   | `/api/v1/orders/`      | Place a new order          | Authenticated    |
| POST   | `/api/v1/transactions/`| Create a transaction       | Authenticated    |

---

## 🧩 Project Structure
```
Toy-Project/
├── core/           # Custom user model
├── shop/           # Product, Category, Order, API, tests
├── accounting/     # Payment logic & transactions
├── manage.py
├── requirements.txt
├── README.md
└── ...
```

---

## 📝 Testing
- All major API endpoints are covered by unit tests in `shop/tests/`
- Run with: `python3.12 manage.py test shop`

---

## 💡 Extending
- Add new models to `shop/models.py` or `accounting/models.py`
- Add new endpoints to `shop/views/` or `accounting/views.py`
- Add business logic to `shop/services.py` or `accounting/services.py`

---

## 👤 Author
- **Foysal (CronosCoder)**
- [GitHub](https://github.com/CronosCoder)

---

## 📄 License
MIT License

---

> Made with ❤️ using Django REST Framework
