# Marmaris Store
**SE3355 Assignment 2**
### Data Model
I've constructed a data model that includes several essential attributes for the products in my Flask application, such as `product_no`, `description`, `price`, `image`, and `category`. I've decided to use Flask-SQLAlchemy to facilitate interactions with a SQLite database that comes with Flask.

### Assumptions
My application is developed with **Flask**. It is structured around the layout of **Trendyol**, including a homepage, search results, and product details. Each product card is designed to display an image, a description, the price, and a link to view more details. A search feature is integrated to query across all product attributes. For enhanced user navigation, I've included breadcrumbs, and I've ensured that the website is responsive for a range of devices and screen sizes. For responsive design i used **Bootstrap** framework.

### Deployment Errors
- Without `requirements.txt` i couldn't deploy my web app to Azure Web Services. I found this out after some research. 

## Deployment
I deployed the web app to Azure Web Services. The deployment process included setting up the necessary configurations, environment variables, and ensuring all dependencies were listed in `requirements.txt`.

The web app is deployed here via Azure Web Services: [Marmaris Store](https://marmaris-store.azurewebsites.net/)
