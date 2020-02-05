
//
// UPDATE articles
//     SET verified = Coalesce(verified, 0), 1
//     WHERE link ="chrome://extensions/";
//
// UPDATE articles
//     SET verified = CASE
//         WHEN verified IS NULL THEN 1
//         ELSE verified+
// WHERE link = 'chrome://extensions/' ;

$(document).ready (function () {
    var counter = 1;
    var urls = [];

    //put the url into the html prior to any functionality taking place
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
        var url = tabs[0].url;
        $("#pageUrl").html("<strong>Website URL:</strong>" + url);
    });


    //check if valid gets the url and then makes a get request to the chrome server to see if it is stored
    function checkIfValid() {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
            var url = tabs[0].url;

            url = "?link=" + url;
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "http://localhost:4499/get-fields" + url, false);
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4) {
                    console.log(xhr.responseText.length);

                    //if responseText is just an empty array, the url has not been evaluated yet
                    if (xhr.responseText.length <= 2) {
                        var opt = {
                            type: "basic",
                            title: "URL has not been evaluated yet",
                            message: "This page has not been verified/unverified by any other users. BE THE FIRST!",
                            iconUrl: "imgs/icon.png"
                        }
                        chrome.notifications.create('notEvaluated', opt, function () {
                        });
                    }
                    else {
                        // JSON.parse does not evaluate the attacker's scripts.
                        var res = JSON.parse(xhr.responseText);

                        var ver = res[0].verified;
                        var unver = res[0].unverified;
                        if (ver === undefined || ver === null || isNaN(ver)) {
                            console.log("verified undefined");
                            ver = 0;
                        }
                        else
                            var ver = res[0].verified;


                        if (unver === undefined || unver === null || isNaN(unver)) {
                            console.log("Unverified undefined");
                            unver = 0;
                        }
                        else
                            var unver = res[0].unverified;

                        var total = ver + unver;

                        var verifiedPercentage = ver / total;

                        console.log("Ver: " + ver + "\nUnver: " + unver + "\n" + "Total: " + total + "\n");
                        console.log(verifiedPercentage);

                        if (verifiedPercentage < .66) {
                            var opt = {
                                type: "basic",
                                title: "CAUTION: URL NOT VERIFIED",
                                message: "The website you are currently reading is not verified. It's information may not be valid.",
                                iconUrl: "imgs/icon.png"
                            }
                            chrome.notifications.create('invalidArticle', opt, function () {
                            });
                        }
                        if (verifiedPercentage >= .66) {
                            var opt = {
                                type: "basic",
                                title: "URL Verified",
                                message: "The URL you are currently on has been verified by our users, and has been deemed as a verified source.",
                                iconUrl: "imgs/icon.png"
                            }
                            chrome.notifications.create('invalidArticle', opt, function () {
                            });
                        }
                    }
                }
            }
            xhr.send();

        });
    }
    checkIfValid();

    $('#validStory').on('click', function () {

        chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
            var url = tabs[0].url;

            url = "?link=" + url;
            //
            //get the verified count
            var getVerifiedCount = new XMLHttpRequest();
            var verifiedCount;
            getVerifiedCount.open("GET", "http://localhost:4499/get-verified-count" + url, false);
            getVerifiedCount.onreadystatechange = function () {
                if (getVerifiedCount.readyState == 4) {
                    var res = JSON.parse(getVerifiedCount.responseText);
                    console.log(getVerifiedCount.responseText);

                    if(getVerifiedCount.responseText.length <= 2 || res[0].verified === null)
                        verifiedCount = 1;
                    else
                        verifiedCount = res[0].verified + 1;

                    console.log("Verified count: " + verifiedCount + "\n");
                }
            }
            getVerifiedCount.send();


            //check to see if the article is already in the database, if it is update the verified count
            //  If not add it and update the verified count
            var xhr = new XMLHttpRequest();
            xhr.open("GET", "http://localhost:4499/article-found" + url, false);
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4) {

                    console.log(xhr.responseText);

                    //the url has not been found inside of the database, so create a new row
                    if(xhr.responseText.length <= 2) {

                        var createRow = new XMLHttpRequest();
                        createRow.open("GET", "http://localhost:4499/insert-link" + url, false);
                        createRow.onreadystatechange = function () {
                            if (xhr.readyState == 4) { console.log(createRow.responseText) }
                        }
                        createRow.send();

                        //update the verified count now that the row is created in the database
                        var newXhr = new XMLHttpRequest();
                        var request = url + "&verified=" + verifiedCount;
                        newXhr.open("GET", "http://localhost:4499/update-verified-count" + request, false);
                        newXhr.onreadystatechange = function () {
                            console.log(newXhr.responseText);
                            if (newXhr.readyState == 4) {
                                console.log(newXhr.responseText);
                            }
                        }
                        newXhr.send();

                    }
                    else {
                        var newXhr = new XMLHttpRequest();
                        var request = url + "&verified=" + verifiedCount;
                        newXhr.open("GET", "http://localhost:4499/update-verified-count" + request, false);
                        newXhr.onreadystatechange = function () {
                            console.log(newXhr.responseText);
                            if (newXhr.readyState == 4) {
                                console.log(newXhr.responseText);
                            }
                        }
                        newXhr.send();
                    }
                }
            }
            xhr.send();
        });
        alert("Valid Submitted");
    });

    $('#invalidStory').on('click', function () {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
            var url = tabs[0].url;
            url = "?link=" + url;

            //get the unverified count
            var getUnverified = new XMLHttpRequest();
            var unverifiedCount;
            getUnverified.open("GET", "http://localhost:4499/get-unverified-count" + url, false);
            getUnverified.onreadystatechange = function () {
                if (getUnverified.readyState == 4) {
                    var res = JSON.parse(getUnverified.responseText);
                    console.log(getUnverified.responseText);
                    console.log(getUnverified.responseText.length);

                    if(getUnverified.responseText.length <=2 || res[0].unverified === null)
                        unverifiedCount = 1;

                    else
                        unverifiedCount = res[0].unverified + 1;

                    console.log("Unverified count: " + unverifiedCount + "\n");
                }
            }
            getUnverified.send();

            var xhr = new XMLHttpRequest();
            xhr.open("GET", "http://localhost:4499/article-found" + url, false);
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4) {

                    console.log(xhr.responseText);
                    //the url has not been found inside of the database, so create a new row
                    if(xhr.responseText.length <= 2) {

                        var createRow = new XMLHttpRequest();
                        createRow.open("GET", "http://localhost:4499/insert-link" + url, false);
                        createRow.onreadystatechange = function () {
                            if (xhr.readyState == 4) { console.log(createRow.responseText) }
                        }
                        createRow.send();

                        //update the verified count now that the row is created in the database
                        var newXhr = new XMLHttpRequest();
                        var request = url + "&unverified=" + unverifiedCount;
                        newXhr.open("GET", "http://localhost:4499/update-unverified-count" + request, false);
                        newXhr.onreadystatechange = function () {
                            console.log(newXhr.responseText);
                            if (newXhr.readyState == 4) {
                                console.log(newXhr.responseText);
                            }
                        }
                        newXhr.send();
                    }
                    else {

                        var newXhr = new XMLHttpRequest();
                        var request = url + "&unverified=" + unverifiedCount;
                        newXhr.open("GET", "http://localhost:4499/update-unverified-count" + request, false);
                        newXhr.onreadystatechange = function () {
                            console.log(newXhr.responseText);
                            if (newXhr.readyState == 4) {
                                console.log(newXhr.responseText);
                            }
                        }
                        newXhr.send();
                    }
                }
            }
            xhr.send();
        });
        alert("Invalid Submitted");

    });
});

