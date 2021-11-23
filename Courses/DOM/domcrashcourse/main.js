let form=document.querySelector("#addForm");
let list=document.querySelector("ul");
let filter=document.querySelector("#filter");
function addItem(e)
{
    let item=document.querySelector('#item').value;
    if(item.length>0)
    {
        let listItem=`<li class="list-group-item">${item} <button class="btn btn-danger btn-sm float-right delete">X</button></li>`;
        list.innerHTML+=listItem;
    }
    e.preventDefault();
    filterItems(e);
}
function removeItem(e)
{
    if(e.target.tagName=="button".toLocaleUpperCase())
    {
        let li=e.target.parentElement;
        list.removeChild(li);
    }
}
function filterItems(e)
{
    let text=filter.value.toLowerCase();
    let lis=Array.from(list.children);
    lis.forEach(li=>{
        let itemText=li.firstChild.textContent.toLowerCase();
        let space100 =' '.repeat(100);
        if((space100+itemText+space100).indexOf(text)==-1)
        {
            li.style.display='none';
        }
        else
        {
            li.style.display='block';
        }
    })
}
form.addEventListener('submit',addItem);
list.addEventListener('click',removeItem);
filter.addEventListener('keyup',filterItems);
