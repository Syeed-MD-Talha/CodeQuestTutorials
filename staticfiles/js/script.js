
console.log('Hello world how are you?')


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