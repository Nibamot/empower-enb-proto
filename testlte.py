#!/usr/bin/env python3
"""Test script for empower-agent"""
import time
import ctypes as ct

from emage import INIT
from emage import DISCONNECTED
from emage import ENB_SETUP_REQUEST
from emage import UE_REPORT
from emage import CELL_MEASURE
from emage import UE_MEASURE
from emage.empoweragent import EmpowerAgent
from v1.lte.ltemsg import LTEMsg
from v1.lte.schedule.lteschedulemsg import LTEScheduleMsg
from v1.lte.schedule.hello.ltechelloreq import LTECHelloReq
from v1.lte.schedule.cellmeas.lteccellmeasreq import LTECCellMeasReq
from v1.lte.schedule.cellmeas.lteccellmeasrep import LTECCellMeasRep
from v1.lte.schedule.hello.ltechellorep import LTECHelloRep
from v1.lte.single.ltesinglemsg import LTESingleMsg
from v1.lte.single.enbcap.ltesenbcaprep import LTESEnbCapRep
from v1.lte.single.enbcap.ltesenbcapreq import LTESEnbCapReq
from v1.lte.single.cellcap.ltescellcaprep import LTESCellCapRep
from v1.lte.single.cellcap.ltescellcapreq import LTESCellCapReq
from v1.lte.trigger.uerep.ltetuereprep import LTETUeRepRep
from v1.lte.trigger.uerep.ltetuerepreq import LTETUeRepReq
from v1.lte.trigger.uemeas.ltetuemeasrep import LTETUeMeasRep
from v1.lte.trigger.uemeas.ltetuemeasreq import LTETUeMeasReq
from v1.lte.single.enbcap import _EnbDetails
from v1.lte.single.cellcap import _CellDetails
from v1.lte.trigger.uerep import _UeDet
from v1.lte.trigger.uemeas import _UeReport
from v1.lte.trigger.uemeas import _UeMeasurement
from v1.lte.schedule.cellmeas import _CellReports
from v1.lte.single.cellcap import CellcapType
from v1.empowerparser import EmpowerParser


testbuf = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
           #\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x07\xd0\x00\x00\x00\x00
hellot = b'\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9e\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x07\xd0\x00\x00\x00\x01'
"""
pop = LTETUeMeasReq()
uemeas = _UeMeasurement()
uemeas.nof_rrc = 1
uemeas.rrc[0].meas_id = 1
uemeas.rrc[0].rnti = 10
uemeas.rrc[0].earfcn = 19
uemeas.rrc[0].interval = 1000
uemeas.rrc[0].max_cells = 12
uemeas.rrc[0].max_meas = 10

uerep = _UeReport()
uerep.nof_rrc = 1
uerep.rrc[0].meas_id = 1
uerep.rrc[0].pci = 1
uerep.rrc[0].rsrp = 10
uerep.rrc[0].rsrq = 23

print(pop.format(testbuf, len(testbuf), uemeas))"""

def main():
    #Sample script to test empower-agent
    #Test-callback

    def testcap(mod):
        #Enb Cap test callback
        print("Controller requested by module id"+str(mod))
        enbrep = LTESEnbCapRep()
        edt = _EnbDetails()
        edt.nof_cells = ct.c_uint32(1)
        edt.cells[0].pci = ct.c_uint16(1)
        edt.cells[0].feat = ct.c_uint32(CellcapType.EP_CCAP_UE_MEASURE)#from init import ccap
        edt.cells[0].DL_earfcn = ct.c_uint16(1750)
        edt.cells[0].UL_earfcn = ct.c_uint16(19750)
        edt.cells[0].DL_prbs = ct.c_uint8(25)
        edt.cells[0].UL_prbs = ct.c_uint8(25)
        edt.cells[0].max_ues = ct.c_uint16(10)
        msgsz = enbrep.format(testbuf, len(testbuf), edt)
        print(msgsz)
        print(enb.send(testbuf, msgsz))

    def testinit():
        #Init test callback#
        print("Agent init to the controller")


    def testdisconnect():
        #Disconnect test callback#
        print("Disconnected from the controller")


    def testuereport(mod, trigid):
        # UE Report test callback#
        print("UE Report Requested by modid "+str(mod)+" and trigger ID "+str(trigid))
        uerep = LTETUeRepRep()
        uerep.pci = 1
        uedet = _UeDet()
        uedet.plmn = 4386
        uedet.rnti = 2233
        uedet.imsi = 3344
        uedet.tmsi = 4455
        msgs = uerep.format(testbuf, len(testbuf), uedet)
        print(enb.send(testbuf, msgs))


    def testcellmeas(cell, mod, interval, trig_id):
        # UE Report test callback#
        print("Cellmeasurement Requested by modid "+str(mod)+" and trigger ID "+str(trig_id)+" and interval "+str(interval))
        cellmeasrep = LTECCellMeasRep()
        cellmeasrep.pci = 1
        cellrep = _CellReports()
        cellrep.DL_prbs = 25
        cellrep.DL_prbs_used = 6
        cellrep.UL_prbs = 25
        cellrep.UL_prbs_used = 16
        msgs = cellmeasrep.format(testbuf, len(testbuf), cellrep)
        print(enb.send(testbuf, msgs))


    def testuemeas(cell, mod, interval, trig_id):
        # UE measure test callback#
        print("UE Measurement Requested by modid "+str(mod)+" and trigger ID "+str(trig_id)+" and interval "+str(interval))
        uemeasrep = LTETUeMeasRep()

        uerep = _UeReport()
        uerep.nof_rrc = 1
        uerep.rrc[0].meas_id = 1
        uerep.rrc[0].pci = 1
        uerep.rrc[0].rsrp = 10
        uerep.rrc[0].rsrq = 23
        msgs = uemeasrep.format(testbuf, len(testbuf), uerep)
        print(enb.send(testbuf, msgs))


    enblist = []
    i = 1
    if i == 1:
        enb = EmpowerAgent(id=i)
        enb.register_to(INIT, testinit)
        enb.register_to(DISCONNECTED, testdisconnect)
        enb.register_to(ENB_SETUP_REQUEST, testcap)
        enb.register_to(UE_REPORT, testuereport)
        enb.register_to(UE_MEASURE, testuemeas)
        enb.register_to(CELL_MEASURE, testcellmeas)
        enb.start()
        time.sleep(1)
        enblist.append(enb)

    for enb in enblist:
        time.sleep(6)
        msg = LTECHelloReq()
        msgsz = msg.format(testbuf, len(testbuf))
        print(msgsz)
        print(enb.send(testbuf, msgsz))

    for enb in enblist:
        time.sleep(60)
        enb.terminate()



if __name__ == "__main__":
    main()
