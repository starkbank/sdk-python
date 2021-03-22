import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBrcodePreviewGet(TestCase):

    def test_success(self):
        previews = list(starkbank.brcodepreview.query(brcodes=[
            "00020126390014br.gov.bcb.pix0117valid@sandbox.com52040000530398654041.005802BR5908Jon Snow6009Sao Paulo62110507sdktest63046109"
        ]))
        for preview in previews:
            print(preview)


if __name__ == '__main__':
    main()
