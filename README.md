# Django-Ecommerce

Django Ecommerce app by Hammad Faiz and Alex Taylor

Project Goal: Create an SSR (Server Side Rendering) Project so we can get a full understanding of a backend framework.

Description: Django/Python SSR (Server Side Rendering) Ecommerce website equipped with cart, checkout, payment methods, product rating, live chat, and return option.

Technologies: Django, Python, Javascript, HTML, CSS, Bootstrap, WebSocket, Git.

We Authenticated users at login by using Django built-in authentication.

![Django-14](https://user-images.githubusercontent.com/105521583/198363056-af45214c-3f61-4d94-9cd9-be62f7652786.png)

Once logged in, Users will be redirected to the main page. There is a navbar at the top of the main page which users can use to navigate to different pages along with the logout option. This navbar is consistently at the top of every page throughout the website. At the Bottom, all the items are listed using a CSS grid layout. 

![navbar](https://user-images.githubusercontent.com/105521583/198407990-bc300707-1dcc-4edf-aa36-236f0a64412e.png)

![Django-2](https://user-images.githubusercontent.com/105521583/198365036-b73fb232-cec5-4730-b3ca-edcf667cdd94.png)

Users have the option to click on any item which will take them to the item detail page. This page has details about the product like the image, price, and description. This page also includes many functionalities like add to cart option, update product option, delete option, review section, and live chat.

In the live chat, users can ask questions about the product from the admin. It has the username to the left and the message they sent to the right as shown below.

![live chat](https://user-images.githubusercontent.com/105521583/198624191-373d3875-17bc-417c-920b-3318c4309a1e.png)

In the review section, users can leave a comment on the product. Users can also like each other comments.

![review section](https://user-images.githubusercontent.com/105521583/198618581-57c294ff-fe93-43fe-839e-ddbbd660d6c1.png)

If Users want to check out, they can navigate to the cart using the navbar. This cart has all the functionality a cart should have.

![cart](https://user-images.githubusercontent.com/105521583/198625456-af738de6-d3eb-424a-92f0-7ff239d54e4f.png)

On the checkout page, users are asked for the shipping address.

![Django-9](https://user-images.githubusercontent.com/105521583/198387097-8ffd7963-c833-4b1d-8807-91996fc2b016.png)

Once users enter their shipping address they can click the continue button. This will make the payment methods appear. 

![Django-10](https://user-images.githubusercontent.com/105521583/198387216-33384fa4-a32d-40e7-aeeb-465e6f9b74fc.png)

Users can checkout with any of the payment options available. This will then complete the transaction. 

![payment complete](https://user-images.githubusercontent.com/105521583/198388429-3f7b00a1-674a-4d89-b776-09306eaa4118.png)

If Users want to return something or check up on their past orders they can click on purchases in the navbar. Purchases page has every order made by that specific user. There is also a view details option. Here I am going to click view details for the order we just made.

![Django-11](https://user-images.githubusercontent.com/105521583/198389357-fac4239d-7654-4e0f-a7a9-a5473d5f7427.png)

Now we can see specific details of the order we placed earlier along with the shipping address of the order. There is also a return option. Clicking the return button will delete the item from the order.

![Django-12](https://user-images.githubusercontent.com/105521583/198390295-df51ac60-238b-4f34-b8b3-da60664f1aa3.png)
