function moveRightAjax(value){
    req = $.ajax({
            url : '/_moveright',
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: "json",
            data : JSON.stringify({ 'index' : value})
        })
    
        req.done(function() {
            $("#add-loc").load(location.href + " #add-loc");
        });
};

function moveLeftAjax(value){
    req = $.ajax({
            url : '/_moveleft',
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: "json",
            data : JSON.stringify({ 'index' : value})
        })
    
        req.done(function() {
            $("#add-loc").load(location.href + " #add-loc");
        });
};

function removeAjax(value){
    req = $.ajax({
            url : '/_remove',
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: "json",
            data : JSON.stringify({ 'index' : value})
        })
        
        req.done(function() {
            $("#cards-loc").load(location.href + " #cards-loc");
            $("#add-loc").load(location.href + " #add-loc");
            
        });
};

function addAjax(value){
    req = $.ajax({
            url : '/_add',
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: "json",
            data : JSON.stringify({ 'card_id' : value})
        })
        
        req.done(function() {
            $("#cards-loc").load(location.href + " #cards-loc");
            $("#add-loc").load(location.href + " #add-loc");
            
        });
};


function searchAjax(){
    var searchText = document.getElementById('searchtext').value;
    req = $.ajax({
            url : '/_search',
            type: 'POST',
            contentType: 'application/json;charset=UTF-8',
            dataType: "json",
            data : JSON.stringify({ 'search_text' : searchText})
        })
        
        req.done(function() {
            $("#cards-loc").load(location.href + " #cards-loc");
            $("#search-loc").load(location.href + " #search-loc");
            
        });
};

function resetAjax(){
    req = $.ajax({
            url : '/_reset',
            type: 'POST',

        })
        
        req.done(function() {
            $("#cards-loc").load(location.href + " #cards-loc");
            $("#search-loc").load(location.href + " #search-loc");
            
        });
};

function consolelog(){
    console.log('clicked')
    
};

function showDecks(){
    req = $.ajax({
        url : '/_showdecks',
        type: 'POST',       
    })
    
    req.done(function() {
        $("#radio-buttons").load(location.href + " #radio-buttons");
        
    });
    
};

function hideDecks(){
    req = $.ajax({
        url : '/_hidedecks',
        type: 'POST',
    })
    
    req.done(function() {
        $("#radio-buttons").load(location.href + " #radio-buttons");
        
    });
    
};

function showAjax(value){
    req = $.ajax({
        url : '/_show',
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        dataType: "json",
        data : JSON.stringify({ 'deck_id' : value})

    })
    
    req.done(function() {
        $("#cards-loc").load(location.href + " #cards-loc");
        $("#add-loc").load(location.href + " #add-loc");
        $("#save-loc").load(location.href + " #save-loc");
        $("#name-loc").load(location.href + " #name-loc");

        element = document.getElementById("name-loc")
        element.scrollIntoView();

        
        
    });
    
};

function duplicateAjax(value){
    req = $.ajax({
        url : '/_duplicate',
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        dataType: "json",
        data : JSON.stringify({ 'deck_id' : value})

    })
    
    req.done(function() {
        $("#cards-loc").load(location.href + " #cards-loc");
        $("#add-loc").load(location.href + " #add-loc");
        $("#save-loc").load(location.href + " #save-loc");
        $("#name-loc").load(location.href + " #name-loc");

        element = document.getElementById("name-loc")
        element.scrollIntoView();
    });
    
};

function deleteAjax(value){  

    req = $.ajax({
        url : '/_delete',
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        dataType: "json",
        data : JSON.stringify({ 'deck_id' : value })

    })
    
    req.done(function() {
        $("#save-loc").load(location.href + " #save-loc");
        
    });    

};

function saveAjax(){

    let nameText = document.getElementById('nametext').value;
    
    

    req = $.ajax({
        url : '/_save',
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        dataType: "json",
        data : JSON.stringify({ 'deck_name' : nameText })

    })
    
    req.done(function() {
        $("#cards-loc").load(location.href + " #cards-loc");
        $("#add-loc").load(location.href + " #add-loc");
        $("#name-loc").load(location.href + " #name-loc");
        $("#save-loc").load(location.href + " #save-loc");
        
    });
    
};

function updateAjax(){

    let nameText = document.getElementById('nametext').value;

    

    req = $.ajax({
        url : '/_update',
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        dataType: "json",
        data : JSON.stringify({ 'deck_name' : nameText  })

    })
    
    req.done(function() {
        $("#cards-loc").load(location.href + " #cards-loc");
        $("#add-loc").load(location.href + " #add-loc");
        $("#name-loc").load(location.href + " #name-loc");
        $("#save-loc").load(location.href + " #save-loc");
        
    });
    
};

function cancelAjax(){

    req = $.ajax({
        url : '/_cancel',
        type: 'POST',
    })
    
    req.done(function() {
        $("#cards-loc").load(location.href + " #cards-loc");
        $("#add-loc").load(location.href + " #add-loc");
        $("#name-loc").load(location.href + " #name-loc");
        $("#save-loc").load(location.href + " #save-loc");
        
    });
    
};

function showSupplyAjax(){

    req = $.ajax({
        url : '/_showsupply',
        type: 'POST',
    })
    
    req.done(function() {       
        $("#add-loc").load(location.href + " #add-loc");
        $("#name-loc").load(location.href + " #name-loc");
        
    });
    
};

function hideSupplyAjax(){

    req = $.ajax({
        url : '/_hidesupply',
        type: 'POST',
    })
    
    req.done(function() {       
        $("#add-loc").load(location.href + " #add-loc");
        $("#name-loc").load(location.href + " #name-loc");
        
    });
    
};



