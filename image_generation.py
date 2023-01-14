"""
A Simple Python Instruction Guide on how to use OpenAI API for Image Generation
"""

import openai, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ImageGenerator:
    
    __slots__ = [
        'IMAGE_HEIGHT',
        'IMAGE_WIDTH',
        'NO_OF_IMAGES_TO_GENERATE'
    ]
    
    def __init__(self):
        self.IMAGE_HEIGHT               = 1024
        self.IMAGE_WIDTH                = 1024
        self.NO_OF_IMAGES_TO_GENERATE   = 1
        openai.api_key                  = "" ## Your API key - Look at Instructions in README.md

    def generate_image(self, my_promt):
        try:
            response = openai.Image.create(
                prompt              = my_promt,
                n                   = self.NO_OF_IMAGES_TO_GENERATE,
                size                = f"{self.IMAGE_HEIGHT}x{self.IMAGE_WIDTH}"
            )
            image_url = response['data'][0]['url']
            print(f"[URL] Please go to the following URL to see your Generated Image: \n{bcolors.OKGREEN}{image_url}{bcolors.ENDC}")
        except Exception as e:
            sys.exit(f"Oops! Something went wrong while generating your image. \nError - {bcolors.FAIL}{e}{bcolors.ENDC}")


if __name__ == '__main__':
    ig = ImageGenerator()
    ig.generate_image(input("Describe your Image that you wish to be generated: "))

