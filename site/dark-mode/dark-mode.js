const container = document.body;
if(localStorage.getItem("data-theme")){
    container.setAttribute("data-theme",localStorage.getItem("data-theme")); 
    toggleDark(1)
} 
//actually use the saved value


function toggleDark(r) {//this function is executed when switching from the current theme to the other
    const dataTheme = container.getAttribute("data-theme");
    var style = document.createElement('style');
    let theme_switch;
    if(dataTheme === "light") {theme_switch = 1} else {theme_switch = 0}
    if(r){theme_switch = !theme_switch}//so the oppisite of the theme stored is used when calling this function 
    if (theme_switch) {
        container.setAttribute("data-theme", "dark");
        document.getElementById("night").style.display = "block";
        document.getElementById("light").style.display = "none";
        localStorage.setItem("data-theme", "dark");
        
    } else {
        container.setAttribute("data-theme", "light");
        document.getElementById("night").style.display = "none";
        document.getElementById("light").style.display = "block";
        localStorage.setItem("data-theme", "light");
    }
}

// if (dataTheme === "dark") {
//     var style = document.createElement('style');
//     style.innerHTML = `
//     blockquote p{
//         color: #f8f7f2;
//     }
//     `;
//     document.head.appendChild(style);
// }


