let tabs = Array.from(document.querySelectorAll('li'));
let contents = Array.from(document.querySelectorAll('.content div'));

function removeActive() {
    tabs.forEach(tab => {
        tab.classList.remove('active');
    })
    contents.forEach(content => {
        content.style.display = 'none'
    })
}

function mainFunctionality(e) {
    let tab = e.target;
    removeActive();
    tab.classList.add('active');
    let content = document.querySelector(tab.dataset.cat);
    content.style.display = 'block';
}
document.querySelector('ul').addEventListener('click', mainFunctionality)