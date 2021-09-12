from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message
from spade.template import Template


class AIBehaviour(CyclicBehaviour):
    """Class for Agent Interface Behaviour"""

    async def on_start(self):
        print("AIBehaviour started...")

    def __init__(self):
        super().__init__()

    async def run(self):
        m = await self.receive(timeout=10)
        if m:
            print(m.body)
            self.agent.controller.update_table_values(message=m.body)
        else:
            print("Pas de message réçu")

    async def on_end(self):
        await self.agent.stop()


class AgentInterface(Agent):
    """Class for Agent Interface"""

    def __init__(self, jid, password, controller):
        super().__init__(jid, password, verify_security=False)
        self.controller = controller

    async def setup(self):
        t = Template()
        t.set_metadata("performative", "inform")
        t.set_metadata("ontology", "update")
        self.add_behaviour(AIBehaviour(), t)


class ANOBehaviour(OneShotBehaviour):
    async def on_start(self):
        print("ANOBehaviour started...")

    async def run(self):
        m = Message(to=self.agent.receiver)
        m.set_metadata("performative", "inform")
        m.set_metadata("ontology", "update")
        m.body = self.agent.message
        await self.send(m)
        print(f"Message sent successfully:{m.body}")
        self.exit_code = "Job finished!"
        await self.agent.stop()


class AgentNotification(Agent):
    def __init__(self, jid, password, message, receiver, verify_security=False):
        super().__init__(jid, password, verify_security)
        self.message = message
        self.receiver = receiver

    async def setup(self):
        self.add_behaviour(ANOBehaviour())
