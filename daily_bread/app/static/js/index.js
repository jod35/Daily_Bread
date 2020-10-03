const footer=document.querySelector('footer');

window.onload=function(){
    let date = new Date();

    footer.innerHTML=`<p>Daily Bread &copy; ${date.getFullYear()}</p>`
}