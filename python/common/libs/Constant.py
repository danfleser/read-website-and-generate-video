class Constant:
    """A class for storing constants for YoutubeUploader class"""
    YOUTUBE_URL = 'https://www.youtube.com'
    YOUTUBE_STUDIO_URL = 'https://studio.youtube.com'
    YOUTUBE_UPLOAD_URL = 'https://www.youtube.com/upload'
    USER_WAITING_TIME = 1
    VIDEO_TITLE = 'title'
    VIDEO_DESCRIPTION = 'description'
    VIDEO_THUMBNAIL = 'thumbnail_path'
    TEXTBOX = 'textbox'
    TEXT_INPUT = 'text-input'
    RADIO_LABEL = 'radioLabel'
    NEXT_BUTTON = 'next-button'
    PUBLIC_BUTTON = 'PUBLIC'
    VIDEO_URL_CONTAINER = "//span[@class='video-url-fadeable style-scope ytcp-video-info']"
    VIDEO_URL_ELEMENT = "//a[@class='style-scope ytcp-video-info']"
    HREF = 'href'
    UPLOADED = 'Upload complete'
    ERROR_SHORT_SELECTOR = '#dialog > div > ytcp-animatable.button-area.metadata-fade-in-section.style-scope.ytcp-uploads-dialog > div > div.left-button-area.style-scope.ytcp-uploads-dialog > div > div.error-short.style-scope.ytcp-uploads-dialog'
    ERROR_SHORT_XPATH = '//*[@id="dialog"]/div/ytcp-animatable[2]/div/div[1]/div/div[1]'
    UPLOADING_PROGRESS_SELECTOR = '#dialog > div > ytcp-animatable.button-area.metadata-fade-in-section.style-scope.ytcp-uploads-dialog > div > div.left-button-area.style-scope.ytcp-uploads-dialog > ytcp-video-upload-progress > span'
    DONE_BUTTON = 'done-button'
    INPUT_FILE_VIDEO = "//input[@type='file']"
    INPUT_FILE_THUMBNAIL = "//input[@id='file-loader']"
    TITLE_CONTAINER = "#container > #outer > #child-input > #input > #textbox"
    DESCRIPTION_CONTAINER = '.description-textarea > #container > #outer > #child-input > #input > #textbox'
    title_description_containers = '#container > #outer > #child-input > #input > #textbox'
    ERROR_CONTAINER = '//*[@id="error-message"]'
