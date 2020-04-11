# 包：含大量模块的文件夹，__init__.py

# 方法1(推荐)：import 包名.模块名
import package_directory.package1 as p1
import package_directory.package2 as p2

p1.show()
p2.show()

# 方法2(推荐)： from 包名 import 模块名
from package_directory import package1 as p3
from package_directory import package2 as p4

p3.show()
p4.show()

# 方法3: from 包名 import *
# 需要和__init__.py文件内设置__all__=['模块名1','模块名2']配合，如果不设置，所有模块都不导入
from package_directory import *

package1.show()

# 方法4：import 包名
import package_directory

package_directory.package2.show()
