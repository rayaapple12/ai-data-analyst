# AI Data Analyst Agent

An agentic AI system that answers natural-language questions about structured datasets by combining LLM reasoning with deterministic data-analysis tools.

The system is designed to move beyond a basic "chat with CSV" workflow by dynamically planning analysis, selecting tools, validating results, recovering from failures, and producing evidence-backed answers.

## Overview

Users can ask questions such as:

- "What are the top 10 products by revenue?"
- "Which region contributed most to the revenue decline?"
- "Compare sales between Q1 and Q2."
- "Is the change statistically significant?"
- "Show me the monthly revenue trend."
- "Find unusual sales behavior."

Instead of asking the LLM to perform calculations directly, the agent delegates computation to deterministic tools such as SQL, Pandas, and statistical functions.

## Architecture

```text
                         User
                           |
                           v
                       FastAPI
                           |
                           v
                 Query Understanding
                           |
                           v
                    LangGraph Agent
                           |
                           v
                        Planner
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
          SQL Tool    Python Tool   Statistics Tool
             |             |             |
             v             v             v
        PostgreSQL      Pandas/       NumPy/
                        Python       Statistics
             |             |             |
             +-------------+-------------+
                           |
                           v
                   Result Validation
                           |
                           v
                    Agent Reasoning
                           |
                    +------+------+
                    |             |
                    v             v
              Visualization   Final Answer