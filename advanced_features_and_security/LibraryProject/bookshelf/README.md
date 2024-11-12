# Permissions and Groups Setup

This document describes the permissions and groups setup in the application.

### Custom Permissions
We have defined custom permissions on the `Document` model:
- `can_view`: Allows viewing documents.
- `can_create`: Allows creating new documents.
- `can_edit`: Allows editing existing documents.
- `can_delete`: Allows deleting documents.

### Groups
The following groups have been created:
- **Viewers**: Access to view documents.
- **Editors**: Access to view, create, and edit documents.
- **Admins**: Full access (view, create, edit, delete).

### Usage in Views
Each view is protected by specific permissions using Django's `@permission_required` decorator or `PermissionRequiredMixin` for class-based views.

For further details, check `views.py` and `models.py`.

