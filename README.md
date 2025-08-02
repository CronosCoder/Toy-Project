# Toy Project: Payment Gateway Integration & Shop API

![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-API-blue)
![Python](https://img.shields.io/badge/Python-3.12-blue)

## 🚀 Overview
A smart Django project featuring a custom user model, payment gateway integration, and a modular shop API using Django REST Framework. Designed for learning, rapid prototyping, and real-world e-commerce scenarios.

---

## 📦 Features
- **Custom User Model** (email as username)
- **Shop API**: Products, Categories, Stock, and more
- **Role-based Permissions**: Admin-only product creation
- **Service Layer**: Clean business logic separation
- **Unit Tests**: API endpoints covered
- **Modular Structure**: Easy to extend

---

## 🛠️ Tech Stack
- Python 3.12
- Django 5.x
- Django REST Framework
- SQLite (default, easy to swap)

---

## 🏁 Quickstart

```bash
# Clone the repo
$ git clone <your-repo-url>
$ cd Toy-Project

# Create and activate a virtual environment
$ python3.12 -m venv .venv
$ source .venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Run migrations
$ python3.12 manage.py migrate

# Run tests
$ python3.12 manage.py test shop

# Start the server
$ python3.12 manage.py runserver
```

---

## 🔑 Authentication
- Custom user model (`core.User`) with email login
- Admin users can create products
- Public can view products

---

## 📚 API Endpoints
| Method | Endpoint                | Description                | Permissions      |
|--------|------------------------|----------------------------|------------------|
| GET    | `/api/v1/products/`    | List all products          | Public           |
| POST   | `/api/v1/products/`    | Create a new product       | Admin only       |

---

## 🧩 Project Structure
```
Toy-Project/
├── core/           # Custom user model
├── shop/           # Product, Category, API, tests
├── accounting/     # (Optional) Payment logic
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
- Add new models to `shop/models.py`
- Add new endpoints to `shop/views/`
- Add business logic to `shop/services.py`

---

## 👤 Author
- **Foysal (CronosCoder)**
- [GitHub](https://github.com/CronosCoder)

---

## 📄 License
MIT License

---

> Made with ❤️ using Django REST Framework
