from starkbank import request
from .base import Base
from ..checks import check_user


class GetPdf(Base):
    @classmethod
    def _pdf_endpoint(cls, id):
        return "{info_endpoint}/pdf".format(
            info_endpoint=cls._id_endpoint(id),
        )

    @classmethod
    def _get_pdf(cls, id, user=None):
        return request.get(
            user=check_user(user),
            endpoint=cls._pdf_endpoint(id),
        )
