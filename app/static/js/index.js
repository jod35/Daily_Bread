const recordAdditionForm = document.querySelector(".add");
const verseContainer = document.querySelector(".verses");
const clearButton=document.querySelector('.clear');
const verseContents=document.querySelectorAll('.verse');
const verseIds=document.querySelectorAll('.verse-id');
const verseNames=document.querySelectorAll('.verse-name');
const verseNotes=document.querySelectorAll('.verse-notes');
const deleteButtons=document.querySelectorAll('.del-btn');
const updateButtons=document.querySelectorAll('.update-btn');
const updateModal=document.querySelector('.update-modal');
const updateForm=document.querySelector('.update');



const closeModal=(id)=>{
	let el=document.getElementById(id);

	el.style.display="none";
}



clearButton.addEventListener('click',()=>{
	clearAllVerses();
})


const clearAllVerses=()=>{
	for(let i =0 ; i < verseContents.length; i++){
		let RESOURCE_URI=`/api/verse/${verseIds[i].innerText}`;

		console.log(RESOURCE_URI);


		fetch(RESOURCE_URI,
				{
					method:"DELETE",
				}
			).then(res=>res.json())
			 .then(data=>{
				 console.log(data)
				 verseContents[i].style.display="none";
			 })
	}
}

recordAdditionForm.addEventListener("submit", (event) => {
  let formdata = new FormData(recordAdditionForm);

  let recordData = {
    verse: formdata.get("verse"),
    notes: formdata.get("notes"),
  };

  console.log(recordData);

  let API_URL = "/api/verses";

  fetch(
    API_URL,

    {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify(recordData),
    }
  )
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      let newVerse = document.createElement("div");

      newVerse.classList.add("verse");

      newVerse.innerHTML = `
				<span class="verse-id">${data.verse.id}</span>
				<h3 class="verse-name">${data.verse.verse}</h3>
				<p>${data.verse.notes}</p>
				<div class="options">
							<a href="#" class="del-btn"><i class="fa fa-trash"  aria-hidden="true"></i></a>
							<a href="#" class="update-btn"><i class="fas fa-feather "></i></a>
				</div>
		`;

	  verseContainer.insertBefore(newVerse,verseContainer.childNodes[0]);
	  
	  setTimeout(() => {
		  location.reload();
	  }, 3000);
    });

  recordAdditionForm.reset();
  event.preventDefault();
});


for(let i =0 ; i < verseContents.length; i++){
	deleteButtons[i].addEventListener('click',()=>{
		let RESOURCE_URI=`/api/verse/${verseIds[i].innerText}`;

		console.log(RESOURCE_URI);


		fetch(RESOURCE_URI,
				{
					method:"DELETE",
				}
			).then(res=>res.json())
			 .then(data=>{
				 console.log(data)
				 verseContents[i].style.display="none";
			 })
	})
}



for(let i =0 ; i < verseContents.length; i++){
	updateButtons[i].addEventListener('click',()=>{
		updateModal.style.display="block";



		let RESOURCE_URI=`/api/verse/${verseIds[i].innerText}`




		fetch(RESOURCE_URI,
				{method:"GET"}
			).then(res=>res.json())
			 .then(data=>{
				 document.querySelector("#update-name").value=data.verse.verse;
				 document.querySelector("#update-notes").value=data.verse.notes;
			 })

		updateForm.addEventListener('submit',(e)=>{
			let updatedData=new FormData(updateForm);
			
			fetch(
				RESOURCE_URI,
				{
					method:"PUT",
					body:JSON.stringify({
						verse:updatedData.get('verse'),
						notes:updatedData.get('notes')
					}),
					headers:{
						"content-type":"application/json"
					}

				}
			)
			.then(res=>res.json())
			.then(data=>{
					verseNames[i].innerText=data.verse.verse;
					verseNotes[i].innerText=data.verse.notes;

					updateModal.style.display="none";
			})

			e.preventDefault();
		})
	})


}