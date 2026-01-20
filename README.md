# Autonomous WhatsApp Updates Agent

This project demonstrates an autonomous mobile agent built using the Droidrun framework.

## Overview
The agent reviews unread WhatsApp chats (including communities), scrolls through unread messages,
and generates a structured daily summary in the Notes app titled **"WhatsApp Updates"**.

If some messages cannot be fully accessed, the agent transparently reports this in the summary
instead of hiding failures.

## What the Agent Does
- Opens WhatsApp and navigates to unread chats
- Handles communities and announcement groups
- Scrolls through unread messages to capture content
- Synthesizes information into a dated summary
- Writes the summary into the Notes app

## Why This Matters
Unread messages are fragmented across multiple chats and communities.
This agent reduces cognitive load by converting scattered conversations
into a single actionable update.

## Technology Stack
- Droidrun Agent Framework
- Mobilerun Playground
- Vision-enabled LLM execution
- Android device automation

## Demo
A full autonomous execution demo is available via the submitted YouTube link.

## Notes
This repository focuses on agent logic and reproducibility.
Execution is demonstrated using the Mobilerun Playground for reliability.

