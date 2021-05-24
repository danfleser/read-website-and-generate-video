// SCRAPER theverge - https://theverge.com/
const body = document.querySelector("body");
const content = body.querySelector("#content").children[0];

// register init callbacks
const title = content.querySelector(".c-page-title").textContent;
const thumbnailUrl = content.querySelector(".c-picture").querySelector("img").src;
window.registerArticleTitle(title)
window.registerArticleThumbnailUrl(thumbnailUrl)

// set paragraphs
let paragraphs = Array.from(content.querySelector('.c-entry-content').children);

cleanWebsite()

const sentences = paragraphs
    // read only following elements
    .filter(e => ['P', 'H4', 'H3', 'H2', 'BLOCKQUOTE', 'OL', 'UL'].includes(e.tagName))

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
    // remove bottom articles and comments
    content.children[0].remove();
    const div0 = content.lastElementChild;
    const div1 = div0.previousElementSibling;
    div1.remove();
    div0.remove();

    // header and footer
    const header = document.querySelector(".l-header");
    header.nextElementSibling.remove()
    header.remove()
    document.querySelector("footer").remove();

    // title extras
    const title_container = content.querySelector('.l-segment');
    title_container.children[1].remove();
    title_container.children[0].children[1].children[1].remove();
    title_container.children[0].children[3].remove();
    title_container.children[0].children[2].remove();
    title_container.children[0].children[0].remove();

    // ads sidebar
    const sidebar = content.querySelector('.l-col__sidebar');
    sidebar.remove();

    // top bar
    const topbar = body.querySelector('.c-tab-bar');
    topbar.remove();


    const paragraphs = content.querySelector('.l-col__main');
    paragraphs.querySelector('#formatter-datter').remove();
    paragraphs.querySelector('.c-nextclick').remove();
    paragraphs.querySelector('.e-image__meta').remove()

    const paragraphs_container = content.querySelector('.l-article-body-segment');
    paragraphs_container.style.display = "flex";
    paragraphs_container.style['justify-content'] = "center";
    paragraphs.style['max-width'] = "700px";

    const title_container_sty = content.querySelector('.c-entry-hero__header-wrap');
    title_container_sty.style.display = "flex";
    title_container_sty.style['justify-content'] = "center";
    title_container_sty.children[0].style['max-width'] = "700px";

    body.querySelector('.l-segment.l-main-content').style.margin = "0px";
    body.querySelector('#privacy-consent').remove();
    // --- END CLEAN CLUTTER ---
}