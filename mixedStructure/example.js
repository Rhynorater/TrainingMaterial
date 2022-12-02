document.getElementById("greetButton").addEventListener("click", function(){
		document.getElementById("name").innerText=document.getElementById("name_input").value;
});
document.getElementById("saveButton").addEventListener("click", function(){
		var name = document.getElementById("name_input").value;
		fetch("http://localhost:8001/checkUser?name="+name).then((d)=>d.json()).then(function(response){
			if (response['alreadyRegistered']){
					alert(name+"! You already registered at: "+response['time'])
			} else if (response['registered']){
					alert("Welcome "+response['name']+"! You've successfully registered.")
			}
		})
});
