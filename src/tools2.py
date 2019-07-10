# This application will not work on localhost
from itoolkit import *
from itoolkit.transport import DatabaseTransport
import ibm_db_dbi

itool = iToolKit()
conn = ibm_db_dbi.connect()
itransport = DatabaseTransport(conn)

itool.add(iCmd('addlible', 'ADDLIBLE PYSEIDEN'))

itool.add(iPgm('pypgm001c', 'PYPGM001C')
          .addParm(iData('RTNMSG', '50a', 'a'))
          .addParm(iData('AMOUNT', '15p2', '33.33'))
)

itool.call(itransport)

pypgm001c = itool.dict_out('pypgm001c')

if 'success' in pypgm001c:
    print(pypgm001c['success'])
    print("Return parameter values:")
    print("RTNMSG: " + pypgm001c['RTNMSG'])
    print("AMOUNT: " + pypgm001c['AMOUNT'])
else:
    raise Exception("Program call error:" + pypgm001c['error'])

