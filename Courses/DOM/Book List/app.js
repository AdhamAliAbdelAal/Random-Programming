class book
{
    constructor(title,author,isbn)
    {
        console.log(title.length);
        if(title.length==0)
        {
            title="Untitled";
        }
        if(author.length==0)
        {
            author="Unknown";   
        }
        if(isbn.length==0)
        {
            isbn="0";
        }
        this.title=title;
        this.author=author;
        this.isbn=isbn;
    }
}
class storage
{
    static getStoredBooks()
    {
        let booksTest =localStorage.getItem("books");
        if(booksTest)
        {
            return JSON.parse(booksTest);
        }
        else{
            localStorage.setItem('books','[]');
            return [];
        }
    }
    static addBook2Storage(book)
    {
        let books=JSON.parse(localStorage.getItem("books"));
        books.push(book);
        localStorage.setItem('books',JSON.stringify(books));
    }

    static deleteBookFromStorage(book)
    {
        let books=JSON.parse(localStorage.getItem("books"));
        console.log(books);
        for(let i=0;i<books.length;i++)
        {
            console.log(book);
            console.log(books[i]);
            if(books[i].title===book.title&& books[i].isbn===book.isbn&&books[i].author===book.author)
            {
                console.log(books.splice(i,1));
                console.log(1);
                break;
            }
        }
        console.log(books);
        localStorage.setItem('books',JSON.stringify(books));
    }
}
class UI
{
    static displayBooks()
    {
        const books=storage.getStoredBooks();
        console.log(books);
        books.forEach(b=>UI.addBook(b));
    }
    static addBook(book)
    {
        const body=document.querySelector("tbody");
        body.innerHTML+=
        `<tr>
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.isbn}</td>
            <td><button type="button" class="btn btn-danger btn-sm py-1 float-end">X</button></td>
        </tr>`;
    }
    static deleteBook(myBook)
    {
        const tr=myBook.parentElement.parentElement;
        let tdS=Array.from(tr.children);
        let sBook=new book (tdS[0].firstChild.textContent,tdS[1].firstChild.textContent,tdS[2].firstChild.textContent);
        storage.deleteBookFromStorage(sBook);
        tr.parentElement.removeChild(tr);
    }
}
document.addEventListener('DOMContentLoaded',UI.displayBooks);
document.querySelector("form").addEventListener('submit',(e)=>{
    e.preventDefault();
    const title=document.querySelector("#title");
    const author=document.querySelector("#author");
    const isbn=document.querySelector("#isbn");
    let myBook=new book(title.value,author.value,isbn.value);
    UI.addBook(myBook);
    storage.addBook2Storage(myBook);
    title.value='', author.value='', isbn.value='';
});
document.querySelector("table").addEventListener('click',e=>{
    if(e.target.tagName.toLowerCase()=="button")
    {
        UI.deleteBook(e.target);
    }
});
