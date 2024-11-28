# Ecommerce_CAT2

A Django-based e-commerce application with models for **Customers** and **Orders**. This project demonstrates a basic one-to-many relationship where a customer can place multiple orders.

## Prerequisites

Ensure you have the following installed on your system:

- Python (3.12.6)
- pip 
- Django
- Virtual environment

## Setting Up the Environment

Follow these steps to set up the environment and run the project:

### 1. Create a GitHub Repository

- Go to [GitHub](https://github.com/) and create a new repository.
- Copy the repository URL.

### 2. Clone the Repository

```bash
git clone https://github.com/IreneWanjiruKariuki/Ecommerce_CAT2.git
cd Ecommerce_CAT2
```

### 3. Create and Activate a Virtual Environment

Create a virtual environment to isolate project dependencies:

```bash
py -m venv venv
```
Activate the virtual environment:

- On Windows:
  ```bash
  .\venv\Scripts\Activate.ps1
  ```

### 4. Run Database Migrations

Apply the database migrations to set up the `Customers` and `Orders` models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

## Models

### Customers
- Fields:
  - `fname`: First name of the customer
  - `lname`: Customer last name
  - `phone`: Phone number of the customer
  - `email`: Unique email of customer
  - `address`: Opttional address of the customer

### Orders
- Fields:
  - `quantity_ordered`: The number of goods ordered by the customer
  - `order_date`:Automatically set date and time of when the order is placed
  - `total_amount`: Total monetary value of the order
  - `customer`: Foreign key linking to the `Customer` model (one-to-many relationship)

## Uploading the Project to GitHub

### 1. Initialize a Git Repository

```bash
git add .
git commit -m "First commit"
git push
```
