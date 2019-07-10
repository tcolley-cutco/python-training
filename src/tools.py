# This application will not work on localhost
from itoolkit import *
from itoolkit.transport import DatabaseTransport
import ibm_db_dbi

itool = iToolKit()
conn = ibm_db_dbi.connect()
itransport = DatabaseTransport(conn)

itool.add(iCmd('rtvjoba', 'RTVJOBA USRLIBL(?) SYSLIBL(?) CCSID(?N) OUTQ(?)'))
itool.call(itransport)
rtvjoba = itool.dict_out('rtvjoba')
if 'success' in rtvjoba:
    print(rtvjoba['row'][0]['USRLIBL'])
    print(rtvjoba['row'][1]['SYSLIBL'])
    print(rtvjoba['row'][2]['CCSID'])
    print(rtvjoba['row'][3]['OUTQ'])