let serial = document.querySelector('.serial'),
    generator = document.querySelector('.button'),
    allChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

generator.addEventListener('click', generate);

function generate() {
    let newSerial = '',
        passwordLength = Math.floor(Math.random() * (20 - 10)) + 11
    for (let i = 0; i < passwordLength; i++) {
        newSerial += allChars[Math.floor(Math.random() * allChars.length)];
    }
    serial.textContent = newSerial;
    // serial.style.transitionDuration = '5s';
    // console.log(serial.style.transitionDuration);
    console.log(passwordLength)

}