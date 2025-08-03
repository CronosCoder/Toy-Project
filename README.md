
# 🛍️ Toy Project
### Payment Gateway Integration & Shop API

<div align="center">

[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-API-blue?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Stripe](https://img.shields.io/badge/Stripe-Integration-blue?style=for-the-badge&logo=stripe)](https://stripe.com/)

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#api-endpoints">API</a> •
  <a href="#testing">Testing</a>
</p>

</div>

<hr>

## 🚀 Overview
A smart Django project featuring a custom user model, payment gateway integration, and modular APIs for shop, orders, and transactions using Django REST Framework. Designed for learning, rapid prototyping, and real-world e-commerce scenarios.

---

## ⭐ Features
<table>
  <tr>
    <td>🔐 <b>Authentication</b></td>
    <td>
      • Custom User Model with email login<br>
      • JWT Authentication<br>
      • Role-based access control
    </td>
  </tr>
  <tr>
    <td>🛒 <b>Shop Features</b></td>
    <td>
      • Product & Category Management<br>
      • Order Processing<br>
      • Stock Management
    </td>
  </tr>
  <tr>
    <td>💳 <b>Payment</b></td>
    <td>
      • Stripe Integration<br>
      • Transaction Management<br>
      • Payment Status Tracking
    </td>
  </tr>
  <tr>
    <td>🛠️ <b>Technical</b></td>
    <td>
      • Clean Architecture<br>
      • Service Layer Pattern<br>
      • Comprehensive Test Coverage
    </td>
  </tr>
</table>

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

## 📁 Project Structure
```plaintext
Toy-Project/
├── 📁 core/           # User Management
│   ├── models.py      # Custom User Model
│   └── views.py       # Authentication Views
├── 📁 shop/           # Shop Features
│   ├── models.py      # Product, Order Models
│   ├── views/         # API Views
│   ├── services.py    # Business Logic
│   └── tests/         # Unit Tests
├── 📁 accounting/     # Payment Integration
│   ├── models.py      # Transaction Models
│   └── services.py    # Payment Processing
└── 📄 manage.py       # Django CLI
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
