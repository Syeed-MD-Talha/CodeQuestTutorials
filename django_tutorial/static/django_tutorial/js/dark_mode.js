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
toggleSwitch.addEventListener('change', switchTheme, false);



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