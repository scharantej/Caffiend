## Flask Application Design for Single Page Application for Coffee Shop

### HTML Files

- `index.html`: Main HTML file for the application. This will contain the user interface for the coffee shop, including a product list, shopping cart, and checkout form.
- `menu.html`: Partial view that displays the list of coffee products available for purchase.
- `cart.html`: Partial view that displays the items in the user's shopping cart, along with their quantity and price.
- `checkout.html`: Partial view that displays the checkout form, which allows the user to enter their contact and payment information.

### Routes

- `/@`: Root route that serves the `index.html` page.
- `/menu`: Route that serves the `menu.html` partial view.
- `/cart`: Route that serves the `cart.html` partial view.
- `/checkout`: Route that serves the `checkout.html` partial view.
- `/api/products`: API route that returns a list of all available coffee products.
- `/api/cart`: API route that allows the user to add or remove items from their shopping cart.
- `/api/checkout`: API route that processes the user's checkout information and creates an order.