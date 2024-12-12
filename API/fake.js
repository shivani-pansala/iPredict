
const url = "https://jsonplaceholder.typicode.com/posts";

const getbutton = document.querySelector("#get");
const postbutton = document.querySelector("#post");
const putbutton = document.querySelector("#put");
const deletebutton = document.querySelector("#delete");


//get Data from API
const getapi = async () => {
  try{
    const response = await fetch(url);
    const posts = await response.json();
    return posts;
  }
  catch(error){
    console.error("Error fetching data: ", error);
  }
  
}

//get button
getbutton.addEventListener("click",async () =>{
     const posts = await getapi();
    if(posts){
     const table = `<table class="table">
     <thead>
     <tr>
       <th>ID</th>
       <th>Title</th>
     </tr>
     </thead>
     <tbody>
     ${posts.map(post => `<tr>
       <td>${post.id}</td>
       <td>${post.title}</td>
     </tr>`) 
     .join("\n")}
     </tbody>
     </table>`;
    document.querySelector("#table").innerHTML = table;    
    } 
});

//Post Data from API
const postapi = async (newpost) => {
  try{
    const response = await fetch(url, {
      method: "POST",
      body: JSON.stringify(newpost),
      headers: {
        "Content-Type": "application/json"},
    });
    const post = await response.json();
    return post;
    }
    catch(error){
    console.log(error);
  }
}

//post button
postbutton.addEventListener("click", async () =>{
   const newPost = {
     userId: 1,
     title: "New Post",
     body: "This is a new post",
   };
   const add = await postapi(newPost)
    console.log(add);
});

//PUT Data from API
const putapi = async(newPost,id) => {
  try{
    const response = await fetch(`${url}/${id}`, {
      method: "PUT",
      body: JSON.stringify(newPost),
      headers: {
        "Content-Type": "application/json"},
    });
    const post = await response.json();
    return post;
    }
    catch(error){
    console.log(error);
  }
};
 
//put button
putbutton.addEventListener("click", async () =>{
  const newPost = {
    id: 2,
    userId: 1,
    title: "Upadates Post Title",
    body: "Updated Post Body",
  };
  const update = await putapi(newPost,2)
   console.log(update);
});

//DELETE Data from API
const deleteapi = async(id) => {
  try{
    const response = await fetch(`${url}/${2}`, {
      method: "DELETE",
    });
    return response.ok;
    }
    catch(error){
    console.log(error);
  }
};

//delete button
deletebutton.addEventListener("click", async () =>{
     const del = await deleteapi(2);
     console.log(del);
});
