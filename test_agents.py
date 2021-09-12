import time

from agents import AIA, ANO
from agents.agents import AgentInterface, AgentNotification

aia = AgentInterface(jid=AIA["jid"], password=AIA["password"], controller=None)
future = aia.start()
future.result()
ano = AgentNotification(jid=ANO["jid"], password=ANO["password"], receiver=AIA["jid"], message="Hello Test")
ano.start()
while aia.is_alive():
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        aia.stop()
        ano.stop()
        break