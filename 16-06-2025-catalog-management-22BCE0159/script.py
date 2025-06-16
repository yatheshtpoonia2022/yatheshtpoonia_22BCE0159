import requests
import time

# Replace this with your actual API endpoint
API_URL = "http://localhost:5000/api/product"

products = [
  {
    "image": "https://m.media-amazon.com/images/I/71AvQd3VzqL._AC_UL800_.jpg",
    "title": "OnePlus Nord CE 2 Lite 5G (Blue Tide, 6GB RAM, 128GB Storage)",
    "price": 18999,
    "description": "High performance smartphone with 5G connectivity and long battery life.",
    "quantity": 50,
    "status": "Private",
    "createdAt": "2025-06-16T12:01:38Z",
    "updatedAt": "2025-06-16T12:01:38Z",
    "_id": "55c7cb97ca364d36a4e3989f",
    "__v": 0,
    "id": "1bc246c56c9740cd8f28cd11"
  },
  {
    "image": "https://m.media-amazon.com/images/I/51UhwaQXCpL._AC_UL800_.jpg",
    "title": "OnePlus Bullets Z2 Bluetooth Wireless in Ear Earphones with Mic",
    "price": 1999,
    "description": "Premium wireless earphones with bombastic bass and fast charging.",
    "quantity": 100,
    "status": "Public",
    "createdAt": "2025-06-16T12:02:45Z",
    "updatedAt": "2025-06-16T12:02:45Z",
    "_id": "66d8dc98db475e47b5e4990a",
    "__v": 0,
    "id": "2cd357d67d0851de9g39de22"
  },
  {
    "image": "https://m.media-amazon.com/images/I/81I3w4J6yjL._AC_UL800_.jpg",
    "title": "Samsung Galaxy M33 5G (Mystique Green, 6GB, 128GB Storage)",
    "price": 15999,
    "description": "Powerful 5G smartphone with 6000mAh battery and RAM Plus technology.",
    "quantity": 30,
    "status": "Private",
    "createdAt": "2025-06-16T12:03:52Z",
    "updatedAt": "2025-06-16T12:03:52Z",
    "_id": "77e9ed09ec586f58c6f5aa1b",
    "__v": 0,
    "id": "3de468e78e1962efah4aef33"
  },
  {
    "image": "https://m.media-amazon.com/images/I/61vtLhO6fDL._AC_UL800_.jpg",
    "title": "Apple 20W USB-C Power Adapter (for iPhone, iPad & AirPods)",
    "price": 1589,
    "description": "Fast charging adapter compatible with various Apple devices.",
    "quantity": 200,
    "status": "Public",
    "createdAt": "2025-06-16T12:04:59Z",
    "updatedAt": "2025-06-16T12:04:59Z",
    "_id": "88fafe1afd697069d7g6bb2c",
    "__v": 0,
    "id": "4ef579f89f2a73f0bi5bf44"
  },
  {
    "image": "https://m.media-amazon.com/images/I/61S9aVnRZDL._AC_UL800_.jpg",
    "title": "Fire-Boltt Ninja Call Pro Plus 1.83\" Smart Watch",
    "price": 1799,
    "description": "Feature-rich smartwatch with Bluetooth calling and AI voice assistance.",
    "quantity": 75,
    "status": "Public",
    "createdAt": "2025-06-16T12:06:06Z",
    "updatedAt": "2025-06-16T12:06:06Z",
    "_id": "990b0f2b0e7a17a0e8h7cc3d",
    "__v": 0,
    "id": "5fg68a09ag3b84g1cj6cg55"
  },
  {
    "image": "https://m.media-amazon.com/images/I/81lnKynSaqL._AC_UL800_.jpg",
    "title": "Samsung Galaxy M33 5G (Emerald Brown, 6GB, 128GB Storage)",
    "price": 15999,
    "description": "Elegant smartphone with powerful performance and large storage.",
    "quantity": 40,
    "status": "Private",
    "createdAt": "2025-06-16T12:07:13Z",
    "updatedAt": "2025-06-16T12:07:13Z",
    "_id": "aa1c203c1f8b28b1f9i8dd4e",
    "__v": 0,
    "id": "6gh79b1bh4c95h2dk7dh66"
  },
  {
    "image": "https://m.media-amazon.com/images/I/81UT07JsBqL._AC_UL800_.jpg",
    "title": "Redmi A1 (Light Blue, 2GB RAM, 32GB Storage)",
    "price": 5899,
    "description": "Budget-friendly smartphone with AI dual camera and leather texture design.",
    "quantity": 120,
    "status": "Public",
    "createdAt": "2025-06-16T12:08:20Z",
    "updatedAt": "2025-06-16T12:08:20Z",
    "_id": "bb2d314d209c39c2g0j9ee5f",
    "__v": 0,
    "id": "7hi8ac2ci5da6i3el8ei77"
  },
  {
    "image": "https://m.media-amazon.com/images/I/613SAOPmLeL._AC_UL800_.jpg",
    "title": "OnePlus 11R 5G (Galactic Silver, 16GB RAM, 256GB Storage)",
    "price": 44999,
    "description": "Premium 5G smartphone with high-end specifications and performance.",
    "quantity": 25,
    "status": "Private",
    "createdAt": "2025-06-16T12:09:27Z",
    "updatedAt": "2025-06-16T12:09:27Z",
    "_id": "cc3e425e31ad4ad3h1k0ff6g",
    "__v": 0,
    "id": "8ij9bd3dj6eb7j4fm9fj88"
  },
  {
    "image": "https://m.media-amazon.com/images/I/514NPRZ1AQL._AC_UL800_.jpg",
    "title": "OnePlus Nord Buds True Wireless in Ear Earbuds with Mic",
    "price": 2799,
    "description": "Wireless earbuds with titanium drivers and long playback time.",
    "quantity": 150,
    "status": "Public",
    "createdAt": "2025-06-16T12:10:34Z",
    "updatedAt": "2025-06-16T12:10:34Z",
    "_id": "dd4f536f42be5be4i2l1gg7h",
    "__v": 0,
    "id": "9jkace4ek7fc8k5gn0gk99"
  },
  {
    "image": "https://m.media-amazon.com/images/I/51aBTOiXRlL._AC_UL800_.jpg",
    "title": "boAt Rockerz 255 Pro+ in-Ear Bluetooth Neckband",
    "price": 1499,
    "description": "Comfortable neckband earphones with 40 hours playback time.",
    "quantity": 80,
    "status": "Public",
    "createdAt": "2025-06-16T12:11:41Z",
    "updatedAt": "2025-06-16T12:11:41Z",
    "_id": "ee5f647053cf6cf5j3m2hh8i",
    "__v": 0,
    "id": "0klbdf5fl8gd9l6ho1hl00"
  },
  {
    "image": "https://m.media-amazon.com/images/I/61jQim6YPnL._AC_UL800_.jpg",
    "title": "Hammer Ace 3.0 Bluetooth Calling Smart Watch",
    "price": 1499,
    "description": "Smartwatch with large display and strong metallic build quality.",
    "quantity": 60,
    "status": "Private",
    "createdAt": "2025-06-16T12:12:48Z",
    "updatedAt": "2025-06-16T12:12:48Z",
    "_id": "ff6g758164d7dg6k4n3ii9j",
    "__v": 0,
    "id": "1lmceg6gm9he0m7ip2im11"
  },
  {
    "image": "https://m.media-amazon.com/images/I/71lVwl3q-kL._AC_UL800_.jpg",
    "title": "MI Power Bank 3i 20000mAh Lithium Polymer 18W Fast Power Delivery Charging",
    "price": 2049,
    "description": "High capacity power bank with fast charging capability.",
    "quantity": 90,
    "status": "Public",
    "createdAt": "2025-06-16T12:13:55Z",
    "updatedAt": "2025-06-16T12:13:55Z",
    "_id": "00g7h869275e8eh7l5o4jj0k",
    "__v": 0,
    "id": "2mndfh7hn0if1n8jq3jn22"
  },
  {
    "image": "https://m.media-amazon.com/images/I/61DjwgS4cbL._AC_UL800_.jpg",
    "title": "SanDisk Cruzer Blade 32GB USB Flash Drive",
    "price": 278,
    "description": "Compact and reliable USB flash drive with 32GB storage.",
    "quantity": 300,
    "status": "Public",
    "createdAt": "2025-06-16T12:15:02Z",
    "updatedAt": "2025-06-16T12:15:02Z",
    "_id": "11h8i97a386f9fi8m6p5kk1l",
    "__v": 0,
    "id": "3noegi8io1jg2o9kr4ko33"
  },
  {
    "image": "https://m.media-amazon.com/images/I/7180ZAZmERL._AC_UL800_.jpg",
    "title": "SanDisk Ultra® microSDXC™ UHS-I Card, 64GB",
    "price": 488,
    "description": "High-speed microSD card with 10-year warranty for smartphones.",
    "quantity": 250,
    "status": "Public",
    "createdAt": "2025-06-16T12:16:09Z",
    "updatedAt": "2025-06-16T12:16:09Z",
    "_id": "22i9ja8b497g0gj9n7q6ll2m",
    "__v": 0,
    "id": "4opfhj9pj2kh3p0ls5lp44"
  },
  {
    "image": "https://m.media-amazon.com/images/I/81UmTnrBDSL._AC_UL800_.jpg",
    "title": "Redmi A1 (Light Green, 2GB RAM 32GB ROM)",
    "price": 5899,
    "description": "Affordable smartphone with segment best AI dual camera.",
    "quantity": 110,
    "status": "Private",
    "createdAt": "2025-06-16T12:17:16Z",
    "updatedAt": "2025-06-16T12:17:16Z",
    "_id": "33j0akb5c0a8h1k0o8r7mm3n",
    "__v": 0,
    "id": "5pqgik0qk3li4q1mt6mq55"
  },
  {
    "image": "https://m.media-amazon.com/images/I/613SAOPmLeL._AC_UL800_.jpg",
    "title": "OnePlus 11R 5G (Galactic Silver, 8GB RAM, 128GB Storage)",
    "price": 39999,
    "description": "Powerful 5G smartphone with premium design and features.",
    "quantity": 35,
    "status": "Private",
    "createdAt": "2025-06-16T12:18:23Z",
    "updatedAt": "2025-06-16T12:18:23Z",
    "_id": "44k1blc6d1b9i2l1p9s8nn4o",
    "__v": 0,
    "id": "6qrjhl1rl4mj5r2nu7nr66"
  },
  {
    "image": "https://m.media-amazon.com/images/I/61y2VVWcGBL._AC_UL800_.jpg",
    "title": "Fire-Boltt Phoenix Smart Watch with Bluetooth Calling",
    "price": 1699,
    "description": "Smartwatch with 120+ sports modes and health monitoring features.",
    "quantity": 85,
    "status": "Public",
    "createdAt": "2025-06-16T12:19:30Z",
    "updatedAt": "2025-06-16T12:19:30Z",
    "_id": "55l2cmd7e2c0j3m2q0t9oo5p",
    "__v": 0,
    "id": "7rskim2sm5nk6s3ov8os77"
  },
  {
    "image": "https://m.media-amazon.com/images/I/21uXmiH98wL._AC_UL800_.jpg",
    "title": "Samsung 25W USB Travel Adapter for Cellular Phones - White",
    "price": 1099,
    "description": "Compact travel adapter with fast charging capability.",
    "quantity": 180,
    "status": "Public",
    "createdAt": "2025-06-16T12:20:37Z",
    "updatedAt": "2025-06-16T12:20:37Z",
    "_id": "66m3dne8f3d1k4n3r1u0pp6q",
    "__v": 0,
    "id": "8stljn3tn6ol7t4pw9pt88"
  },
  {
    "image": "https://m.media-amazon.com/images/I/51ZT3aMrJIL._AC_UL800_.jpg",
    "title": "pTron Bassbuds Duo in Ear Earbuds with 32Hrs Total Playtime",
    "price": 799,
    "description": "Wireless earbuds with long battery life and touch controls.",
    "quantity": 140,
    "status": "Public",
    "createdAt": "2025-06-16T12:21:44Z",
    "updatedAt": "2025-06-16T12:21:44Z",
    "_id": "77n4eof9g4e2l5o4s2v1qq7r",
    "__v": 0,
    "id": "9tumko4uo7pm8u5qx0qu99"
  },
  {
    "image": "https://m.media-amazon.com/images/I/51zv+mozGgL._AC_UL800_.jpg",
    "title": "TAGG Verve Sense Smartwatch with 1.70'' Large Display",
    "price": 999,
    "description": "Smartwatch with real-time health tracking and long battery backup.",
    "quantity": 65,
    "status": "Private",
    "createdAt": "2025-06-16T12:22:51Z",
    "updatedAt": "2025-06-16T12:22:51Z",
    "_id": "88o5fp0h5f3m6p5t3w2rr8s",
    "__v": 0,
    "id": "0uvnlp5vp8qn9v6ry1rv00"
  }
]


headers = {"Content-Type": "application/json"}

for product in products:
    product["price"] = str(product["price"])
    product["quantity"] = str(product["quantity"])
    response = requests.post(API_URL, json=product, headers=headers)
    print(f"Sent: {product['title']}, Status: {response.status_code}, Response: {response.text}")
    time.sleep(1)  # Optional delay between requests
