// Wait for the DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on the demo page
    if (document.getElementById('demo-container')) {
        initializeDemo();
    }

    // Add smooth scrolling to all links
    addSmoothScrolling();
});

function initializeDemo() {
    const convertButton = document.getElementById('convert-button');
    const imageInput = document.getElementById('image-input');
    const resultContainer = document.getElementById('result-container');
    const faviconPreview = document.getElementById('favicon-preview');

    convertButton.addEventListener('click', function() {
        const file = imageInput.files[0];
        if (file) {
            // Simulate conversion process
            resultContainer.innerHTML = `<p>Converting ${file.name} to favicon...</p>`;
            
            // Read the file and create a preview
            const reader = new FileReader();
            reader.onload = function(e) {
                setTimeout(function() {
                    resultContainer.innerHTML = '<p>Conversion complete! (This is a simulated result)</p>';
                    
                    // Create favicon previews
                    const sizes = [16, 32, 48, 64];
                    faviconPreview.innerHTML = '';
                    sizes.forEach(size => {
                        const img = document.createElement('img');
                        img.src = e.target.result;
                        img.style.width = `${size}px`;
                        img.style.height = `${size}px`;
                        img.style.margin = '5px';
                        faviconPreview.appendChild(img);
                    });
                }, 2000); // Simulate 2 seconds of processing time
            }
            reader.readAsDataURL(file);
        } else {
            resultContainer.innerHTML = '<p>Please select an image first.</p>';
        }
    });

    imageInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            resultContainer.innerHTML = `<p>Selected file: ${file.name}</p>`;
        }
    });
}

function addSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
}

// Add a simple animation to the logo on the home page
const logo = document.querySelector('.logo');
if (logo) {
    logo.addEventListener('mouseover', function() {
        this.style.transform = 'scale(1.1)';
        this.style.transition = 'transform 0.3s ease-in-out';
    });

    logo.addEventListener('mouseout', function() {
        this.style.transform = 'scale(1)';
    });
}

// Add a 'back to top' button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("backToTop").style.display = "block";
    } else {
        document.getElementById("backToTop").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// Add the back to top button to the DOM
const backToTopButton = document.createElement('button');
backToTopButton.id = 'backToTop';
backToTopButton.title = 'Go to top';
backToTopButton.innerHTML = '↑';
backToTopButton.onclick = topFunction;
document.body.appendChild(backToTopButton);

// Add styles for the back to top button
const style = document.createElement('style');
style.innerHTML = `
    #backToTop {
        display: none;
        position: fixed;
        bottom: 20px;
        right: 30px;
        z-index: 99;
        font-size: 18px;
        border: none;
        outline: none;
        background-color: #333;
        color: white;
        cursor: pointer;
        padding: 15px;
        border-radius: 4px;
    }

    #backToTop:hover {
        background-color: #555;
    }
`;
document.head.appendChild(style);
