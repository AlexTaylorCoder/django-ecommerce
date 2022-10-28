# django-ecommerce

Django Ecommerce app by Hammad Faiz and Alex Taylor

Project Goal: Create a SSR (Server Side Rendering) Project so we can get a full understanding of a backend framwork.

Description: Django/Python SSR (Server Side Rendering) Ecommerce website equipped with cart, checkout, payment methods, product rating, live chat, and return option.

Technologies: Django, Python, Javascript, HTML, CSS, Bootstrap, WebSocket, Git.

We Authenticated users at login by using Django built in authentication.

![Django-14](https://user-images.githubusercontent.com/105521583/198363056-af45214c-3f61-4d94-9cd9-be62f7652786.png)

Once logged in, Users will be redirected to the main page. There is navbar at the top of the main page which users can use to navigate to different pages along with the option to logout. This navbar is consistently at the top of every page throughout the website. At the Bottom of main page all the products are listed using css grid layout. 

![navbar](https://user-images.githubusercontent.com/105521583/198407990-bc300707-1dcc-4edf-aa36-236f0a64412e.png)

![Django-2](https://user-images.githubusercontent.com/105521583/198365036-b73fb232-cec5-4730-b3ca-edcf667cdd94.png)

Users have the option to click any item which will take them ti item detail page. This page has details about the product like the image, price and description. This page also includes many functionalities like add to cart option .update product option, delete option, review section, and live chat to ask questions about the product from the admin. 

![Django-6](https://user-images.githubusercontent.com/105521583/198372114-e806aff2-0704-4fea-ae17-6ede2a79d25e.png)

If Users want to checkout, they can click the cart icon in the navbar which will then redirect them to the cart page. This cart has all the functionality a cart should. Users can edit the quantity of a product by clicking on the plus or minus Icon and the total price of the cart will adjust along with the total price of the item. For checkout users can click the green button at the top right corner. This will then redirect them to the checkout page.

![Django-7](https://user-images.githubusercontent.com/105521583/198385085-248aeae2-d3cf-4a59-a994-44a463357b9c.png)

In the checkout page users are asked for shipping address.

![Django-9](https://user-images.githubusercontent.com/105521583/198387097-8ffd7963-c833-4b1d-8807-91996fc2b016.png)

Once users enter their shipping address they can click the continue button. This will make the payment methods appear. 

![Django-10](https://user-images.githubusercontent.com/105521583/198387216-33384fa4-a32d-40e7-aeeb-465e6f9b74fc.png)

Users can checkout with any of the payment options avaliable. This will then complete the transaction. 

![payment complete](https://user-images.githubusercontent.com/105521583/198388429-3f7b00a1-674a-4d89-b776-09306eaa4118.png)

If Users want to return something or checkup on their past orders they can click on purchase the navbar. Purchases page has every order listed made by that specific user. There is also view details option which shows the details of that specific order. Here I am going to click view details for order listed at the top. This is the same we made earlier.  

![Django-11](https://user-images.githubusercontent.com/105521583/198389357-fac4239d-7654-4e0f-a7a9-a5473d5f7427.png)

Here we can see specific details of the order we placed earlier along with the shipping address of the order. There is also a return option. Clicking the return button will delete the item from the order.

![Django-12](https://user-images.githubusercontent.com/105521583/198390295-df51ac60-238b-4f34-b8b3-da60664f1aa3.png)












