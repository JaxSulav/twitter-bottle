window.addEventListener(
    'DOMContentLoaded', function () {
        const overlay = document.querySelector('#overlay')
        const signupBtn = document.querySelector('#signup-btn')
        const closeBtn = document.querySelector('#close-btn')
        const overlayLogin = document.querySelector("#overlay-login")
        const loginBtn = document.querySelector("#login-btn")
        const closeBtnLogin = document.querySelector("#close-btn-login")
      

      

        signupBtn.addEventListener('click', function() {
            overlay.classList.remove('hidden')
            overlay.classList.add('flex')
        })

        closeBtn.addEventListener('click', function() {
            overlay.classList.remove('flex')
            overlay.classList.add('hidden')
        })

        loginBtn.addEventListener('click', function() {
            overlayLogin.classList.remove('hidden')
            overlayLogin.classList.add('flex')
        })

        closeBtnLogin.addEventListener('click', function() {
            overlayLogin.classList.remove('flex')
            overlayLogin.classList.add('hidden')
        })

    }
)
//############################################################//
//IMAGE
document.querySelector("#user_image").addEventListener("change", function(){
  const reader = new FileReader();
  reader.addEventListener("load", function(){
    localStorage.setItem("my-image", reader.result)
  })
  reader.readAsDataURL(this.files[0])
})

document.addEventListener("DOMContentLoaded", function (){
  const staticImage = "/images/twitter-logo.png"
  const userImageUrl = localStorage.getItem("my-image");
  if(userImageUrl) {
    document.querySelector("#image").setAttribute("src", userImageUrl);
  }else {
    return document.querySelector("#image").setAttribute("src", staticImage)
  }
})


//############################################################//

function _all(q, e=document){return e.querySelectorAll(q)}
function _one(q, e=document){return e.querySelector(q)}


function toggleTweetModal(){
  _one("#tweetModal").classList.toggle("hidden")
}

async function sendTweet(){
  const form = event.target
  // Get the button, set the data-await, and disable it
  const button = _one("button[type='submit']", form)
  button.innerText = button.dataset.await
  // button.innerText = button.getAttribute("data-await")
  button.disabled = true
  const connection = await fetch("/api-create-tweet", {
    method : "POST",
    body : new FormData(form)
  })

  button.disabled = false
  button.innerText = button.dataset.default

  if( ! connection.ok ){
    return
  }

  
  const tweetResponse = await connection.text() // tweet id will be here
  const parsedTweet = JSON.parse(tweetResponse)
  console.log("PT: ", parsedTweet)
  // Success
  let tweet = `
    <div id="${parsedTweet.id}" class="p-4 border-t border-slate-200">
    <div class="flex">
      <img class="flex-none w-12 h-12 rounded-full" src="/images/${parsedTweet.user_image}" alt="">
      <div class="w-full pl-4">
        <p class="font-bold">
          @${parsedTweet.username}
        </p>            
        <p class="font-thin">
          ${parsedTweet.first_name} ${parsedTweet.last_name} <strong>.</strong> ${parsedTweet.date}
        </p>                
        <div class="pt-2 tweet-text">
          ${_one("input", form).value}
        </div>`
        if (parsedTweet.image){
          tweet = tweet + `<img class="mt-2 w-full object-cover h-80" src="/images/${parsedTweet.image}"></img>`
        }
        
        tweet = tweet + `
        <div class="flex gap-12 mt-4 text-lg text-gray-400 justify-between">
                <div id="comm" class="cursor-pointer">
                  <i class="fa fa-comment"></i>
                </div>
                <div id="del" class="cursor-pointer">
                  <i onclick="delete_tweet(${parsedTweet.id})" class="material-icons">delete</i>
                </div>
                <div id="like" class="cursor-pointer">
                  <button type="button" onclick="likeTweet(${parsedTweet.id})">
                    <div id="likes${parsedTweet.id}" style="display: inherit;" class="cursor-pointer">
                      <i class="fa fa-heart"></i>
                    </div>
                  </button>
                  <span id="likes_span${parsedTweet.id}" class="text-sm"
                    value="0">0</span>
                </div>

                <div id="retweet" class="cursor-pointer">
                  <i class="fa fa-retweet"></i>
                </div>

                <div>
                  <i class="fa-solid fa-pen-to-square"></i>
                </div>

              </div>
  `
  _one("input", form).value = ""  

  _one("#tweets").insertAdjacentHTML("afterbegin", tweet)

}


async function delete_tweet(tweet_id){
  // Connect to the api and delete it from the "database"
  const connection = await fetch(`/api-delete-tweet/${tweet_id}`, {
    method : "DELETE"
  })
  if( ! connection.ok ){
    alert("uppps... try again")
    return
  }

  document.getElementById("tweet" + tweet_id).remove();
}

//LIKES
async function likeTweet(tweet_id) {
    const form = new FormData()
    const element = document.getElementById("likes" + tweet_id);
    span_element = document.getElementsByTagName('span')["likes_span" + tweet_id];
    value = parseInt(span_element.getAttribute("value"), 10)+1;
    
    form.append("tweet_id", tweet_id)
    form.append("likes", value)
    const connection = await fetch("/api-like-tweet", {
      method : "POST",
      body : form
    })

    if( ! connection.ok ){
      return
    }
    
    const tweetResponse = await connection.text() 
    const parsedTweet = JSON.parse(tweetResponse)
    
    if (parsedTweet.success == true) {
      element.setAttribute("style", "color: deeppink")
      span_element.innerHTML = value;
    }
      // ELSE UNLIKE
}


async function updateTweet(tweet_id) {

  const element = document.getElementById(tweet_id)
  const text = element.querySelector('.tweet-text')


  let response = prompt("Update Tweet", text.innerText)

  if(response){
  const form = {
    tweet_id,
    tweet_text : response
  }
 
  const connection = await fetch(`/api_update_tweet`, {
    method : "POST",
    body : JSON.stringify(form)
  })

  if(!connection.ok){
    return
  }


  text.textContent = response
  
}
}

