let table = document.getElementById("table")
onload = table.style.display = "none"

function searchBlog(){
    
    let filter = document.getElementById("filter").value.toUpperCase();
    let table = document.getElementById("table")
    let tr = table.getElementsByTagName("tr")

    

    for(var i = 0; i < tr.length; i++){
        let td = tr[i].getElementsByTagName("td")[0];


        if(td){
            let text_value = td.textContent || td.innerHTML;

            if(text_value.toUpperCase().indexOf(filter) > -1){
                table.style.display = "";
                tr[i].style.display = "";
            }
            else{
                
                tr[i].style.display = "none";
            }
            
            
        }
    }
}


   