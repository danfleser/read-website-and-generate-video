// ---- INIT ----

// -- mark.js --
// options
const markJsOptions = {
    "separateWordSearch": false,
    "each": (element) => {
        setTimeout(() => $(element).addClass("animate"), 250);
    },
    "acrossElements": true
}

// css
function addStyle(styles) {
    /* Create style document */
    var css = document.createElement('style');
    css.type = 'text/css';

    if (css.styleSheet)
        css.styleSheet.cssText = styles;
    else
        css.appendChild(document.createTextNode(styles));

    /* Append style to the tag name */
    document.getElementsByTagName("head")[0].appendChild(css);
}
var styles = `
    mark {
        padding: 5px;
        margin: -5px;
        border-radius: 5px;
        background: linear-gradient(to right, #5c2de1 50%, transparent 50%);
        background-position: right bottom;
        background-size: 200% 100%;
        transition: all 1s ease;
        color: black;
    }
    mark.animate {
        background-position: left bottom;
        color: white;
    }`;
addStyle(styles)
// -- END mark.js --

// ---- END INIT ----