from rest_framework.permissions import SAFE_METHODS, BasePermission


class CanUseTicketPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.has_perm('ticket.can_mark_used_ticket')
