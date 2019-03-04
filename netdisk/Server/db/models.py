class BaseRole:
    def __init__(self, name, password):
        self.name = name
        self.password = password


class Admin(BaseRole):
    def __init__(self, name, password):
        BaseRole.__init__(self, name, password)


class User(BaseRole):
    def __init__(self, name, password, is_member=0):
        super().__init__(name, password)
        self.is_member = is_member


class File:
    def __init__(self, name, size, md5, path_in_server, uploaded_by=None):
        self.name = name
        self.size = size
        self.md5 = md5
        self.path_in_server = path_in_server
        self.uploaded_by = uploaded_by
