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
    console.log(searchText)
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

function showDecks(value){
    req = $.ajax({
        url : '/_showdecks',
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        dataType: "json",
        data : JSON.stringify({ 'user' : value})

    })
    
    req.done(function() {
        $("#radio-buttons").load(location.href + " #radio-buttons");
        
    });
    
};

function hideDecks(value){
    req = $.ajax({
        url : '/_hidedecks',
        type: 'POST',
        contentType: 'application/json;charset=UTF-8',
        dataType: "json",
        data : JSON.stringify({ 'user' : value})

    })
    
    req.done(function(value) {
        $("#radio-buttons").load(location.href + " #radio-buttons");
        
    });
    
};



