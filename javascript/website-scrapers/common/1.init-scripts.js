// remove all click event listeners on page
window.addEventListener("click", function(event) {
    event.stopImmediatePropagation();
}, true);
// -- LOAD mark.js --
const markScript = document.createElement('script');
markScript.setAttribute('src', 'https://cdnjs.cloudflare.com/ajax/libs/mark.js/8.11.1/mark.min.js');
document.head.appendChild(markScript);
// -- LOAD jQuery.js --
const jqueryScript = document.createElement('script');
jqueryScript.setAttribute('src', "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js");
document.head.appendChild(jqueryScript);

// -- window extra props --
window.isSpeaking = () => window.speechSynthesis.speaking;
window.registerArticleTitle = (title) => {
    window.articleTitle = title;
}
window.registerArticleThumbnailUrl = (imageSrc) => {
    window.articleThumbnailUrl = imageSrc;
}
window.registerHeadingReadTimes = (headingTimes) => {
    window.headingTimes = headingTimes;
}
window.doNotReadTagName = 'COX';
window.scrollToElement = (element) => {
    window.scrollBy({
        top: element.getBoundingClientRect().top - window.innerHeight / 2,
        behavior: 'smooth'
    });
}