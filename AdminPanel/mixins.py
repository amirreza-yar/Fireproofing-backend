from django.http import Http404
class SuperuserMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(SuperuserMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404("permission denied")

class CategoryMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.category_access:
            return super(CategoryMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404("permission denied")

class ProductMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.product_access:
            return super(ProductMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404("permission denied")

class BlogMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.blog_access:
            return super(BlogMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404("permission denied")
