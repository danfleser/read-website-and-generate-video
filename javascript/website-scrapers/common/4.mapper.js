const mapParagraphs = (e) => {
    // transform p children to only span text and strong elements
    // removed tags like em
    // text STRONG text => span STRONG span
    const children = [];
    let buffer = "";
    for (let i = 0; i < e.childNodes.length; i++) {
        const child = e.childNodes[i];
        // elements to keep
        if (["STRONG", "A"].includes(child.nodeName)) {
            if (buffer) {
                children.push(createSpan(buffer));
                buffer = "";
            }

            if (isLastChild(child)) {
                child.textContent += child.nextSibling.textContent;
                children.push(child);
                buffer = "";
                break;
            }

            children.push(child);
            // add href as string after text
            // so the user can see the url
            // if (child.nodeName === "A") {
            //     children.push(createElement(window.doNotReadTagName, `(${child.href})`));
            // }

            continue;
        }

        buffer += htmlToText(child.textContent);
    }
    if (buffer) {
        children.push(createSpan(buffer));
    }

    // splitting spans into smaller span elements
    // speech synthesis can read small sentences
    const sentenceElements = [];
    children.forEach(child => {
        if (child.nodeName === "SPAN") {
            const sentences = splitTextByDotAndComma(child.textContent);

            let buffer = "";
            sentences.forEach(sentence => {
                if (sentence.replace(/\s/g, '').length > 1) {
                    const span = document.createElement('span');
                    const text = document.createTextNode(buffer + sentence);
                    span.appendChild(text);

                    sentenceElements.push(span);
                    buffer = "";
                } else {
                    buffer += sentence;
                }
            });
        } else {
            // strong elements
            sentenceElements.push(child);
        }
    });

    // appending crated element to the DOM
    // by replacing innerHTML
    const sentencesElement = document.createElement(e.tagName);
    sentenceElements.forEach(element => sentencesElement.append(element));
    e.innerHTML = '';
    e.append(sentencesElement);

    return sentencesElement;
}