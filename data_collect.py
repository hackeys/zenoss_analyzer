import Globals
from Products.ZenUtils.ZenScriptBase import ZenScriptBase
from transaction import commit
dmd = ZenScriptBase(connect=True, noopts=True).dmd

f = open('/tmp/data_collection.txt', 'w')
f.writelines("ZENOSS_VERSION: {0}\n".format(dmd.version))
f.writelines("DEVICE_COUNT: {0}\n".format(dmd.Devices.countDevices()))
#f.writelines("CATALOG_OBJECT_COUNT: {0}".format(len(zport.global_catalog)))
f.close()
