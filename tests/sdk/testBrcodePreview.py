import starkbank
from unittest import TestCase, main
from tests.utils.user import exampleProject


starkbank.user = exampleProject


class TestBrcodePreviewGet(TestCase):

    def test_success(self):
        previews = list(starkbank.brcodepreview.query(brcodes=[
            "00020101021226890014br.gov.bcb.pix2567invoice-h.sandbox.starkbank.com/v2/d5b00b1994454706ba90a0387ff39b7952040000530398654040.005802BR5925Afel Tec Servicos Adminis6009Sao Paulo62070503***630475CE"
        ]))
        for preview in previews:
            print(preview)


if __name__ == '__main__':
    main()
