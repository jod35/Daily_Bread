const footer = document.querySelector('footer');

window.onload = function () {
    let date = new Date()

    footer.innerHTML = `<p>Daily Bread &copy; ${date.getFullYear()}</p>`
}

const recordAdditionButton = document.querySelector('#add-btn');
const recordViewButton = document.querySelector('#view-btn');
const recordFormContainer = document.querySelector('.add-section');
const recordViewSection = document.querySelector('.view-section');

recordAdditionButton.addEventListener('click', showRecordForm)
recordViewButton.addEventListener('click', showRecordsView)

function showRecordForm() {
    recordViewSection.style.display = "none";
    recordFormContainer.style.display = "block";

}

function showRecordsView() {
    recordFormContainer.style.display = "none";
    recordViewSection.style.display = "block";
}


const verse_submit_button = document.querySelector("#send_data");
let bible_verse_content = document.querySelector("#bible_verse").value;
let notes_content = document.querySelector("#notes").value;
let message_display=document.querySelector(".message");


const xHttp = new XMLHttpRequest();


function Verse(bible_verse, notes) {
    this.bible_verse = bible_verse;
    this.notes = notes;
}

const createVerse = function (bible_verse, notes) {
    return new Verse(bible_verse, notes);
}

const handleStateChange = function () {
    if (xHttp.readyState == 4) {
        if (xHttp.status == 201) {
            console.log("Request sent to server");
            alert(JSON.parse(xHttp.responseText));
        }
    }
    else {
        console.log("Something Happened: " + xHttp.status);
    }
}

const startRequest = function () {
    xHttp.onreadystatechange = handleStateChange();
    xHttp.open("POST", "/dailybread/add_verse");
    xHttp.setRequestHeader("Content-Type", "application/json");

    let new_verse = createVerse(bible_verse_content, notes_content);
    console.log(JSON.stringify(new_verse));

    xHttp.send(JSON.stringify(new_verse));

    message_display.style.display="block";
    message_display.innerHTML=`<p class="green-text">Verse Created Sucessfully</p>`;
}

verse_submit_button.onclick = function () {
    startRequest();
}