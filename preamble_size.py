"""
Print the size of a typical SSH command line and the bootstrap code sent to new
contexts.
"""

import inspect
import zlib

import mitogen.fakessh
import mitogen.master
import mitogen.parent
import mitogen.ssh
import mitogen.sudo

router = mitogen.master.Router()
context = mitogen.parent.Context(router, 0)
stream = mitogen.ssh.Stream(router, 0, hostname='foo')

print 'SSH command size: %s' % (len(' '.join(stream.get_boot_command())),)
print 'Preamble size: %s (%.2fKiB)' % (
    len(stream.get_preamble()),
    len(stream.get_preamble()) / 1024.0,
)

for mod in (
        mitogen.master,
        mitogen.parent,
        mitogen.ssh,
        mitogen.sudo,
        mitogen.fakessh,
        ):
    sz = len(zlib.compress(mitogen.parent.minimize_source(inspect.getsource(mod))))
    print '%s size: %s (%.2fKiB)' % (mod.__name__, sz, sz / 1024.0)
