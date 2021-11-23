let options = Array.from(document.querySelectorAll('li'));
let images = Array.from(document.images);
options.forEach((li) => {
    li.addEventListener('click', removeActive)
    li.addEventListener('click', addImages)
})

function removeActive(e) {
    options.forEach(li => {
        li.classList.remove('active');
        e.target.classList.add('active');
    })
}

function addImages(e) {
    images.forEach(img => {
        img.style.opacity = 0;
        if (img.classList.contains(e.target.dataset.cat)) {
            img.style.display = 'block'
            img.style.opacity = 1;
        } else {
            setTimeout(() => {
                img.style.display = 'none'
                console.log(img)
            }, 500);
        }
    })
    if (e.target.dataset.cat == 'all') {

        document.querySelector('.alert').style.display = 'flex';
    }
    //let selectedElements = document.querySelectorAll(e.target.dataset.cat)
    //selectedElements.forEach(img => img.style.display = 'block')
}
console.log(options);
console.log(images);
document.querySelector('.alert').addEventListener('click', () => {
    document.querySelector('.alert').style.display = 'none';
})