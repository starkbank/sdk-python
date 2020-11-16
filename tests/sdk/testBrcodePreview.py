import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBrcodePreviewGet(TestCase):

    def test_success(self):
        previews = list(starkbank.brcodepreview.query(brcodes=[
            "00020126580014br.gov.bcb.pix0136a629532e-7693-4846-852d-1bbff817b5a8520400005303986540510.005802BR5908T'Challa6009Sao Paulo62090505123456304B14A"
        ]))
        for preview in previews:
            print(preview)


if __name__ == '__main__':
    main()
