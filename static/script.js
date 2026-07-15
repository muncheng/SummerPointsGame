

// --------------------
// NAME PAGE
// --------------------


window.submitName = async function(){


let username =
document.getElementById("usernameInput").value;



if(username.trim()==""){
alert("Enter a name");
return;
}



localStorage.setItem(
"username",
username
);



await addDoc(
collection(db,"users"),
{
name:username,
points:0
}
);



window.location.href="app.html";


}






// --------------------
// CHALLENGES
// --------------------



window.showChallenges=function(){


let content =
document.getElementById("content");



content.innerHTML=`

<h2>Challenges</h2>


<div class="challenge-card">

<h3>Watch a sunset</h3>

<p>
Find a nice place and watch the sunset.
</p>

<p>
Points: 20
</p>


<button onclick="acceptChallenge('Watch a sunset',20)">
Accept
</button>


</div>



<div class="challenge-card">

<h3>Try a new food</h3>

<p>
Eat something new.
</p>

<p>
Points: 15
</p>


<button onclick="acceptChallenge('Try a new food',15)">
Accept
</button>


</div>

`;

}





window.acceptChallenge=function(name,points){


let content =
document.getElementById("content");


content.innerHTML=`

<h2>${name}</h2>


<p>
Upload proof when completed.
</p>


<form 
action="/submit_proof"
method="POST"
enctype="multipart/form-data"
>


<input
type="hidden"
name="username"
value="{{ username }}"
>


<input 
type="hidden"
name="challenge"
value="Watch a sunset"
>


<input
type="hidden"
name="points"
value="20"
>


<input
type="file"
name="photo"
accept="image/*"
>


<button type="submit">
Submit Proof
</button>


</form>


<button onclick="showChallenges()">
Back
</button>


`;

}






// --------------------
// LEADERBOARD
// --------------------


window.showLeaderboard=async function(){


let content =
document.getElementById("content");


let users =
await getDocs(collection(db,"users"));



let html="<h2>Leaderboard</h2>";



let list=[];


users.forEach((user)=>{

list.push(user.data());

});



list.sort(
(a,b)=>b.points-a.points
);



list.forEach((user,index)=>{


html+=`

<p>
${index+1}.
${user.name}
-
${user.points} points
</p>


`;

});



content.innerHTML=html+`

<button onclick="showChallenges()">
Back
</button>

`;


}






// --------------------
// ADMIN
// --------------------



async function loadAdmin(){


let box =
document.getElementById("submissions");



let submissions =
await getDocs(
collection(db,"submissions")
);



box.innerHTML="";



submissions.forEach((item)=>{


let data=item.data();



if(data.status=="pending"){


box.innerHTML+=`

<div class="proof-card">


<h3>
${data.username}
</h3>


<p>
${data.challenge}
</p>


<img src="${data.photo}" width="200">


<button onclick="approve('${item.id}')">
Approve
</button>


<button onclick="reject('${item.id}')">
Reject
</button>


</div>

`;

}


});


}



window.approve=async function(id){


await updateDoc(
doc(db,"submissions",id),
{
status:"approved"
}
);


alert("Approved");

loadAdmin();


}





window.reject=async function(id){


await updateDoc(
doc(db,"submissions",id),
{
status:"rejected"
}
);


loadAdmin();


}





if(document.getElementById("content")){
showChallenges();
}



if(document.getElementById("submissions")){
loadAdmin();
}
