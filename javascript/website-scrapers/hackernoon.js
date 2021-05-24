// SCRAPER hackernoon - https://hackernoon.com/
const body = document.querySelector("body");
const content = body.querySelector("[class^='Container-sc']");

// register init callbacks
const title = content.children[0].textContent
const thumbnailUrl = body.querySelector("[class^='FullScreenToggleImage']").children[0].children[0].src;
window.registerArticleTitle(title)
window.registerArticleThumbnailUrl(thumbnailUrl)

// set paragraphs
let paragraphs = Array.from(content.children);

cleanWebsite()

// replace all occurrences of website name with google
replaceAllOccurrences(
    paragraphs,
    "hackernoon",
    ["https://hackernoon.com/images", "https%3A%2F%2Fhackernoon.com%2Fimages"]
)


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
    body.classList = "";

    document.querySelectorAll("[class^='Reactions__Layout']").forEach(e => e.remove());
    document.querySelector("[class^='StoryMeta']").remove();
    document.querySelector("[class^='Profile__Layout']").remove();
    document.querySelector("header").remove();
    const postFooter = document.querySelector("footer");
    const bottomJunk0 = postFooter.previousElementSibling;
    const bottomJunk1 = bottomJunk0.previousElementSibling;
    const bottomJunk11 = bottomJunk1.previousElementSibling;
    if (bottomJunk11.tagName.indexOf("H")) {
        bottomJunk11.remove();
    }
    bottomJunk1.remove();
    bottomJunk0.remove();
    const bottomJunk2 = postFooter.nextElementSibling;
    const bottomJunk3 = bottomJunk2.nextElementSibling;
    bottomJunk3.nextElementSibling.remove();
    bottomJunk3.remove();
    bottomJunk2.remove();
    postFooter.remove();
    document.querySelector("footer").remove();

    document.querySelector("#iubenda-cs-banner").remove();

    document.querySelectorAll(".image-container").forEach(e => {
        e.appendChild(e.querySelector("img"));
        e.children[0].remove();
    })
    // --- END CLEAN CLUTTER ---
}