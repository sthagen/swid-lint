# [[[fill git_describe()]]]
__version__ = '2023.10.22+parent.a2b07f84'
# [[[end]]] (checksum: 6fbabfee32c9c3510a8969f35f34619c)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
