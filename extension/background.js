
var intervalId = setInterval(function() {
    chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
        function(tabs){
            // alert("/_get_url/" + encodeURIComponent(tabs[0].url) + "");
            fetch('http://127.0.0.1:5000/_get_url?url=' + encodeURIComponent(tabs[0].url))
                .then(r => r.text()).then(result => {
                console.log(result);
            })
        }
    );
}, 5000);



