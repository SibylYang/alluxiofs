from .alluxio_custom_io import *
import builtins


# Override the built-in open function
builtins.open = alluxio_open

os.listdir = alluxio_ls
os.mkdir = alluxio_mkdir
os.rmdir = alluxio_rmdir
os.rename = alluxio_rename
os.remove = alluxio_remove
shutil.copy = alluxio_copy
os.stat = alluxio_stat
os.path.isdir = alluxio_isdir
os.path.isfile = alluxio_isfile
os.path.exists = alluxio_exists
# original_chmod = os.chmod
os.walk = alluxio_walk