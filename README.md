<p align="center">
  <img src="app/static/images/LensonsKitchen.png" alt="Lensons Kitchen Logo" />
</p>


A web based restaurant platform designed to strengthen relationship between a restaurant and it’s customers by enhancing interaction personalization and loyalty. 
Customers are able to book reservations, place orders,, access menus with a QR code system and earn legacy points based on various interactions.
It also features a dynamic admin dash for creation, deletion, update of reservations, orders, and menus


### 📦 Tech Stack

| Category          | Technologies / Tools                                                                                                                                         |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 💻 Languages      | Python, HTML5/CSS3, JavaScript                                                                                                                               |
| 🧰 Frameworks     | Flask, Bootstrap                                                                                                                                             |
| 🧰 Tools & Libraries | MongoEngine (ODM for MongoDB), bcrypt (password hashing), PyJWT (JWT authentication),  Jinja2 (HTML templating)                                           |
| 🛢️ Database       | MongoDB (NoSQL document store)                                                                                                                               |



### ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/lensonlovescode/LensonsKitchen.git
cd LensonsKitchen

# Create and activate virtual environment
python3 -m venv LKitchen
source LKitchen/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
touch .env
```

Add the following inside `.env`:

```env![LensonsKitchen](https://github.com/user-attachments/assets/4b3d71b0-8a78-4607-ba98-309589335d27)

SK="your_secret_key_here"
```

> The `SK` is the secret key for password hashing, JWT token signing, and other security-related operations.

## 🚀 Starting the Application

```bash
# Start MongoDB (Debian/Ubuntu)
sudo systemctl start mongod

# If MongoDB is not installed:
sudo apt update
sudo apt install -y mongodb
sudo systemctl enable mongod
sudo systemctl start mongod

# Create unique index on email field to prevent duplicate accounts
# Start mongosh
mongosh

# Inside MongoDB shell:
use LensonsKitchen
db.user.createIndex({ "email": 1 }, { unique: true })

# Start Backend API (Port 5001)
python -m api.v1.api

# Start Frontend App (Port 5000)
python -m app.app

```
✅ Usage:
```
Frontend App: http://localhost:5000
Backend API: http://localhost:5001
```

> [!IMPORTANT]  
> Ensure MongoDB is always running in the background while using the app.
