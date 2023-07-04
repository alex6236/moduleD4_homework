const searchView = document.getElementById("search_view");
const searchBtn = document.getElementById("search_btn");

window.addEventListener("load", () => {
    searchView.style.display === "none";
});

searchBtn.addEventListener("click", () => {
        searchView.style.display = 
        searchView.style.display === "none" ?
        (searchView.style.display = "block") :
        (searchView.style.display = "block");
});

{/* <script>
    const searchView = document.getElementById("search_view");
    const searchBtn = document.getElementById("search_btn");
    
    window.addEventListener("load", (event) => {
        searchView.style.display = "none";
    }); 
    
    searchBtn.addEventListener("click", (event) => {
        event.preventDefault();
        searchView.style.display = searchView.style.display === "none" ? "block" : "none";
    });
</script> */}