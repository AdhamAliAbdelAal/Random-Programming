async function get() {
    const response = await fetch("http://hp-api.herokuapp.com/api/characters/");
    const data = await response.json();
    console.log(data);
    let i = -1;
    arr = data.map(actor => {
        i = i + 1;
        return `<option value=${i}>${actor.name}</option>`;
    });
    console.log(arr);
    document.querySelector("#actor").innerHTML =
        `<select class="form-select">
    <option id="first" value="0">Choose Character</option>
    ${arr}
    </select>`;
    let sel = document.querySelector("select");
    sel.addEventListener("change", () => {
        let temp = data[sel.value];
        document.querySelector("#first").value = sel.value;
        let info = Object.entries(temp);
        let img = "";
        let output = info.map(inf => {
            if (inf[0] == "image") {
                img = `<div class="w-100 d-flex justify-content-center align-items-center"><img class="m-2 img-fluid" src="${inf[1]}" style="width:70%;" alt=""></div> `;
            } else {
                return `<tr><td>${inf[0]}</td><td>${inf[1]}</td></tr>`;
            }
        })
        document.querySelector("#data").innerHTML = `${img}<div class="container p-2"><table class="table table-light table-sm w-70">${output.join(' ')}</table></div>`;
    });
}
get();