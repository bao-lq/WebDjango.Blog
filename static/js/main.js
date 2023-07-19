document.addEventListener("DOMContentLoaded", function(event) {
    
    const showNavbar = (toggleId, navId, bodyId, headerId) =>{
        const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId),
        bodypd = document.getElementById(bodyId),
        headerpd = document.getElementById(headerId)

        // delay function
        // var delay = function (elem, callback) {
        //     var timeout = null;
        //     elem.onmouseover = function() {
        //         // Set timeout to be a timer which will invoke callback after 1s
        //         timeout = setTimeout(callback, 500);
        //     };
        
        //     elem.onmouseout = function() {
        //         // Clear any timers set to timeout
        //         clearTimeout(timeout);
        //     }
        // };
        
        // Validate that all variables exist
        if(toggle && nav && bodypd && headerpd){
            // delay function 
            // toggle.addEventListener('mouseover', delay(toggle, function() {
                toggle.addEventListener('mouseenter',() => {
                    // show navbar
                    nav.classList.add('show')
                    // change icon
                    // toggle.classList.toggle('bx-x')
                    // add padding to body
                    bodypd.classList.add('body-pd')
                    // add padding to header
                    headerpd.classList.add('body-pd')
                })
            // )
                
                toggle.addEventListener('mouseleave',() => {
                    // show navbar
                    nav.classList.remove('show')
                    // change icon
                    // toggle.classList.toggle('bx-x')
                    // add padding to body
                    bodypd.classList.remove('body-pd')
                    // add padding to header
                    headerpd.classList.remove('body-pd')
                })
        }
    }
    
    showNavbar('nav-bar','nav-bar','body-pd','header')
    
    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')
    
    function colorLink(){
        if(linkColor){
            linkColor.forEach(l=> l.classList.remove('active'))
            this.classList.add('active')
        }
    }
    linkColor.forEach(l=> l.addEventListener("mouseover", colorLink))
});