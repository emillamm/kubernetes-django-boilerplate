from rest_framework import generics, viewsets
from rest_framework.exceptions import APIException

from .serializers import BlogPostSerializer
from .models import BlogPost


class ViewValidationError(APIException):
    status_code = 400


class ViewDoesNotExistError(APIException):
    status_code = 404


class BlogPostViewSet(
        viewsets.GenericViewSet,
        generics.RetrieveAPIView, generics.ListAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.filter(draft=False)

    def get_object(self):
        slug = self.kwargs.get('pk', '')
        try:
            post = BlogPost.objects.get(slug=slug)
            if post.draft:
                raise ViewValidationError(detail='Post is in draft mode')
        except BlogPost.DoesNotExist:
            raise ViewDoesNotExistError(detail='Post does not exist')
        except ValueError:
            raise ViewValidationError(detail='Not a valid slug')
        return post
