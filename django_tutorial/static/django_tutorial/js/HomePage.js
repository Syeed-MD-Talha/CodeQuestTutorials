// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Progress bar
window.onscroll = function() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = (winScroll / height) * 100;
    document.getElementById("progressBar").style.width = scrolled + "%";
};

// Dark mode toggle
const toggleSwitch = document.querySelector('#theme-toggle');
const currentTheme = localStorage.getItem('theme');

if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
    if (currentTheme === 'dark') {
        toggleSwitch.checked = true;
    }
}

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    }    
}

// toggleSwitch.addEventListener('change', switchTheme, false);

// // Toggle subtopics
// document.querySelectorAll('.nav-links > li > a').forEach(link => {
//     link.addEventListener('click', function(e) {
//         const listItem = this.parentElement;
//         if (listItem.querySelector('.subtopics')) {
//             e.preventDefault();
//             listItem.classList.toggle('active');
//         }
//     });
// });


toggleSwitch.addEventListener('change', switchTheme, false);

// Toggle subtopics
document.addEventListener('DOMContentLoaded', function() {
    const topicLinks = document.querySelectorAll('.nav-links > li > a');
    
    // Initially hide all subtopics
    document.querySelectorAll('.subtopics').forEach(subtopic => {
        subtopic.style.display = 'none';
    });
    
    // Remove 'active' class from all list items
    document.querySelectorAll('.nav-links > li').forEach(li => {
        li.classList.remove('active');
    });

    topicLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const listItem = this.parentElement;
            const subtopics = listItem.querySelector('.subtopics');
            
            if (subtopics) {
                // Toggle the display of subtopics
                if (subtopics.style.display === 'none' || subtopics.style.display === '') {
                    subtopics.style.display = 'block';
                    listItem.classList.add('active');
                } else {
                    subtopics.style.display = 'none';
                    listItem.classList.remove('active');
                }
            }
        });
    });
});




// Code for copy button......................

document.querySelectorAll('code').forEach(codeElement => {codeElement.classList.add('language-python');});

document.addEventListener('DOMContentLoaded', (event) => {
    // Add copy buttons to pre elements
    const preElements = document.querySelectorAll('pre');
    preElements.forEach((preElement) => {
        // Create the copy button
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.innerHTML = 'Copy'; // Using Font Awesome icon
        copyButton.setAttribute('aria-label', 'Copy code to clipboard');
        
        // Position the button
        preElement.style.position = 'relative';
        
        // Add the copy button to the pre element
        preElement.appendChild(copyButton);
        
        // Add click event to the copy button
        copyButton.addEventListener('click', () => {
            const textToCopy = preElement.textContent;
            
            navigator.clipboard.writeText(textToCopy).then(() => {
                // copyButton.innerHTML = '<i class="fas fa-check"></i>'; // Change to checkmark icon
                copyButton.innerHTML='Copied!'
                setTimeout(() => {
                    copyButton.innerHTML = 'Copy'; // Change back to copy icon
                }, 1000);
            }).catch(err => {
                console.error('Failed to copy: ', err);
            });
        });
    });
});



/*********   switching codeblock for dark and light mode     ******/

const themeToggle = document.getElementById('theme-toggle');
    const prismTheme = document.getElementById('prism-theme');

    // Function to switch Prism themes
    function switchPrismTheme(isDarkMode) {
        if (isDarkMode) {
            prismTheme.href = "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-twilight.min.css";
        } else {
            prismTheme.href = "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css";
        }
    }

    // Check if the dark mode is enabled by default and set the theme
    switchPrismTheme(themeToggle.checked);

    // Listen for theme toggle
    themeToggle.addEventListener('change', function() {
        switchPrismTheme(this.checked);
    });