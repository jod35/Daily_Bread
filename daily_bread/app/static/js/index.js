const footer=document.querySelector('footer');

window.onload=function(){
    let date = new Date()

    footer.innerHTML=`<p>Daily Bread &copy; ${date.getFullYear()}</p>`
}

const recordAdditionButton=document.querySelector('#add-btn');
const recordViewButton=document.querySelector('#view-btn');
const recordFormContainer=document.querySelector('.add-section');
const recordViewSection=document.querySelector('.view-section');

recordAdditionButton.addEventListener('click',showRecordForm)
recordViewButton.addEventListener('click',showRecordsView)

function showRecordForm(){  
    recordViewSection.style.display="none";
    recordFormContainer.style.display="block";

}

function showRecordsView(){
    recordFormContainer.style.display="none";
    recordViewSection.style.display="block";
}