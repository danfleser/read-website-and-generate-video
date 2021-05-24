const lastIndexOf = (list, tagName) => {
    let foundPos = 0;
    list.forEach((e, index) => {
        if (e.tagName.startsWith(tagName)) {
            foundPos = index;
        }
    })

    return foundPos;
}

const replaceAllOccurrences = (htmlElements, wordToReplace, skipWords) => {
    let elements = htmlElements;
    if (skipWords.length) {
        skipWords.forEach(word =>
            elements = elements.filter(e => e.innerHTML.indexOf(word) === -1)
        )
    }

    const replace = new RegExp(`${wordToReplace}`, 'gi');
    const replaceWith = "google";

    elements.forEach(e => e.innerHTML = e.innerHTML.replace(replace, replaceWith));
};

const htmlToText = (text) => text.replace(/<[^>]+>/g, '');

const splitTextByDotAndComma = (text) => text
    .replaceAll('. ', '. cox')
    .replaceAll(', ', ', cox')
    .replaceAll('? ', '? cox')
    .replaceAll('! ', '! cox')
    .replaceAll('- ', '- cox')
    .replaceAll('— ', '— cox')// long dash
    .replaceAll(': ', ': cox')
    .replaceAll('; ', '; cox')
    .replaceAll('(', '')
    .replaceAll(')', '')
    .split("cox")
    .filter(e => e !== '');

const createElement = (tag, text) => {
    const element = document.createElement(tag);
    const textNode = document.createTextNode(text);
    element.appendChild(textNode);

    return element;
}

const createSpan = (text) => {
    return createElement('span', text);
}

const isLastChild = (child) => {
    return child.nextSibling !== null
        && child.nextSibling.textContent.length === 1
        && child.nextSibling.nextSibling === null
}

class StopWatch {
    constructor() {
        this.startTime = new Date();
        // { id: { text: headingText, time: 00:01:30 } }
        this.headingTimes = {};
    }

    registerTime(id, text) {
        let timeDiff = new Date() - this.startTime;

        // strip the ms
        timeDiff /= 1000;
        // get seconds (Original had 'round' which incorrectly counts 0:28, 0:29, 1:30 ... 1:59, 1:0)
        let seconds = Math.round(timeDiff % 60);

        // remove seconds from the date
        timeDiff = Math.floor(timeDiff / 60);
        // get minutes
        let minutes = Math.round(timeDiff % 60);

        // remove minutes from the date
        timeDiff = Math.floor(timeDiff / 60);
        // get hours
        let hours = Math.round(timeDiff % 24);

        // register first occurrence
        if (this.headingTimes[id] === undefined) {
            this.headingTimes[id] = {
                text: text.replace('<', '').replace('>', ''),
                time: `${hours}:${minutes}:${seconds}`
            };
        }
    }

    getHeadingTimes() {
        return Object
            .keys(this.headingTimes)
            .map(key => this.headingTimes[key]);
    }
}

const playAudios = (sentences) => {
    const stopWatch = new StopWatch();

    const audios = [];
    sentences.forEach((sentencesElement, index) => {
        Array.from(sentencesElement.children)
            // ditch elements that we specified not to be read
            .filter(sentencesElement => sentencesElement.tagName !== window.doNotReadTagName)

            // creating audio sentences
            // initializing markJs for each sentence
            .forEach((sentenceElement, i) => {
                const msg = new SpeechSynthesisUtterance();
                msg.highlight = new Mark(sentenceElement)
                msg.text = sentenceElement.textContent;
                msg.onstart = () => {
                    if (i === 0) {
                        window.scrollToElement(sentenceElement);
                    }

                    // save read time for each paragraph so we have timing for youtube
                    if (sentencesElement.tagName.startsWith("H")) {
                        stopWatch.registerTime(index, sentenceElement.textContent);
                    }

                    msg.highlight.mark(msg.text, markJsOptions);
                }
                msg.onend = () => {
                    msg.highlight.unmark();

                    window.registerHeadingReadTimes(stopWatch.getHeadingTimes());
                }

                audios.push(msg)
            });
    });

    audios.forEach(msg => window.speechSynthesis.speak(msg));
}
