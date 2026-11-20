Here is a structured, actionable **quality improvement backlog** for the *roles-skills* open-source project, split into **user-facing** (new visitors, promotion, upskilling) and **engineering** (coding, testing, auditing) tracks.
Tasks are unordered inside each category; use the labels (⚡ quick win, 🎯 high-impact, 📊 measurable) to sequence them.

---

## 🚀 **New visitors, promotion & upskilling**

### 1. Discoverability & first impressions
| Task | Description | Effort | Label |
|---|---|---|---|
| **Add an interactive “Find my role” wizard** | 3–5 question funnel on the home page that narrows to a suggested role based on discipline + seniority + keyword. | 2 d | 🎯 |
| **Search inside the site** | Client-side search (e.g., Pagefind, MiniSearch) over role titles, summaries, responsibilities, skill names. | 1–2 d | ⚡ |
| **Badges on GitHub repo** | Add shields for licence, languages, last commit, CI status, stars, website. | 1 h | ⚡ |
| **Tags / keywords in repo** | Curate `topics:` in `roles-skills/.github/repo-metadata.yml` (or `.github/community/topics.yml`) so the project appears in GitHub topic pages. | 30 m | ⚡ |
| **One-pager hand-out** | PDF/HTML flyer (A4) with URL, elevator pitch, example role snippet, licence, QR code to site. | 1 d | 🎯 |
| **Slide deck template** | 10-slide intro deck for meet-ups or internal training—CC-BY. | 1 d | 🎯 |

### 2. Guides & onboarding for users
| Task | Description | Effort | Label |
|---|---|---|---|
| **5-min video screencast** | Walk-through: find role → open self-assessment → export TSV → open in Sheets. | 1 d | 🎯 |
| **Guided tour on website** | Add Shepherd.js or Intro.js tour that points out self-assessment, export, locale picker. | 1 d | ⚡ |
| **Quick-start “recipes”** | New `guides/recipes/` folder with cookbook pages: “Run a team gap-analysis in 30 min”, “Prepare for a performance review”, “Create a learning plan from gaps”. | 2 d | 🎯 |
| **Embeddable widget** | `<iframe>` snippet that organisers can drop into intranets; searches and displays role summaries. | 2 d | 🎯 |
| **FAQ page** | Consolidate common questions: “Is this official?”, “How do bands map to pay?”, “Can I reuse the TSVs?”. | 1 d | ⚡ |
| **Glossary tooltip** | Hover definitions for PCF, ESCO, SFIA, Band 8a–8d, competency outline. | 1 d | ⚡ |

### 3. Promotion & community growth
| Task | Description | Effort | Label |
|---|---|---|---|
| **Blog post series** | Medium/Dev.to: (1) Why we built it, (2) How bands map to PCF/SFIA, (3) Running a skills gap analysis. | 3 d | 🎯 |
| **Hacker News / Reddit launch** | Draft a short, honest “Show HN” post with a clear hook (“Open reference of 73 digital-health roles, 253 skills, 20 locales”). | 30 m | ⚡ |
| **Twitter thread** | 10-tweet explainer with GIF screencaps of self-assessment export. | 1 h | ⚡ |
| **Add to awesome lists** | PRs to `awesome-healthcare-it`, `awesome-standards`, `awesome-public-datasets`. | 1 h | ⚡ |
| **LinkedIn article & share** | Post “Using an open roles reference for performance reviews” with downloadable TSV example. | 1 d | 🎯 |
| **Community call** | Monthly 30-min Zoom/Teams open office hours; record & publish notes. | ongoing | 🎯 |

### 4. Upskilling & learning paths
| Task | Description | Effort | Label |
|---|---|---|---|
| **Learning-path generator** | Given a role + gap TSV, suggest ordered learning resources (MOOCs, certifications) that map to each skill at the target level. Start with free resources per skill YAML. | 3 d | 🎯 |
| **Skill → resource crosswalk** | New `data/learning/` folder: YAML mapping each skill to 1–3 recommended resources (url, title, cost, duration). | 5 d | 📊 |
| **Competency matrix dashboard** | Simple web view: upload your team’s TSV gap files, see a heat-map of skill levels vs. expected. | 2 d | 📊 |
| **Export as badges / OpenBadges** | Extend self-assessment export to include OpenBadges-compatible JSON so users can display completed assessments. | 2 d | 🎯 |
| **Role comparison view** | Side-by-side view of two role levels to see responsibility and skill delta. | 1 d | ⚡ |
| **Gamification** | Streak counter on the client-side self-assessment (“You’ve assessed 3 roles this week”). | 1 d | ⚡ |

---

## 🔧 **Engineering, coding, testing & auditing**

### 1. Code & repo health
| Task | Description | Effort | Label |
|---|---|---|---|
| **Switch website build to `npm` scripts** | Replace Makefile targets with standard `package.json` scripts so CI and contributors use the same commands. | 1 h | ⚡ |
| **Add pre-commit hooks** | `pre-commit` framework: `black`, `isort`, `mdformat`, `prettier`, `eslint`, `cspell`. | 1 d | ⚡ |
| **Pin Python & Node versions** | Add `.python-version`, `.nvmrc`, and engine field in `package.json`; document in CONTRIBUTING. | 30 m | ⚡ |
| **Dockerise build & serve** | `Dockerfile` + `docker-compose.yml` for “one command” local preview. | 1 d | ⚡ |
| **GitHub Actions CI matrix** | Run check & build on every PR across Python 3.10–3.12 and Node 18–20. | 1 d | ⚡ |
| **Enforce signed commits** | Enable `require-signatures` branch protection on `main`. | 30 m | ⚡ |

### 2. Testing & validation
| Task | Description | Effort | Label |
|---|---|---|---|
| **Unit tests for `scripts/build.py`** | `pytest` with 90 %+ coverage; mock `data/` when needed. | 3 d | 📊 |
| **Snapshot tests for docs** | Store golden Markdown outputs; fail if generation drifts. | 1 d | 📊 |
| **Link-check website build** | Add `lychee` or `linkchecker` to CI to validate every Markdown link in generated Markdown and website. | 1 d | ⚡ |
| **TSV schema validation** | JSON-schema (or `csv-validate`) for every export TSV; CI step that fails on schema drift. | 1 d | ⚡ |
| **Property-based tests** | `hypothesis` on data integrity: every role references valid band, every skill exists, points sum within band range. | 1 d | 📊 |
| **Website accessibility audit** | Run `axe-core` or Pa11y in CI on the static site; fix WCAG 2.2 AA failures. | 2 d | 🎯 |

### 3. Tooling & automation
| Task | Description | Effort | Label |
|---|---|---|---|
| **Automated dependency updates** | Dependabot for npm (`roles-skills.github.io`) and Python (`scripts/`). | 30 m | ⚡ |
| **Automated locale synchronisation** | Bot that flags missing keys or stale YAML in locale folders via PR comments. | 2 d | ⚡ |
| **CI nightly build & deploy preview** | GitHub Actions that builds the site on schedule, publishes preview to `gh-pages` branch `preview/YYYY-MM-DD`. | 1 d | ⚡ |
| **Release workflow** | GitHub Actions that tags, builds, commits exports, creates GitHub Release with changelog from PR titles. | 1 d | ⚡ |
| **Fuzzy matching in CMS** | Sveltia CMS plugin: fuzzy-match skill names when editors type so typos are caught. | 2 d | ⚡ |
| **Bulk import / export script** | `scripts/import_roles.py` to bulk-add roles from a CSV template (for organisations that want to extend). | 2 d | 🎯 |

### 4. Website performance & reliability
| Task | Description | Effort | Label |
|---|---|---|---|
| **Performance budgets** | Lighthouse CI: < 1 s First Contentful Paint, < 2 s Largest Contentful Paint, < 500 KB total JS. | 1 d | ⚡ |
| **Lazy-load locale bundles** | Split the SvelteKit locale store so each page only loads the current locale JSON. | 1 d | ⚡ |
| **Service-worker + cache** | Pre-cache all static assets for offline reading. | 1 d | ⚡ |
| **Canonical URLs & sitemap** | Auto-generate `/sitemap.xml` with hreflang alternates; validate in CI. | 1 d | ⚡ |
| **404 & redirect pages** | Custom 404 page with search box; redirect legacy paths (e.g., `/roles/software-developer` → `/en-001/roles/software-developer/`). | 1 d | ⚡ |
| **Error tracking** | Sentry or similar for client-side errors in the website (opt-in telemetry). | 1 d | ⚡ |

### 5. Data integrity & auditing
| Task | Description | Effort | Label |
|---|---|---|---|
| **Auditable YAML change history** | Add `git-notes` or conventional-commits messages to `data/**` so every field change is auditable. | 1 d | ⚡ |
| **Provenance metadata in YAML** | Add `last_reviewed:` date + reviewer name to each role YAML; validate in CI that nothing is > 12 months old. | 1 d | 📊 |
| **Cross-reference consistency suite** | One script `scripts/audit.py` that runs: every catalogue role has a YAML file; every referenced skill exists; every ESCO URI resolves; every PCF skill is in the crosswalk; job-evaluation points are in-band. | 2 d | 🎯 |
| **Deprecation markers** | Allow YAML field `deprecated: true` on skills/roles; build then emits warnings and excludes from indexes. | 1 d | ⚡ |
| **Diff report generator** | `scripts/diff_report.py` that emits Markdown comparing any two commits’ data changes (roles added/removed, skills renamed, etc.). | 2 d | 🎯 |
| **Audit log export** | nightly JSON dump of every role YAML hash + timestamp to S3/Releases for public audit trail. | 1 d | ⚡ |

### 6. Security & compliance
| Task | Description | Effort | Label |
|---|---|---|---|
| **SPDX licence scanning** | Run `scan-licenses` or `licensee` in CI to confirm only CC-BY-4.0 + MIT + OGL-3.0 content. | 1 h | ⚡ |
| **Sveltia CMS authentication** | Finish GitHub OAuth or key-based auth for `/admin/`. | 1 d | ⚡ |
| **CSP & security headers** | Tighten `Content-Security-Policy` in SvelteKit; add `X-Content-Type-Options`, `X-Frame-Options`. | 1 d | ⚡ |
| **API rate-limit for CMS** | Add rate limiting to Sveltia CMS endpoint (if public) to prevent abuse. | 1 d | ⚡ |
| **Secret scanning** | `gitleaks` or `trufflehog` in PR checks to block accidental commit of keys. | 1 h | ⚡ |

---

### How to prioritise next
1. **Start with ⚡ quick wins** – many are < 1 day and block nothing.
2. **Pick 🎯 high-impact items** that directly help new visitors: search, wizard, quick-start recipes, blog post.
3. **Tackle 📊 measurable engineering** once basics are solid: CI tests, accessibility audit, snapshot tests, audit suite.
4. **Schedule recurring tasks**: community call, dependency updates, nightly builds.

All code tasks should include tests or validation, and all user-facing changes should be A/B-testable or easily reversible (feature flags via URL params work well in static sites).
