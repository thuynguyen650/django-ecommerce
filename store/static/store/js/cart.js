updateBtns = document.getElementsByClassName('update-cart')

for(i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        const productId = this.dataset.product
        const action = this.dataset.action
        if(user === 'AnonymousUser') {
            console.log('You have not logged in!')
        } else {
            UpdateCart(productId, action)
        }
    })
}

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