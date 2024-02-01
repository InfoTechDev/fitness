from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.response import Response


class BaseResponse:

    def __init__(self):
        self.data = []
        self.meta = []
        self.status = 200
        self.message = ""
        self.success = False
        self.pagination = {"total": 0, 'total_pages': 0}

    def get_data(self):
        return self.data

    def paginate(self, request, query):

        page = request.GET.get('page', 1)
        item_num = request.GET.get('num_item_in_page', 200)
        paginator = Paginator(query, item_num)

        try:
            if page == "-1":
                self.data = paginator.page(paginator.num_pages).object_list
            else:
                self.data = paginator.page(page).object_list

        except PageNotAnInteger:
            self.data = paginator.page(1).object_list
        except EmptyPage:
            page = []

        self.pagination.update({
            "page": page,
            "total": paginator.count,
            "total_pages": paginator.num_pages,
            "per_page": item_num
        })
        return self

    def collect(self, data={}, is_paginated=False):

        for key, values in data.items():
            if key == "message":
                self.message = values

            elif key == 'status':
                if values >= 200 and values < 300:
                    self.success = True
                self.status = values

            elif key == 'data':
                self.data = values

        return self.format(is_paginated)

    def format(self, is_paginated):
        response = {}
        if is_paginated:
            response = {'data': {
                'items': self.data,
                "total": self.pagination["total"],
                "total_pages": self.pagination["total_pages"],
            }}
        else:
            if isinstance(self.data, dict):
                response = {'data': self.data}
            else:
                response = {'data': {'items': self.data}}
        response.update({'meta': {
            "success": self.success,
            "status": self.status,
            "message": self.message,
        }})
        return Response(response, self.status)
