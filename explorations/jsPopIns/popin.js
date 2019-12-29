var clickState = {};
var usePopIns = true
function anyElementClicked(){return(!Object.keys(clickState).every((k) => !clickState[k]))};

$(function() {
    $("#radio-popin-off").click(function(){
        usePopIns = false;
        console.log("off clicked, usePopIns is now " + usePopIns)
       })
    $("#radio-popin-on").click(function(){
        usePopIns = true;
        console.log(" on clicked, usePopIns is now " + usePopIns)
       })
    
    $(".annotationDiv").hide()
    $(".staticDiv")
        .mousedown(function(){
           var key = this.innerHTML
           var someOtherElementIsDisplayed = anyElementClicked() && !clickState[key];
           if(someOtherElementIsDisplayed) return;
           if(Object.keys(clickState).indexOf(key) < 0){
              clickState[key] = true;
              }
            else{
              console.log("inverting clickState")
              clickState[key] = !clickState[key]
              }
            console.log("clickState: " + clickState[key]);
            if(clickState[key]){
              $(this).css('background-color', "lightgray");
              $(this).css('border',  "1px solid red");
              }
            else{
              var infoBox = $(this).parent().siblings(".annotationDiv");
              infoBox.hide()
              $(this).css('background-color', "white");
              $(this).css('border',  "1px solid green");
              }
           console.log("click");
           console.log(key);
           })
        .mouseenter(function(){
           if(!usePopIns) return;
           if(!anyElementClicked()){
              var key = this.innerHTML
                // use this minimal event to initialize clickState
              if(Object.keys(clickState).indexOf(key) < 0){
                 clickState[key] = false;
                 }
              var moreInformation = lookup(this.innerHTML)
              window.x = moreInformation;
              var lineCount = moreInformation.split(/\r\n|\r|\n/).length;
              var infoBox = $(this).siblings(".annotationDiv");
              console.log("  infoBox: ");
              console.log(infoBox);
              $(this).css('background-color', "lightgray");
              infoBox.hide()
              console.log("--- about to display info, length: " + moreInformation.length)
              if(moreInformation.length > 0){    
                infoBox.css('height', (lineCount * 25) + 50);
                infoBox.show();
                infoBox.html(lookup(this.innerHTML));
                infoBox.focus();
                }
              }
           }) // mouseEnter
        .mouseleave(function(){
           if(!usePopIns) return;
           if(!anyElementClicked()){
               var key = this.innerHTML
               if(!clickState[key]){
                   $(this).css('background-color', "white");
                   var infoBox = $(this).siblings(".annotationDiv");
                   infoBox.hide()
               }
           } // !anyElementClicked
        }) // mouseleave
    }); // on ready

//------------------------------------------------------------------------------------------------------------------------
function lookup(morpheme)
{
   var found = Object.keys(kb).indexOf(morpheme) >= 0;
   console.log("---- lookup, using kb: '" + morpheme + "', found? " + found)
    
   if(Object.keys(kb).indexOf(morpheme) < 0)
       return("no annotation found")

    var result = kb[morpheme];
    return(result);

} // lookup
//------------------------------------------------------------------------------------------------------------------------


