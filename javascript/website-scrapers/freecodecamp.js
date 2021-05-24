// SCRAPER freecodecamp - https://www.freecodecamp.org/
const post = document.querySelector(".post-full")

// register init callbacks
const title = post.querySelector(".post-full-title").textContent
const thumbnailUrl = post.querySelector(".post-full-image").children[0].src;
window.registerArticleTitle(title)
window.registerArticleThumbnailUrl(thumbnailUrl)

// set paragraphs
const content = post.querySelectorAll(".post-content")
let paragraphs = Array.from(content[0].children);

cleanWebsite()

// replace all occurrences of website name with google
replaceAllOccurrences(
    paragraphs,
    "freecodecamp",
    ["https://www.freecodecamp.org/news/content/images"]
)


const sentences = paragraphs
    // read only following elements
    .filter(e => ['P', 'H4', 'H3', 'H2', 'BLOCKQUOTE', 'OL', 'UL'].includes(e.tagName))

    // ditch elements that have math elements inside
    //ADD HERE MULTIPLE ELEMENT TAGS LIKE "match"
    .filter(e => e.innerHTML.indexOf("math") === -1)

    // start mapping
    .map(mapParagraphs);

playAudios(sentences);


function cleanWebsite() {
    // --- CLEAN CLUTTER ---
    // remove top header
    document.querySelector(".banner").remove()
    document.querySelector(".site-nav.nav-padding").remove()
    document.querySelector(".post-full-meta").remove()
    // clean authors
    document.querySelectorAll(".post-full-author-header").forEach(e => e.remove())
    // remove social bottom links
    document.querySelector(".social-row").previousElementSibling.remove()
    document.querySelector(".social-row").remove()
    // remove freecodecamp bottom links
    document.querySelector(".learn-cta-row").previousElementSibling.remove()
    document.querySelector(".learn-cta-row").remove()
    // remove freecodecamp footer
    document.querySelector(".site-footer").remove()
    // remove last author paragraphs
    const authorConclusionParagraphIndex = lastIndexOf(paragraphs, "H");
    if (authorConclusionParagraphIndex > 2) {
        paragraphs.slice(authorConclusionParagraphIndex, paragraphs.length)
            .forEach(e => e.remove())
        paragraphs = paragraphs.slice(0, authorConclusionParagraphIndex);
    }
    // --- END CLEAN CLUTTER ---
}