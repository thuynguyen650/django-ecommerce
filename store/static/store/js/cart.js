updateBtns = document.getElementsByClassName('update-cart')
//add item to cart on click
for(i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        const productId = this.dataset.product
        const action = this.dataset.action
        if(user === 'AnonymousUser') {
            addCookieItem(productId, action)
        } else {
            UpdateCart(productId, action)
        }
    })
}

// update cart without login 
// dont need to add anything to database
function addCookieItem(productId, action) {
    // cart = {
    //     1: {'quantity': 4}
    //     3: {'quantity': 2}
    //     4: {'quantity': 1}
    // }
    if(action=='add') {
        if(cart[productId] == undefined) {
            cart[productId] = {
                'quantity': 1
            }
        } else {
            cart[productId]['quantity'] += 1
        }
    } else if (action=='remove') {
        cart[productId]['quantity'] -= 1
        if(cart[productId]['quantity'] < 1) {
            console.log('Item removed!')
            delete cart[productId]
        }
    } else if(action=='delete') {
        console.log('Item removed!')
        delete cart[productId]
    }
    console.log(cart)
    //update cookie
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
    location.reload()
}

//update cart when logged in
function UpdateCart(productId, action) {
    const url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
            'X-CSRFToken': csrftoken
        },
        // send data to backend 
        body: JSON.stringify({
            productId: productId,
            action: action,
        })
    })
    // return a promise, res is the response that received from backend after send data
    .then(res => res.json())
    .then(data => {
        console.log(data)
        location.reload()
    })
}