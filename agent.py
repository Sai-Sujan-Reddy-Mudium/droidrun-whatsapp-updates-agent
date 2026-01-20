"""
Autonomous WhatsApp Updates Agent (Demo Reference)

This file represents the agent logic used in the Droidrun DevSprint submission.
Execution is demonstrated via the Mobilerun Playground.
"""

from droidrun import DroidAgent, AdbTools

GOAL = """
Open WhatsApp, navigate to unread chats (including communities),
scroll through unread messages, and generate a dated summary
in the Notes app titled 'WhatsApp Updates'.
"""

def main():
    tools = AdbTools()
    agent = DroidAgent(
        goal=GOAL,
        tools=tools
    )
    agent.run()

if __name__ == "__main__":
    main()
