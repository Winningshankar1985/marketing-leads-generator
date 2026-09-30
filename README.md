# 🎯 Marketing Leads Generator

An AI-powered multi-agent system that automates B2B lead generation for IT consulting businesses. It uses **DeepSeek LLM** as the reasoning backbone and **Google Places API** to discover real business contacts — then writes structured lead files to disk automatically.

---

## ✨ Features

- **Multi-Agent Architecture** — A supervisor agent delegates to specialized sub-agents for targeted lead discovery
- **Google Places Integration** — Pulls real-time business data (names, addresses, phone numbers, websites) via the Google Places API
- **Automated File Output** — Each run generates a timestamped lead file with structured contact information
- **Customizable Prompts** — Specify any location + industry domain to generate tailored leads
- **Retry & Error Handling** — Built-in retry logic (up to 5 attempts) for robust LLM interactions

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│         Lead Deep Agent             │
│   (Supervisor / Orchestrator)       │
│   Model: DeepSeek v4 Pro            │
├─────────────────────────────────────┤
│                                     │
│  ┌───────────────────────────────┐  │
│  │  Lead Generation Sub-Agent    │  │
│  │  (Prospect Finder)            │  │
│  │                               │  │
│  │  Tools:                       │  │
│  │  ├── find_prospects           │  │
│  │  │   (Google Places API)      │  │
│  │  ├── create_file              │  │
│  │  │   (Write leads to disk)    │  │
│  │  └── read_file                │  │
│  │      (Read generated files)   │  │
│  └───────────────────────────────┘  │
│                                     │
└─────────────────────────────────────┘
         │
         ▼
  leads-generated/
  └── leads-<timestamp>/
      └── leads-file-<timestamp>.txt
```

---

## 📁 Project Structure

```
lead_agents/
├── lead_deepagent.py              # Main entry point — supervisor agent
├── main.py                        # Alternative entry point
├── sub_agents/
│   └── lead_generation_sub_agent.py   # Sub-agent config with tools
├── tools/
│   ├── places_search_tool.py      # Google Places API wrapper
│   └── file_ops.py                # File create/read utilities
├── leads-generated/               # Output folder (auto-created)
│   └── leads-<timestamp>/
│       └── leads-file-<timestamp>.txt
├── .env                           # API keys (not committed)
├── pyproject.toml                 # Project metadata (uv)
├── requirements.txt               # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.14+**
- [**uv**](https://docs.astral.sh/uv/) — fast Python package manager
- **DeepSeek API Key** — [Get one here](https://platform.deepseek.com/)
- **Google Places API Key** — [Google Cloud Console](https://console.cloud.google.com/)

### 1. Clone the Repository

```bash
git clone https://github.com/Winningshankar1985/marketing-leads-generator.git
cd marketing-leads-generator
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```env
DEEPSEEK_API_KEY="your-deepseek-api-key"
map_demo_key="your-google-places-api-key"
model_base="deepseek-v4-flash"
model_pro="deepseek-v4-pro"
```

### 3. Install Dependencies

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

### 4. Run the Agent

```bash
uv run lead_deepagent.py
```

You'll be prompted to enter a location and domain:

```
Please mention a location and the domain to look Leads for:
> find placement officers from universities in Texas, USA
```

---

## 📄 Sample Output

Each run creates a timestamped file under `leads-generated/`:

```
leads-generated/
└── leads-2026-09-30T14:36:28.997599/
    └── leads-file-2026-09-30T14:36:28.997599.txt
```

Example content:

```
User Query: find placement officers from universities in Texas
LEADS GENERATED -
University of Texas at Austin, University, Austin, TX, Career Services, (512) 471-3434, https://www.utexas.edu/
Texas A&M University, University, College Station, TX, Career Center, (979) 845-5139, https://www.tamu.edu/
...
----- Fin -----
```

---

## 🔧 Dependencies

| Package | Purpose |
|---|---|
| `python-dotenv` | Load API keys from `.env` |
| `langchain` | Agent framework & tool decorators |
| `langchain-deepseek` | DeepSeek LLM integration |
| `langchain-google-community[places]` | Google Places API wrapper |
| `deepagents` | Multi-agent orchestration |

---

## 🛡️ Security

- API keys are stored in `.env` and excluded via `.gitignore`
- Never commit your `.env` file to version control
- Generated lead files are also gitignored to prevent accidental data exposure

---

## 📜 License

This project is for personal / internal business use.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.
