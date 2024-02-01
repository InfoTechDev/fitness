import traceback

from django.db import IntegrityError
from django.http import Http404
from rest_framework import exceptions
from rest_framework import status
from rest_framework.exceptions import NotFound, MethodNotAllowed
from rest_framework.exceptions import ValidationError, PermissionDenied

from fitness_training_project.micro_services.base.core.responses.base_response import BaseResponse


class ErrorHandler:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.response = BaseResponse()

    def handle_exception(self, e, specific_error_pos=True):
        if isinstance(e, Http404):
            return self.response.collect(
                {'message': "This Endpoint not found", "status": status.HTTP_404_NOT_FOUND})

        if isinstance(e, (ModuleNotFoundError, NotFound)):
            return self.response.collect(
                {'message': str(e), "status": status.HTTP_404_NOT_FOUND})

        elif isinstance(e, ValidationError):
            return self.response.collect(
                {'message': self.get_message_for_specified_item(e.detail, specific_error_pos),
                 "status": status.HTTP_400_BAD_REQUEST})

        elif isinstance(e, ValueError):
            return self.response.collect(
                {'message': str(e), "status": status.HTTP_400_BAD_REQUEST})

        elif isinstance(e, (exceptions.NotAuthenticated,
                            exceptions.AuthenticationFailed)):
            return self.response.collect(
                {'message': 'Authentication credentials were not provided.', "status": status.HTTP_401_UNAUTHORIZED})

        elif isinstance(e, PermissionDenied):
            return self.response.collect(
                {'message': str(e), "status": status.HTTP_403_FORBIDDEN})

        elif isinstance(e, IntegrityError):
            return self.response.collect(
                {'message': str(e), "status": status.HTTP_400_BAD_REQUEST})

        elif isinstance(e, MethodNotAllowed):
            return self.response.collect(
                {'message': str(e), "status": status.HTTP_405_METHOD_NOT_ALLOWED})

        else:
            # print(e)
            traceback.print_exc()
            message = 'Something Went Wrong'
            return self.response.collect(
                {'message': message, "status": status.HTTP_500_INTERNAL_SERVER_ERROR})
