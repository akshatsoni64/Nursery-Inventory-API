# Nursery-Inventory-API
Backend Part of Nursery Inventory System, ready to integrate with any frontend application

# Installation Notes:
- Configure virtual environment(optional)<br>
<code>virtualenv venv -p python3</code>
- Activate virtualenv<br>
<code>source venv/bin/activate</code>
- Install dependencies from requirements.txt<br>
<code>pip3 install -r requirements.txt</code>
- Make empty database named 'nursery'
- Configure database connection in settings.py
- Migrate the database<br>
<code>python3 manage.py migrate</code>
- Fire up the server<br>
<code>python3 manage.py runserver</code>

# API Documentation:
- Available Options: <code>localhost:8000</code><br>
<i>Check Available APIs</i>
- Plants: <code>localhost:8000/p</code><br>
<b>GET:</b> <i>Get the list of available products</i><br>
<b>POST:</b> <i>Add new Plant</i><br>
<b>Parameters:</b> name, stock, price, image<br>
- Plant Details: <code>localhost:8000/p/[id]</code><br>
<i>Get details of the product with given [id]</i><br>
- Orders: <code>localhost:8000/o</code><br>
<b>GET:</b> <i>Check orders list</i><br>
<b>POST:</b> <i>Place Order</i><br>
<b>Parameters:</b> plant_id, quantity<br>

- Login: <code>localhost:8000/login</code><br>
<b>Parameters:</b>
username, password<br>
- Register: <code>localhost:8000/register</code><br>
<b>Parameters:</b>
username, first_name, last_name, email, password1, password2, mobile, address, type<br>
- Logout: <code>localhost:8000/logout</code>

Note: Authentication is mandatory
