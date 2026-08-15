---
name: rankizz-map-competitive-landscape
description: Map an organic-search market by identifying recurring ranking domains, competitor types, keyword coverage, winning content formats, authority patterns, and underserved opportunities. Use when entering a category, planning SEO strategy, or determining which search competitors matter. Rankizz is optional until live SERP, domain, keyword, or backlink data is needed.
---

# Map the competitive landscape

Explain who wins the search market, why, and where the user's site can compete. Do not reduce the result to a list of familiar business competitors.

## Define the market

Use existing project context when available. Establish:

- product or category
- audience and search tasks
- country and language
- relevant site and current maturity
- time horizon and business constraints

Create a representative query set across head terms, use cases, problems, comparisons, questions, and high-intent searches. Keep the set bounded and show it in the report.

## Gather available evidence

Use public search results, supplied exports, existing research, and accessible pages first. Record market, date, and source for every observation.

Use Rankizz only when live or provider-backed evidence is needed:

- `find_serp_competitors` for repeated domain overlap across a supplied keyword set
- `get_serp_results` for page types and result composition
- `get_domain_overview` for high-level organic footprint
- `get_ranked_keywords` for keyword and URL coverage
- `get_backlinks_overview` for authority context
- `get_ahrefs_domain_rating` for a free cached directional DR check

Hosted calls require at least 10 credits. Stop cloud calls on a low-credit response, link to `https://www.rankizz.com/billing`, and continue with evidence already available. Batch work and avoid enriching every discovered domain.

## Classify competitors

Follow [references/landscape-framework.md](references/landscape-framework.md). Separate:

- direct products or services
- publishers and educational sites
- directories and marketplaces
- communities and forums
- tools, templates, and data products
- aggregators, affiliates, and comparison sites
- institutions or primary sources

Recurring search domains may be important even when they do not compete commercially.

## Analyze patterns

Identify:

- which domains recur and for which intent lanes
- winning page types, depth, freshness, and media
- brand, entity, authorship, and source signals
- topic and keyword coverage
- authority and backlink patterns when measured
- SERP features and zero-click pressure
- gaps where current results underserve the user's audience

Separate evidence from inference. Do not claim causation from correlation.

## Deliver

Return a landscape map containing the query set, competitor-type matrix, recurring winners, content and authority patterns, defensible opportunities, risks, and the next three research actions.

Recommend deeper single-competitor analysis only for domains whose evidence warrants it.
