USER = 'user'
ADMIN = 'admin'
MODERATOR = 'moderator'
ROLE_CHOICES = (
    (USER, 'user'),
    (ADMIN, 'admin'),
    (MODERATOR, 'moderator'),
)
OPEN = 'open'
CLOSE = 'close'
ONLY_LOGIN = 'only_login'
VISIBILITY_CHOICES = (
    (OPEN, 'open'),
    (CLOSE, 'clise'),
    (ONLY_LOGIN, 'only_login'),
)
VISIBILITY_IN_GROUP_CHOICES = (
    (OPEN, 'open'),
    (ONLY_LOGIN, 'only_login'),
)
MAX_ROLE_LENGTH = max([len(role) for role, _ in ROLE_CHOICES])
MAX_VISIBILITY_LENGTH = max([len(visibl) for visibl, _ in VISIBILITY_CHOICES])
MAX_VISIBILITY_IN_GROUP_LENGTH = max(
    [len(visibl) for visibl, _ in VISIBILITY_IN_GROUP_CHOICES]
)
