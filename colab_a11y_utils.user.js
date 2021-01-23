// ==UserScript==
// @name         colab-a11y-utils
// @namespace    https://github.com/hassaku/colab-a11y-utils
// @version      0.1
// @description  improve Google Colab accessesibility
// @author       hassaku
// @match        https://colab.research.google.com/*
// @grant        none
// ==/UserScript==

function say(utterance) {
    window.speechSynthesis.cancel();
    let msg = new SpeechSynthesisUtterance(utterance);
    msg.lang = "en-US";
    window.speechSynthesis.speak(msg);
}

(function() {
    'use strict';

    window.onload = function(){
        window.setInterval(function(){
            // Skip unnecessary focuses.
            for (var toolbar of window.document.getElementsByTagName("colab-cell-toolbar")) {
                toolbar.setAttribute('aria-hidden', true);
            }

            for (var outputInfo of window.document.getElementsByClassName("output-info")) {
                outputInfo.setAttribute('aria-hidden', true);
            }

            for (var cellExcecution of window.document.getElementsByClassName("cell-execution-container")) {
                cellExcecution.setAttribute('aria-hidden', true);
            }

            for (var cell of window.document.getElementsByClassName("cell")) {
                cell.removeAttribute('tabindex');
            }
        }, 1000);
    }

    // Voice notification of whether the current cell is running or not
    document.addEventListener('keydown', function (e) {
        if (event.ctrlKey && event.key === "q") {
            for (var runButton of document.querySelectorAll("colab-run-button")) {
                let div = runButton.shadowRoot.querySelector("div");

                if (div.classList.contains("focused")) {
                    if (div.classList.contains("running")) {
                        say("Running now. To force sto p, press Ctrl + M followed by I");
                    } else if (div.classList.contains("error")) {
                        say("Error on last run");
                    } else if (div.querySelector("div > div.execution-count").innerText === "[ ]") {
                        say("Not executed in the current session");
                    } else {
                        say("Executed");
                    }
                }
            }
        }
    }, false);
})();
