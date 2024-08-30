// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});








// Toggle subtopics
document.querySelectorAll('.nav-links > li > a').forEach(link => {
    link.addEventListener('click', function(e) {
        const listItem = this.parentElement;
        if (listItem.querySelector('.subtopics')) {
            e.preventDefault();
            listItem.classList.toggle('active');
        }
    });
});


