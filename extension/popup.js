setInterval(function() {
    chrome.storage.local.get(["dep_pred"], function(val) {
        console.log(val);
        document.getElementsByClassName("text-1")[0].innerHTML = val["dep_pred"];
        document.getElementsByClassName("text-1")[0].style.left = (6+23.4*parseInt(val["dep_pred"])).toString() + "px";
        document.getElementsByClassName("image-4")[0].style.left = (-17+23.4*parseInt(val["dep_pred"])).toString() + "px";
        document.getElementsByClassName("ellipse-6")[0].style.left = (-17+23.4*parseInt(val["dep_pred"])).toString() + "px";
    });
}, 20);
