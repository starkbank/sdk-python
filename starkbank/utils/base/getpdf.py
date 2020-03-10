from starkbank import request
from .base import Base


class GetPdf(Base):
    @classmethod
    def _pdf_endpoint(cls, id):
        return "{info_endpoint}/pdf".format(
            info_endpoint=cls._id_endpoint(id),
        )

    @classmethod
    def _get_pdf(cls, id, user=None):
        return request.get(
            user=user,
            endpoint=cls._pdf_endpoint(id),
        )
