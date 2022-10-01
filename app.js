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
  console.log(button)
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
  // console.log()
  // Success
  let tweet = `
    <div id="${parsedTweet.id}" class="p-4 border-t border-slate-200">
    <div class="flex">
      <img class="flex-none w-12 h-12 rounded-full" src="/images/1.jpg" alt="">
      <div class="w-full pl-4">
        <p class="font-bold">
          @${parsedTweet.user_name}
        </p>            
        <p class="font-thin">
          ${parsedTweet.user_first_name} ${parsedTweet.user_last_name}
        </p>                
        <div class="pt-2 tweet-text">
          ${_one("input", form).value}
        </div>
        
        <div class="flex gap-12 mt-4 text-lg text-gray-400 justify-between">
        <div class="hover:text-red-300 cursor-pointer">
        <i onclick="delete_tweet('${parsedTweet.id}')" class="fas fa-trash ml-auto"></i>
                </div>
                <div class="hover:text-red-300 cursor-pointer">
                  <i class="fa-solid fa-message ml-auto"></i>
                </div>

                <div class="hover:text-blue1">
                  <button type="button" onclick="likeTweet('${parsedTweet.id}')">
                    <i class="fa-solid fa-heart"></i>
                  </button>
                  <span class="text-sm" id="likes${parsedTweet.id}" value="0"></span>
                </div>

                <div>
                  <i class="fa-solid fa-retweet"></i>
                </div>

                <div class="hover:text-blue1">
                  <button type="button" onclick="updateTweet('${parsedTweet.id}', '${parsedTweet.text}')">
                  <i class="fa-solid fa-pen-to-square"></i>
                  </button>
                 
                </div>

               

           </div>
      </div>
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

  document.querySelector(`[id='${tweet_id}']`).remove()
}

//LIKES
function likeTweet(tweet_id) {
    const element = document.getElementById("likes" + tweet_id);
    value = parseInt(element.getAttribute("value"), 10)+1;
    element.setAttribute("value", value)
    element.innerHTML = value;
  
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

