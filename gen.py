from python.generator import WebsiteToVideoGenerator
from python.common.variables import js_scraper_freecodecamp, js_scraper_theverge, js_scraper_hackernoon, \
    js_scraper_stackoverflow

# 309424 how-do-…read-convert-an-inputstream-into-a-string-in-j mintul 11:40 aprox vezi ce se vede
articles = {
    "freecodecamp": {
        "scraper": js_scraper_freecodecamp,
        "urls": [

        ]
    },
    "hackernoon": {
        "scraper": js_scraper_hackernoon,
        "urls": [
            # "https://hackernoon.com/i-left-banking-for-tech-and-it-was-the-best-career-decision-ive-ever-made-2b9632uj",
            # "https://hackernoon.com/7-tips-for-becoming-a-better-javascript-developer-bw1w32mt",
            # "https://hackernoon.com/adding-multilanguage-support-to-cra-with-react-i18next-module-fe3832k4",
            # "https://hackernoon.com/the-fastest-ways-to-teach-yourself-javascript-jk3h33bh",
            # "https://hackernoon.com/how-to-scrape-almost-anything-with-puppeteer-and-nodejs-722333gv",
            # "https://hackernoon.com/the-abcs-of-javascript-apply-bind-and-call-up4c33ld",
            # "https://hackernoon.com/how-to-send-emails-with-nodejs-and-emailjs-module-dk1133dx",
            # "https://hackernoon.com/front-end-development-without-node_modules-using-skypack-and-snowpack-s03n33mk",
            # "https://hackernoon.com/how-can-developers-save-a-failing-project-learn-from-my-mistakes-l12a33f9",
            # "https://hackernoon.com/how-to-get-sslhttps-for-localhost-i11s3342",
            # "https://hackernoon.com/a-post-mortem-in-5-acts-how-microsoft-privatized-open-source-and-killed-javascript-in-the-process-5s5i33ma",
            # "https://hackernoon.com/how-to-track-user-navigation-events-in-a-react-application-8c2933w1",
            # "https://hackernoon.com/my-personal-plan-to-learn-the-whole-web-frontend-development-ecosystem-in-2021-rw3i334s",
            # "https://hackernoon.com/top-12-lesser-known-tips-for-javascript-best-practices-8t26335n",
            # "https://hackernoon.com/how-to-create-a-slick-ios-widget-in-javascript-e11p33t2",
            # "https://hackernoon.com/9-ways-to-up-your-code-game-with-javascript-7x2r33zs",
            # "https://hackernoon.com/heres-how-i-built-a-video-audio-and-screen-recorder-web-app-with-javascript-f42z338r",
            # "https://hackernoon.com/step-by-step-guide-to-create-3-different-types-of-loading-screens-in-react-lu2633nd",
            # "https://hackernoon.com/8-responsive-web-design-best-practices-to-know-in-2021-p38x33p1",
            # "https://hackernoon.com/the-complete-guide-using-to-selenium-locators-in-protractor-to-run-test-automation-with-scripts-6j7v35j8",
            # "https://hackernoon.com/is-it-easy-to-learn-java-if-you-already-know-javascript-py2i33qd",
            # "https://hackernoon.com/working-with-iterators-and-generators-in-javascript-es6-o23f35mj",
            # "https://hackernoon.com/the-advantages-of-using-nodejs-caching-scalability-and-a-rich-ecosystem-q23t33c1",
            # "https://hackernoon.com/everything-you-need-to-know-about-this-in-javascript-vo2933yg",
            # "https://hackernoon.com/how-to-create-a-simple-twitter-bot-using-nodejs-0g3b35x5",
            # "https://hackernoon.com/handling-nodejs-as-an-asynchronous-application-with-error-handling-hi3p355b",
            # "https://hackernoon.com/a-quick-guide-to-handling-expressjs-errors-in-your-application-ia3b331n",
            # "https://hackernoon.com/using-reactgrid-and-chartjs-to-create-a-financial-liquidity-planner-pj2733ke",
            # "https://hackernoon.com/what-does-serverless-mean-684o35dp",
            # "https://hackernoon.com/a-method-that-will-help-you-clone-netflix-with-micro-frontends-the-right-way-bes33jq",
            # "https://hackernoon.com/learning-duck-typing-in-javascript-qa3g35nc",
            # "https://hackernoon.com/improve-your-application-performance-with-react-hooks-7r3d35p1",
            # "https://hackernoon.com/5-easy-steps-to-create-a-react-project-with-serverless-user-authentication-vtr33tp",
            # "https://hackernoon.com/building-a-twitter-bot-with-nodejs-part-2-deploying-to-server-and-schedule-tweets-eb2a33nx",
            # "https://hackernoon.com/no-more-heavy-ram-memory-consumption-apply-these-3-secret-techniques-gwy33m0",
            # "https://hackernoon.com/step-by-step-tutorial-to-deploy-a-nodejs-app-to-kubernetes-f91b335h",
            # "https://hackernoon.com/how-to-manipulate-dom-elements-in-react-bo1733oo",
            # "https://hackernoon.com/velo-promises-in-action-key-tips-to-call-the-asynchronously-run-functions-y52633kd",
            # "https://hackernoon.com/insert-javascript-into-html-using-the-script-tag-u91k355d",
            # "https://hackernoon.com/what-is-local-storage-in-javascript-and-how-to-use-it-4q1033yv",
            # "https://hackernoon.com/creational-design-patterns-in-javascript-a-brief-tutorial-35w3304",
            # "https://hackernoon.com/how-to-manage-multithreaded-node-js-applications-for-better-performance-654t35od",
            # "https://hackernoon.com/the-wix-fetch-module-as-the-way-to-take-your-website-to-the-next-level-n31s33ig",
            # "https://hackernoon.com/mutability-and-immutability-in-javascript-explained-in-detail-x7q33ag",
            # "https://hackernoon.com/how-to-set-up-a-tsconfig-for-nodejs-2w1833jo",
            # "https://hackernoon.com/the-best-free-resources-to-learn-web-development-0bo334x",
            # "https://hackernoon.com/become-more-productive-as-a-developer-with-these-amazing-vs-code-extensions-ksp33rx",
            # "https://hackernoon.com/your-ultimate-guide-on-html-tags-qvq33ty",
            # "https://hackernoon.com/10-javascript-charting-libraries-data-visualization-b77523d23372",
            # "https://hackernoon.com/how-to-route-traffic-between-microservices-during-development-36183341",
            # "https://hackernoon.com/your-guide-to-learning-redux-r37e35sd",
            # "https://hackernoon.com/free-tools-that-will-help-you-grow-as-a-front-end-developer-in-2021-ssx334e",
            # "https://hackernoon.com/a-custom-chart-by-using-the-html-component-plainly-explained-1h1y33ix",
            # "https://hackernoon.com/building-blocks-of-dom-manipulation-vanilla-js-tutorial-part-one-dy54356y",
            # "https://hackernoon.com/lets-talk-about-vanilla-javascript-what-is-vanilla-js-and-why-should-i-spend-any-time-on-it-sb2f3522",
            # "https://hackernoon.com/what-i-learned-from-500-tech-interviews-in-the-last-65-years-b92d34io",
            # "https://hackernoon.com/how-to-build-a-passwordless-authentication-with-email-and-jwt-o33w3311",
            # "https://hackernoon.com/how-to-go-passwordless-with-idemeum-javascript-sdk-kk1l34v9",
            # "https://hackernoon.com/how-to-resize-an-image-correctly-in-javascript-4548336j",
            # "https://hackernoon.com/exploring-nodejs-event-loop-lr2b33qd",
            # "https://hackernoon.com/what-is-this-in-javascript-835o35kx",
            # "https://hackernoon.com/how-to-create-a-simple-mail-merge-script-with-google-apps-script-jls33c7",
            # "https://hackernoon.com/building-a-page-scroll-in-javascript-1j1g35y1",
            # "https://hackernoon.com/building-an-electron-app-with-net-js-html-and-css-1d1q34w9",
            # "https://hackernoon.com/how-to-setup-unit-tests-with-typescript-beginners-guide-kb27343u",
            # "https://hackernoon.com/how-to-test-an-app-that-using-redux-thunk-middleware-w22c34gd",
            # "https://hackernoon.com/building-react-applications-with-deno-and-alephjs-3m16342n",
            # "https://hackernoon.com/how-to-use-velo-and-wix-fetch-to-extend-your-website-functionality-ox12341b",
            # "https://hackernoon.com/how-to-build-a-reddit-clone-with-react-and-dgraph-cloud-8t15346j",
            # "https://hackernoon.com/react-vs-angular-final-thoughts-8bik3157"
        ]
    },
    "theverge": {
        "scraper": js_scraper_theverge,
        "urls": [
                ]
    },
    "stackoverflow": {
        "scraper": js_scraper_stackoverflow,
        "urls": [
            "https://stackoverflow.com/questions/309424/how-do-…read-convert-an-inputstream-into-a-string-in-java",
            "https://stackoverflow.com/questions/271526/avoiding-nullpointerexception-in-java",
            "https://stackoverflow.com/questions/40471/what-are…erences-between-a-hashmap-and-a-hashtable-in-java",
            "https://stackoverflow.com/questions/157944/create-arraylist-from-array",
            "https://stackoverflow.com/questions/13375357/proper-use-cases-for-android-usermanager-isuseragoat",
            "https://stackoverflow.com/questions/8710619/why-do…vas-compound-assignment-operators-require-casting",
            "https://stackoverflow.com/questions/363681/how-do-…e-random-integers-within-a-specific-range-in-java",
            "https://stackoverflow.com/questions/8881291/why-is-char-preferred-over-string-for-passwords",
            "https://stackoverflow.com/questions/46898/how-do-i-efficiently-iterate-over-each-entry-in-a-java-map",
            "https://stackoverflow.com/questions/1066589/iterate-through-a-hashmap",
            "https://stackoverflow.com/questions/6470651/how-can-i-create-a-memory-leak-in-java",
            "https://stackoverflow.com/questions/215497/what-is…n-public-protected-package-private-and-private-in",
            "https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do",
            "https://stackoverflow.com/questions/419163/what-does-if-name-main-do",
            "https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator",
            "https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python",
            "https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions",
            "https://stackoverflow.com/questions/38987/how-do-i…s-in-a-single-expression-taking-union-of-dictiona",
            "https://stackoverflow.com/questions/89228/how-to-e…te-a-program-or-call-a-system-command-from-python",
            "https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory",
            "https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops",
            "https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists",
            "https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod",
            "https://stackoverflow.com/questions/509211/understanding-slice-notation",
            "https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list",
            "https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method",
            "https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops",
            "https://stackoverflow.com/questions/7074/what-is-the-difference-between-string-and-string-in-c",
            "https://stackoverflow.com/questions/105372/how-to-enumerate-an-enum",
            "https://stackoverflow.com/questions/29482/how-can-i-cast-int-to-enum",
            "https://stackoverflow.com/questions/444798/case-insensitive-containsstring",
            "https://stackoverflow.com/questions/141088/what-is-the-best-way-to-iterate-over-a-dictionary",
            "https://stackoverflow.com/questions/247621/what-are-the-correct-version-numbers-for-c",
            "https://stackoverflow.com/questions/78536/deep-cloning-objects",
            "https://stackoverflow.com/questions/136035/catch-multiple-exceptions-at-once",
            "https://stackoverflow.com/questions/472906/how-do-…representation-of-strings-in-c-sharp-without-manu",
            "https://stackoverflow.com/questions/125319/should-…ing-directives-be-inside-or-outside-the-namespace",
            "https://stackoverflow.com/questions/2706500/how-do-i-generate-a-random-int-number",
            "https://stackoverflow.com/questions/40730/what-is-…-to-give-a-c-sharp-auto-property-an-initial-value",
            "https://stackoverflow.com/questions/943398/get-int-value-from-enum-in-c-sharp",
            "https://stackoverflow.com/questions/9/how-do-i-cal…te-someones-age-based-on-a-datetime-type-birthday",
            "https://stackoverflow.com/questions/151005/how-do-…s-and-xlsx-file-in-c-sharp-without-installing-mic"
        ]
    }
}
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# url ='http://www.websiteaddress.com'
# data = urlopen(url)
# soup = BeautifulSoup(data, 'html.parser')
# result = soup.find('title')
# print(result.get_text())
# # Array.from(document.querySelectorAll('#mainbar .question-hyperlink')).map(e => e.href)
# for link in upcoming_events_div.select('div.title a[href]'):
#     print link['href']

for article in articles:
    webiste = articles[article]

    urls = webiste['urls']
    scraper = webiste['scraper']

    if len(urls) > 0:
        for link in urls:
            WebsiteToVideoGenerator(link, scraper).generate_video()
