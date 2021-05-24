// SCRAPER stackoverflow - https://stackoverflow.com/
const body = document.querySelector("body");
const content = body.querySelector("#content").children[0];

// register init callbacks
const title = content.querySelector("#question-header h1 a").textContent;
window.registerArticleTitle(title)
window.registerArticleThumbnailUrl('')


cleanWebsite()

// set paragraphs
let paragraphs = [];
// add title to read
paragraphs.push(content.querySelector("#question-header h1 a"))
// add question to read
const mainbar = content.querySelector('#mainbar');
paragraphs.push(document.querySelector('.question .js-post-body'))
// add answers to read
mainbar.querySelectorAll('.s-prose').forEach(e => {
    Array.from(e.children).forEach(c => paragraphs.push(c));
})


const sentences = paragraphs
    // read only following elements
    .filter(e => ['P', 'H6', 'H5', 'H4', 'H3', 'H2', 'H1', 'BLOCKQUOTE', 'OL', 'UL'].includes(e.tagName))

    // ditch elements that have math elements inside
    //ADD HERE MULTIPLE ELEMENT TAGS LIKE "math"
    .filter(e => e.innerHTML.indexOf("math") === -1)
    // ditch code elements
    .filter(e => !e.classList.contains("code-container"))

    // start mapping
    .map(mapParagraphs);

playAudios(sentences);


function cleanWebsite() {
    // --- CLEAN CLUTTER ---
    body.style['padding-top'] = "0px";
    body.querySelector('#content').style['border'] = '0px';
    const container = body.querySelector('.container');
    container.style.display = "flex";
    container.style['justify-content'] = "center";


    const content_container = body.querySelector('#mainbar');
    content_container.style.width = 'unset';

    document.querySelectorAll('.js-post-comments-component').forEach(e => e.remove())
    document.querySelectorAll('.mt24').forEach(e => e.remove())
    document.querySelector('.answers-subheader').children[1].remove()
    document.querySelector('.question .post-layout .mb0').remove()
    document.querySelector('#question-header').children[1].remove()
    Array.from(document.querySelector('#content .inner-content .grid').nextElementSibling.children)
        .forEach(e => e.remove())

    body.querySelector('header').remove();
    body.querySelector('footer').remove();
    body.querySelector('.bottom-notice').remove();
    body.querySelectorAll('.s-pagination').forEach(e => e.remove());
    body.querySelector('.s-notice').remove();
    body.querySelector('.js-consent-banner').remove();
    body.querySelector('.js-dismissable-hero').remove();
    body.querySelector('#sidebar').remove();
    body.querySelector('#left-sidebar').remove();
    document.querySelector('.js-zone-container').remove()
    // --- END CLEAN CLUTTER ---
}