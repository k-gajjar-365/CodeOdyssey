
  let productCount = 0;

document.addEventListener("DOMContentLoaded", () => {
  const products = [
    { id: 1, name: "Product 1 ", price: 29.99 },
    { id: 2, name: "Product 2 ", price: 19.99 },
    { id: 3, name: "Product 3 ", price: 59.99 },
  ];

  const cart = [];

  const productList = document.getElementById("product-list");
  const cartItems = document.getElementById("cart-items");
  const emptyCartMessage = document.getElementById("empty-cart");
  const cartTotalMessage = document.getElementById("cart-total");
  let totalPriceDisplay = document.getElementById("total-price");
  const checkoutBtn = document.getElementById("checkout-btn");


  checkoutBtn.addEventListener("click", () => {
    cart.length = 0;
    alert("Checkout successfully");
    renderCart();
  });

  products.forEach((product) => {
    const productDiv = document.createElement("div");
    productDiv.classList.add("product");
    productDiv.innerHTML = `
        <span>${product.name} - $${product.price.toFixed(2)}</span>
        <button class="btn btn-outline-warning" data-id="${
          product.id
        }">Add to cart</button>
        `;

    productList.appendChild(productDiv);
  });

  productList.addEventListener("click", (e) => {
    if (e.target.tagName != "BUTTON") return;

    const productId = parseInt(e.target.getAttribute("data-id"));

    const product = products.find((p) => p.id === productId);

    addToCart(product);
  });

  function addToCart(product) {
    cart.push(product);
    renderCart();
  }


  function renderCart() {
    cartItems.innerHTML = "";
    let totalPrice = 0;

    if (cart.length > 0) {
      emptyCartMessage.classList.add("hidden");
      cartTotalMessage.classList.remove("hidden");

      cart.forEach((item) => {
        totalPrice += item.price;
        const cartItem = document.createElement("div");

        cartItem.innerHTML = `
        <div class="item" count="${productCount++}">
           <span> ${item.name} - $${item.price.toFixed(2)}</span>
           <button pro-id="${item.id}" class="btn btn-danger">Delete</button>
            </div>`;
        cartItems.appendChild(cartItem);

        totalPriceDisplay.innerHTML = `$${totalPrice.toFixed(2)}`;
      });
    } else {
      emptyCartMessage.classList.remove("hidden");
      totalPriceDisplay.innerHTML = `$0.00`;
    }

    cartItems.addEventListener("click", (e) => {
      if (e.target.tagName != "BUTTON") return;

      const selectedProduct = e.target;

      const index = cart.findIndex(item => item.id === parseInt(selectedProduct.getAttribute("pro-id")))
      if(index != -1)
      cart.splice(index,1);

      totalPrice -= selectedProduct.price;

      renderCart();
    });
  }
});
