# Rankizz Agent Skills

Portable SEO and audience-research workflows for Claude, Codex, ChatGPT, and other agents that support the Agent Skills format.

Each skill is an independent folder with a public `SKILL.md`. Some workflows can run entirely with local files and network tools. Others can optionally use Rankizz MCP or the Rankizz REST API for live search, backlink, analytics, and audit data.

## Skills

| Skill | Purpose | Credit usage |
| --- | --- | --- |
| `rankizz-setup-seo-project` | Create reusable SEO project context | Optional |
| `rankizz-audit-site-cloud` | Run a hosted Rankizz site audit | Required |
| `rankizz-audit-site-local` | Audit with the agent's local resources | None |
| `rankizz-audit-on-page-seo` | Check the complete on-page SEO implementation | Optional |
| `rankizz-research-keywords` | Find and prioritize keyword opportunities | Optional |
| `rankizz-cluster-keywords` | Turn keyword lists into a page map | Optional |
| `rankizz-map-competitive-landscape` | Map the domains winning a search market | Optional |
| `rankizz-analyze-competitor` | Analyze one competitor's organic footprint | Optional |
| `rankizz-prospect-links` | Find and qualify relevant link prospects | Optional |
| `rankizz-build-seo-roadmap` | Build an evidence-based 1–30 day SEO roadmap | Required |
| `rankizz-write-human-blog-post` | Research and write a useful post in a natural voice | Optional |
| `rankizz-write-tool-listicle` | Create an evidence-backed best-tools list | Optional |
| `rankizz-write-alternatives-page` | Write a fair product alternatives page | Optional |
| `rankizz-write-comparison-page` | Compare two products using the same evidence standard | Optional |
| `rankizz-write-competitor-review-pricing` | Explain a competitor's product, fit, and current pricing | Optional |
| `rankizz-write-reddit-post` | Write a useful, subreddit-native post | Optional |
| `rankizz-find-reddit-reply-opportunities` | Research threads and save transparent reply drafts | Required |
| `rankizz-write-linkedin-post` | Research current posts and draft a knowledge-first LinkedIn post | Required |
| `rankizz-find-outreach-emails` | Find public, role-relevant outreach contacts with source evidence | None |
| `rankizz-write-backlink-outreach-email` | Write a credible page-specific backlink pitch | Optional |

## Install

Download individual ZIP packages and read the full public instructions at [rankizz.com/docs/skills](https://www.rankizz.com/docs/skills).

For Codex, copy a skill folder into `~/.agents/skills/` for personal use or `.agents/skills/` inside a repository.

For Claude Code, copy a skill folder into `~/.claude/skills/` for personal use or `.claude/skills/` inside a project.

For Claude.ai or another upload-based client, upload the ZIP for the selected skill.

## Rankizz access

Remote Rankizz workflows use the current Streamable HTTP MCP endpoint:

```text
https://www.rankizz.com/mcp
```

Interactive clients should use OAuth. Headless clients can create a personal key from [Rankizz API access](https://www.rankizz.com/api-access). MCP and API calls require a balance of at least 10 credits. A successful no-cost operation does not deduct credits.

## Build packages

Run:

```sh
python3 scripts/build_packages.py
```

The script validates the catalog and creates one self-contained ZIP per skill in `dist/`.
