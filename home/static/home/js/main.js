function setCurrent(index){
    var s = document.getElementById("navbar").getElementsByClassName("navbar-nav");
    var pages = [];
    for(var i=0;i<s.length;i++){
        for(var j=0;j<s[i].children.length;j++){
            if(s[i].children[j].textContent != "" && s[i].children[j].className != "dropdown"){
                pages.push(s[i].children[j]);
            }
        }
    }
    try {
        var x = document.createElement("SPAN");
        x.className = "sr-only";
        x.textContent = "(current)";
        pages[index].appendChild(x);
        pages[index].className = "active";
    } catch (e) {
        console.log("ERROR: NOT ON REGISTERED WEBPAGE");
    }
}
function checkCurrent(){
    var index = Number(document.getElementsByName("page_index")[0].content);
    setCurrent(index);
    if(document.getElementsByName("page_index")[0].content == "INDEX"){
        var x = document.createElement("div")
        x.style.background = "url(\"static/home/media/background.jpg\")";
        x.id = "backgroundImg"
        document.getElementById("main").appendChild(x);
    }
}
function setBrowserStyles(){
  var browser = navigator.userAgent.toLowerCase().indexOf('chrome') > -1 ? 'chrome' : 'other';
  if (browser == "chrome") {
    document.getElementById("main").style.height = "calc(100% - 120px)";
    $(window).on('resize',function(){
      document.getElementById("main").style.height = "calc(100% - 120px)";
    })
  }
  else{
    // for whatever reason firefox has trouble using calc()
    document.getElementById("main").style.height = (window.innerHeight - 120).toString() + "px";
    $(window).on('resize',function(){
      document.getElementById("main").style.height = (window.innerHeight - 120).toString() + "px";
    })
  }
}
$(document).ready(
    function(){
        checkCurrent();
        setBrowserStyles();
        var x = document.getElementsByClassName("fadein");
        for(var i=0;i<x.length;i++){
            if(x[i].dataset.fadetime !== undefined){
                var fadetime = Number(x[i].dataset.fadetime);
            }
            else{
               var fadetime = 1000;
            }
            if(x[i].dataset.fadewait !== undefined){
                var fadewait = Number(x[i].dataset.fadewait);
            }
            else{
                var fadewait = 0;
            }
            // tired, so I'm hardcoding this
            $(x[i]).hide();
            eval("setTimeout(function(){$(document.getElementsByClassName(\"fadein\")[" + i.toString() + "]).fadeIn(" + fadetime.toString() + ");}," + fadewait.toString() + ")")
        }
});