# Rankizz Agent Skills

Portable SEO workflows for Claude, Codex, ChatGPT, and other agents that support the Agent Skills format.

Each skill is an independent folder with a public `SKILL.md`. Some workflows can run entirely with local files and network tools. Others can optionally use Rankizz MCP or the Rankizz REST API for live search, backlink, analytics, and audit data.

## Skills

| Skill | Purpose | Rankizz required |
| --- | --- | --- |
| `rankizz-setup-seo-project` | Create reusable SEO project context | No |
| `rankizz-audit-site-cloud` | Run a hosted Rankizz site audit | Yes |
| `rankizz-audit-site-local` | Audit with the agent's local resources | No |
| `rankizz-research-keywords` | Find and prioritize keyword opportunities | Optional |
| `rankizz-cluster-keywords` | Turn keyword lists into a page map | Optional |
| `rankizz-map-competitive-landscape` | Map the domains winning a search market | Optional |
| `rankizz-analyze-competitor` | Analyze one competitor's organic footprint | Optional |
| `rankizz-prospect-links` | Find and qualify relevant link prospects | Optional |

## Install

Download individual ZIP packages and read the full public instructions at [rankizz.com/docs/skills](https://www.rankizz.com/docs/skills).

For Codex, copy a skill folder into `~/.agents/skills/` for personal use or `.agents/skills/` inside a repository.

For Claude Code, copy a skill folder into `~/.claude/skills/` for personal use or `.claude/skills/` inside a project.

For Claude.ai or another upload-based client, upload the ZIP for the selected skill.

## Rankizz access

Cloud workflows use the current remote Streamable HTTP MCP endpoint:

```text
https://www.rankizz.com/mcp
```

Interactive clients should use OAuth. Headless clients can create a personal key from [Rankizz API access](https://www.rankizz.com/api-access). Hosted MCP and API calls require a balance of at least 10 credits.

## Build packages

Run:

```sh
python3 scripts/build_packages.py
```

The script validates the catalog and creates one self-contained ZIP per skill in `dist/`.
