const depThreshold = 7;
let quote = "";

function showNotification() {
    let title = "Hello!";
    let body = quote;
    let icon = "extension/icon.png";
    var notification = new Notification(
        title,
        {
            body,icon
        });

    notification.onclick = () => {
        window.parent.focus();
        notification.close();
    }
}

setInterval(function() {
    chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
        function(tabs){
            fetch('http://127.0.0.1:5000/_get_url?url=' + encodeURIComponent(tabs[0].url))
                .then(r => r.json()).then(result => {
                    chrome.storage.local.set({"dep_pred": result.dep_pred}, function() {
                        console.log('Value is set to ' + result.dep_pred);
                    });
                    if (result.dep_pred > depThreshold) {
                        showNotification();
                    }
            })
        }
    );
}, 20000);

setInterval(() => {
    fetch('http://127.0.0.1:5000/_get_quote').then(r => r.json()).then(res => {
        quote = res.q + " - " + res.a;
    })
}, 15000);


