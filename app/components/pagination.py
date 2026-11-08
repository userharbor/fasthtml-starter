from fasthtml.common import FT
from fasthtml_basecoat import Pagination as BasePagination
from fasthtml_basecoat import PaginationLink


def Pagination(page: int, total_pages: int) -> FT | None:
    return (
        BasePagination(
            PaginationLink("Previous", href=f"?page={page - 1}") if page > 1 else None,
            *(
                PaginationLink(
                    str(number), href=f"?page={number}", current=number == page
                )
                for number in range(1, total_pages + 1)
            ),
            PaginationLink("Next", href=f"?page={page + 1}")
            if page < total_pages
            else None,
        )
        if total_pages > 1
        else None
    )
