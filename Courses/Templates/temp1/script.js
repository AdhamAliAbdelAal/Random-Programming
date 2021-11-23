let links = document.querySelector('.links');
let ul = document.querySelector('ul');
let secondLayer = document.querySelector('.icon span:nth-child(2)');
links.addEventListener('click', (e) => {
    console.log(ul.style.transform)
    if (ul.style.transform != 'rotateX(0deg)') {
        ul.style.transform = 'rotateX(0deg)';
        secondLayer.style.width = "100%";
    } else {
        ul.style.transform = 'rotateX(90deg)';
        secondLayer.style.width = "60%";
    }
})