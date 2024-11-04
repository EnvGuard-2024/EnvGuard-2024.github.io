import os
import sys

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from iotSystem.IotSystem import IoTSystem
import buchi.Buchi as Buchi
from representation.Environment import setEnvironment, getEnvironment

def runLTL():
    ltl = 'F(TeaRoom.MicrowaveOven.on & !TeaRoom.HumanState.detected)'
    setEnvironment(ltl)
    iot_system = IoTSystem(getEnvironment())
    ts = iot_system.transition_system
    buchi_ts = Buchi.ts_to_genbuchi(ts)
    buchi_ltl = Buchi.ltl_to_buchi(ltl)
    (buchi_final, pairs) = Buchi.product(buchi_ts, buchi_ltl)
    os.chdir("/home/rjl/SafetyTap")
    try:
        os.stat('result')
    except FileNotFoundError:
        os.mkdir('result')

    ts.writeToGv("result/temp.gv")
    buchi_ltl.writeToGv('result/ltl.gv')
    buchi_ts.writeToGv('result/ts.gv')
    buchi_final.writeToGv('result/final.gv')

    buchi_final.get_safty_specification(ts, pairs)

