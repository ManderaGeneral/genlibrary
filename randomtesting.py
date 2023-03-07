
from generalpackager import Packager

# genlibrary = Packager("genlibrary")

# print(list(genlibrary.localrepo.list_packages()))  # Getting there, not sure why this works but terminal doesn't
# print(genlibrary.localrepo.install(editable=True))

# genlibrary.localrepo.bump_version()

# genlibrary.generate_localfiles(print_out=True)

# genlibrary.localrepo.publish()



x = Packager("foobar", path="../foobar")

print(x.create_blank_locally_python())



































