from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404


class UserPermissionsMixin:
    def has_permissions(self):
        return self.get_object().author == self.request.user
        # return self.request.user in self.get_object().students.all()

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)
