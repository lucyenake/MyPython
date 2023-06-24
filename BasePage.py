from pytesseract import pytesseract, Output
from PIL import Image
import sys


# Check the number of arguments
if len(sys.argv) < 2:
    print("Please provide an argument.")
    sys.exit(1)
# Read the argument
bigScreenshot = sys.argv[1]
searchingWord = "Fahrzeug"

class BasePage:
    def image_as_data(self, img: str, show_f: bool = False):
        img = Image.open(img)
        if show_f:
            img.show()
        image_data = pytesseract.image_to_data(img, lang='eng', output_type=Output.DICT)
        return image_data

    def check_text_element_is_present(self, text: str, page_elements: list):
        assert any(x for x in page_elements if text in x)

    def getcoordinats(self, text: str, image_with_buttons: dict):
        for word in image_with_buttons['text']:
            if text in word:
                index = word.index(text)
                left = image_with_buttons['left'][index]
                top = image_with_buttons['top'][index]
                width = image_with_buttons['width'][index]
                height = image_with_buttons['height'][index]
                result_left = left + round(width / 2)
                result_top = top + round(height / 2)
                print(f'Coordinates of the center of the word {word} are: {result_left},{result_top}')

                break


if __name__ == '__main__':
    page = BasePage()

    #searchingWord = page.image_as_data(word, show_f=True)

    mainScreenshot = page.image_as_data(bigScreenshot, show_f=True)

    page.getcoordinats(text=searchingWord, image_with_buttons=mainScreenshot)


    page.check_text_element_is_present(searchingWord, mainScreenshot['text'])


