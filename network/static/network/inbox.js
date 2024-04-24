document.addEventListener('DOMContentLoaded', () => {
    const editButtons = document.querySelectorAll('#edit-button');
    editButtons.forEach(editButton => {
      editButton.addEventListener('click', () => {
    //document.querySelector('#edit-button').addEventListener('click', function(){
      post_id = editButton.getAttribute("data-post-id");
      console.log(post_id);
      document.querySelector(`#opr${post_id}`).style.display = 'none';
      const post = document.querySelector(`#pst${post_id}`);
      const value = document.querySelector(`#psttxt${post_id}`).innerHTML;
      //post_id = document.querySelector("#post_id").getAttribute("data-post-id");


      console.log(value);
    

      post.innerHTML = `<div class="card-footer py-3 border-0" style="background-color: #f8f9fa;">
      <div class="d-flex flex-start w-100">
        
        <div class="form-outline w-100">
          <textarea name="post_text" class="form-control" id="textAreaExample${post_id}" rows="3" style="background: #fff;">${value}</textarea>
        </div>
      </div>
      <div class="float-end mt-2 pt-1">
        <button type="button" class="btn btn-primary btn-sm" id = "save-btn${post_id}">
          Save 
        </button>
      </div>
    </div>`;

    console.log("Update post function is ready to update");

    
    
      document.querySelector(`#save-btn${post_id}`).addEventListener('click', function() {
          update_post(post_id); 
      });  
      });
    });

    //const like_Button = document.querySelector("#like-button");
    //const likeCounter = document.querySelector("#like-counter");

    const likeButtons = document.querySelectorAll('#like-button');
    likeButtons.forEach(likeButton => {
      likeButton.addEventListener('click', () => {
        post_id = likeButton.getAttribute("like-post-id");
        current_user = likeButton.getAttribute("like-post-user");
        like_num = likeButton.getAttribute("like-num");
        
        console.log(`Like button for post ${post_id} clicked by ${current_user}`);
        

        update_like(post_id, current_user,like_num);
      });
    });
/*
    const editButtons = document.querySelectorAll('#edit-button');
    
  
    editButtons.forEach(editButton => {
      editButton.addEventListener('click', () => {
        const cardBody = editButton.closest('.card-body');
        const postContent = cardBody.querySelector('.post-text');
        const originalText = postContent.textContent;
  
        // Replace post content with a textarea
        const textarea = document.createElement('div');
        textarea.innerHTML = `<div id = "change" class="card-footer py-3 border-0" style="background-color: #f8f9fa;">
        <div class="d-flex flex-start w-100">
          
          <div class="form-outline w-100">
            <textarea id = "post_text" name = "post_text" placeholder="What's in your mind, {{request.user}}?" class="form-control" id="textAreaExample" rows="3"
              style="background: #fff;">${originalText}</textarea>
          </div>
        </div>
        <div class="float-end mt-2 pt-1">
          <button id = "save_btn" type="submit" class="btn btn-primary btn-sm">
            Save 
          </button>
        </div>
      </div>`;
  
        // Find the element to replace (here, we assume it's a div with class "post-text")
        const postText = cardBody.querySelector('.post-text');
        cardBody.replaceChild(textarea, postText);

        post_id = document.querySelector("#post_id").getAttribute("data-post-id");
        
        document.querySelector("#save_btn").addEventListener('submit', update_post(post_id));
        //document.querySelector('#compose').addEventListener('click', compose_email);
       
      });
    });

    const like_Button = document.getElementById("like-button");
    const likeCounter = document.getElementById("like-counter");

let likeCount = 0;

like_Button.addEventListener("click", () => {
  likeCount++;
  updateLikeCounter();
});

function updateLikeCounter() {
  likeCounter.textContent = likeCount;
  
  if (likeCount > 0) {
    likeCounter.style.opacity = 1;
  } else {
    likeCounter.style.opacity = 0;
  }
}


// Function to update the post
function update_post(post_id)
  post_text = document.querySelector("#post_text").value;
  fetch('/post_update', {
    method: 'POST',
    body: JSON.stringify({
        post_id: post_id,
        post_text: post_text  
    })
  })
  .then(response => response.json())
  .then(post => {
      // Print result
      console.log(post);

      let text = post.text;
      const postText = cardBody.querySelector('#change');

      const updtd_text = document.createElement('div');
      updtd_text.innerHTML = ` <p class="mt-3 mb-4 pb-2 post-text">
      {{${text}}}
    </p>`;

      postText.innerHTML = updtd_text;
      //load_mailbox("sent");
  })
   // Catch any errors and log them to the console
   .catch(error => {
    console.log('Error:', error);
});

*/


// Function to update the post
function update_post(post_id){
  console.log(post_id);
  console.log("Update post function is ready to update");
  updtd_text = document.querySelector(`#textAreaExample${post_id}`).value;
  console.log(updtd_text);

  fetch('/post_update', {
    method: 'POST',
    body: JSON.stringify({
        post_id: post_id,
        post_text: updtd_text  
    })
  })
  .then(response => response.json())
  .then(Post => {
      // Print result
      console.log(Post);

      let text = Post.text;
      
      document.querySelector(`#pst${post_id}`).innerHTML = ` <p class="mt-3 mb-4 pb-2 post-text id = "psttxt${post_id}">
      ${text}
    </p>`;     

    document.querySelector(`#opr${post_id}`).style.display = 'block';
  })
  // Catch any errors and log them to the console
  .catch(error => {
    console.log('Error:', error);
  });

  return false;
}


function update_like(post_id, current_user, like_num){
  fetch('/like_update', {
    method: 'POST',
    body: JSON.stringify({
        post_id: post_id,
        current_user: current_user
    })
  })  
  .then(response => response.json())
  .then(Post => {
      // Print result
      console.log(Post);
      let likes = Post.num_likes;
      let p = document.querySelector(`#like${post_id}`);
      let likeCounter = p.querySelector('span');

      
      likeCounter.innerHTML = likes;
      if (likes > 0){
        likeCounter.style.opacity = 1;
      }
      else{
        likeCounter.style.opacity = 0;
      }


      if(like_num < likes){
        document.querySelector(`#icon${post_id}`).innerHTML = `<i class="fas fa-thumbs-up"></i>`;
      }
      else{
        document.querySelector(`#icon${post_id}`).innerHTML = `<i class="far fa-thumbs-up me-2"></i>`;
      }
      
      
  })
  // Catch any errors and log them to the console
  .catch(error => {
    console.log('Error:', error);
  });

  
}



const likeCounters = document.querySelectorAll('#like-counter');
likeCounters.forEach(likeCounter => {
updateLikeCounter(likeCounter);


});

function updateLikeCounter(likeCounter ,increment) {

  let likeCount = parseInt(likeCounter.innerHTML);
  if (increment === true){
    likeCount++;
  }
  
  if (likeCount > 0) {
    likeCounter.style.opacity = 1;
  } else {
    likeCounter.style.opacity = 0;
  }
}

});
