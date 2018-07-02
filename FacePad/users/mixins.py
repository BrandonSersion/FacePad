class MixedPermissionModelMixin:
  """
  ModelMixin allowing for permission control by action.
  Subclasses may define permissions by creating a 
  'permission_classes_by_action' variable.

  Example:
  permission_classes_by_action = {
    'create': [IsAdminUser],
    'list': [IsUser],
    'retrieve': [AllowAny],
  }
  """
  permission_classes_by_action = {}

  def get_permissions(self):
    try:
      # return permission_classes depending on `action`
      return [permission() for permission in self.permission_classes_by_action[self.action]]
    except KeyError:
      # action is not set return default permission_classes
      return [permission() for permission in self.permission_classes]