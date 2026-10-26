# GPT Plugin Lab — 365-Day Development Roadmap

## Project rules

- **Start date:** 2026-10-21. Day 1 is the first verified project-setup day; Day 2 is 2026-10-22.
- **Day numbering:** calendar days counted inclusively from the start date, not commit counts.
- **Completion standard:** mark a day complete only after a useful change is committed to the default branch and the resulting commit is verified. Run relevant tests when possible and report test/CI status accurately.
- **No padding:** no empty commits, artificial activity, or backfilled commits for missed days. If blocked, record the blocker honestly and resume with the next useful task.
- **Scope:** reorder work when dependencies, tests, or security review show that doing so is necessary; do not ship unsafe features just to match a date.

## Progress log

- [x] **Day 1 — 2026-10-21:** create GPT Plugin Lab's Python package, dependency-free chat client, unit tests, packaging metadata, secret-safe defaults, and CI workflow. Initial commits verified in repository history.
- [x] **Day 2 — 2026-10-22:** publish the detailed 365-day plan, define calendar-day numbering, and establish honest completion rules. Verified roadmap commit: `0ffd6b7ccdab73db6cc20f6178c35494c9b0c0c4`.
- [x] **Day 3 — 2026-10-23:** add immutable environment configuration in commit `4d56fbfd8f970dd9808ef3d256cb19d0dbe4bcb8`; GitHub Actions passed on that commit.
- [x] **Day 4 — 2026-10-24:** document configuration precedence and local API-key setup, clarify that `.env` is not auto-loaded by the library, and align `.env.example` with the supported timeout setting.
- [x] **Day 5 — 2026-10-25:** validate chat-message objects, supported roles (`system`, `developer`, `user`, `assistant`, `tool`), and string content before sending requests; add offline tests proving malformed messages fail before network access. Implementation: `630b85b1043fe8018005afcbd135e67549bd01a8`; tests: `3d639b7874bb2281fdeff9938ef467d0186c03b7`. Locally mirrored unit suite: 9 tests passed; GitHub CI status was not available at verification time.
- [x] **Day 6 — 2026-10-26:** reject blank or non-string model names and invalid temperatures (out-of-range, non-finite, boolean, or non-numeric) before any network call. Implementation: `b0d3b120c80e0bea64c6dbdb5b2432e69589580e`; tests: `3b3a1fa40bc097fc0a1913735ce1bbb3dbf1da16`. Follow-up hardening safely rejects oversized integer temperatures: implementation `4d53e5254987a03bc6bf337e380e301ca84f2d21`, regression test `66aa981c98e1518761548de485b594fb62dc95f2`. GitHub Actions passed on the latest test commit.

## Daily roadmap

### Days 1–28: Foundation and project hygiene

- [x] **Day 1 (2026-10-21):** Create the package, client, unit tests, and CI foundation.
- [x] **Day 2 (2026-10-22):** Publish this 365-day roadmap and define honest progress rules.
- [x] **Day 3 (2026-10-23):** Implement an immutable configuration object for environment variables.
- [x] **Day 4 (2026-10-24):** Document configuration precedence and local API-key setup.
- [x] **Day 5 (2026-10-25):** Validate message roles and content before requests.
- [x] **Day 6 (2026-10-26):** Reject blank model names and invalid request parameters.
- [ ] **Day 7 (2026-10-27):** Validate timeout values as finite and positive.
- [ ] **Day 8 (2026-10-28):** Normalize and validate provider base URLs.
- [ ] **Day 9 (2026-10-29):** Document public exceptions and error guarantees.
- [ ] **Day 10 (2026-10-30):** Add a typed-package marker and verify package discovery.
- [ ] **Day 11 (2026-10-31):** Configure consistent formatting for Python sources.
- [ ] **Day 12 (2026-11-01):** Configure lint checks for package code and tests.
- [ ] **Day 13 (2026-11-02):** Run CI on Python 3.11.
- [ ] **Day 14 (2026-11-03):** Run CI on Python 3.12.
- [ ] **Day 15 (2026-11-04):** Run CI on Python 3.13.
- [ ] **Day 16 (2026-11-05):** Add contributor setup and test instructions.
- [ ] **Day 17 (2026-11-06):** Add a pull-request template with test expectations.
- [ ] **Day 18 (2026-11-07):** Add a focused bug-report template.
- [ ] **Day 19 (2026-11-08):** Add a feature-request template with acceptance criteria.
- [ ] **Day 20 (2026-11-09):** Verify license and attribution policy.
- [ ] **Day 21 (2026-11-10):** Publish test coverage in CI.
- [ ] **Day 22 (2026-11-11):** Set a justified minimum coverage threshold.
- [ ] **Day 23 (2026-11-12):** Validate source and wheel builds in CI.
- [ ] **Day 24 (2026-11-13):** Smoke-test installation in a clean environment.
- [ ] **Day 25 (2026-11-14):** Test documented public imports.
- [ ] **Day 26 (2026-11-15):** Introduce a consistent changelog format.
- [ ] **Day 27 (2026-11-16):** Document versioning and compatibility policy.
- [ ] **Day 28 (2026-11-17):** Review the foundation and record remaining gaps.

### Days 29–56: Request contracts and response parsing

- [ ] **Day 29 (2026-11-18):** Define a typed chat-message representation.
- [ ] **Day 30 (2026-11-19):** Validate supported roles and content values.
- [ ] **Day 31 (2026-11-20):** Centralize endpoint URL construction.
- [ ] **Day 32 (2026-11-21):** Test request serialization without network access.
- [ ] **Day 33 (2026-11-22):** Separate response parsing from HTTP transport.
- [ ] **Day 34 (2026-11-23):** Preserve safe HTTP status details in client errors.
- [ ] **Day 35 (2026-11-24):** Handle non-JSON HTTP error bodies safely.
- [ ] **Day 36 (2026-11-25):** Handle empty successful responses explicitly.
- [ ] **Day 37 (2026-11-26):** Validate the response choices collection.
- [ ] **Day 38 (2026-11-27):** Validate the first assistant-message object.
- [ ] **Day 39 (2026-11-28):** Handle null or missing assistant content deliberately.
- [ ] **Day 40 (2026-11-29):** Expose the provider finish reason.
- [ ] **Day 41 (2026-11-30):** Parse response IDs when present.
- [ ] **Day 42 (2026-12-01):** Parse returned model metadata when available.
- [ ] **Day 43 (2026-12-02):** Add a typed completion result containing usage.
- [ ] **Day 44 (2026-12-03):** Keep the existing text-returning API compatible.
- [ ] **Day 45 (2026-12-04):** Document model selection and defaults.
- [ ] **Day 46 (2026-12-05):** Add configurable maximum output tokens.
- [ ] **Day 47 (2026-12-06):** Add validated top-p sampling.
- [ ] **Day 48 (2026-12-07):** Add stop-sequence support and tests.
- [ ] **Day 49 (2026-12-08):** Add frequency and presence penalties.
- [ ] **Day 50 (2026-12-09):** Add response-format options where supported.
- [ ] **Day 51 (2026-12-10):** Introduce a typed request-options object.
- [ ] **Day 52 (2026-12-11):** Allow scoped provider-specific request fields.
- [ ] **Day 53 (2026-12-12):** Document provider differences and unsupported options.
- [ ] **Day 54 (2026-12-13):** Add concise request and response examples.
- [ ] **Day 55 (2026-12-14):** Expand contract tests for malformed payloads.
- [ ] **Day 56 (2026-12-15):** Review API stability and breaking-change policy.

### Days 57–84: Testing and network reliability

- [ ] **Day 57 (2026-12-16):** Test HTTP errors with mocked responses.
- [ ] **Day 58 (2026-12-17):** Test connection failures without live network calls.
- [ ] **Day 59 (2026-12-18):** Test timeouts and secret-safe error messages.
- [ ] **Day 60 (2026-12-19):** Test malformed JSON responses.
- [ ] **Day 61 (2026-12-20):** Test invalid UTF-8 response bodies.
- [ ] **Day 62 (2026-12-21):** Test empty and truncated responses.
- [ ] **Day 63 (2026-12-22):** Test non-string assistant content.
- [ ] **Day 64 (2026-12-23):** Guard the suite against accidental network access.
- [ ] **Day 65 (2026-12-24):** Create reusable response fixtures.
- [ ] **Day 66 (2026-12-25):** Use subtests for validation edge cases.
- [ ] **Day 67 (2026-12-26):** Run tests across the supported Python matrix.
- [ ] **Day 68 (2026-12-27):** Document retryable and terminal failures.
- [ ] **Day 69 (2026-12-28):** Add an opt-in bounded retry policy.
- [ ] **Day 70 (2026-12-29):** Retry only explicitly selected transient failures.
- [ ] **Day 71 (2026-12-30):** Implement capped exponential backoff.
- [ ] **Day 72 (2026-12-31):** Make jitter injectable for deterministic tests.
- [ ] **Day 73 (2027-01-01):** Honor valid Retry-After values.
- [ ] **Day 74 (2027-01-02):** Ensure ordinary client errors are not retried.
- [ ] **Day 75 (2027-01-03):** Test retry success, exhaustion, and non-retry cases.
- [ ] **Day 76 (2027-01-04):** Define an overall retry timeout budget.
- [ ] **Day 77 (2027-01-05):** Document idempotency risks for retried requests.
- [ ] **Day 78 (2027-01-06):** Classify rate limits without exposing provider data.
- [ ] **Day 79 (2027-01-07):** Expose safe response-header metadata.
- [ ] **Day 80 (2027-01-08):** Capture provider request IDs when available.
- [ ] **Day 81 (2027-01-09):** Add opt-in environment-gated integration tests.
- [ ] **Day 82 (2027-01-10):** Exercise HTTP behavior with a local fake server.
- [ ] **Day 83 (2027-01-11):** Create a reliability checklist for new features.
- [ ] **Day 84 (2027-01-12):** Review resilience behavior and prioritize gaps.

### Days 85–112: Developer experience and CLI

- [ ] **Day 85 (2027-01-13):** Create a minimal command-line entry point.
- [ ] **Day 86 (2027-01-14):** Load CLI settings through shared configuration.
- [ ] **Day 87 (2027-01-15):** Accept prompt input from standard input.
- [ ] **Day 88 (2027-01-16):** Accept a prompt as a command-line argument.
- [ ] **Day 89 (2027-01-17):** Add a model-selection option.
- [ ] **Day 90 (2027-01-18):** Add a timeout option.
- [ ] **Day 91 (2027-01-19):** Support machine-readable JSON output.
- [ ] **Day 92 (2027-01-20):** Define stable CLI exit codes.
- [ ] **Day 93 (2027-01-21):** Keep credentials out of CLI error output.
- [ ] **Day 94 (2027-01-22):** Test CLI arguments, output, and exit codes.
- [ ] **Day 95 (2027-01-23):** Add a single-prompt example.
- [ ] **Day 96 (2027-01-24):** Add an example with a system instruction.
- [ ] **Day 97 (2027-01-25):** Add a multi-turn conversation example.
- [ ] **Day 98 (2027-01-26):** Add a compatible-provider example.
- [ ] **Day 99 (2027-01-27):** Document all environment variables and defaults.
- [ ] **Day 100 (2027-01-28):** Write troubleshooting guidance for connection failures.
- [ ] **Day 101 (2027-01-29):** Add a setup and compatibility FAQ.
- [ ] **Day 102 (2027-01-30):** Publish a concise public API reference.
- [ ] **Day 103 (2027-01-31):** Add only meaningful badges backed by real checks.
- [ ] **Day 104 (2027-02-01):** Configure the installed console-script entry point.
- [ ] **Day 105 (2027-02-02):** Build a distributable package in CI.
- [ ] **Day 106 (2027-02-03):** Test the CLI after package installation.
- [ ] **Day 107 (2027-02-04):** Document common CLI invocations.
- [ ] **Day 108 (2027-02-05):** Run safe credential-free examples as smoke tests.
- [ ] **Day 109 (2027-02-06):** Organize docs into guides and reference sections.
- [ ] **Day 110 (2027-02-07):** Document contribution and review expectations.
- [ ] **Day 111 (2027-02-08):** Add a documentation release checklist.
- [ ] **Day 112 (2027-02-09):** Review onboarding from a clean checkout.

### Days 113–140: Core GPT capabilities

- [ ] **Day 113 (2027-02-10):** Add typed helpers for system, user, and assistant messages.
- [ ] **Day 114 (2027-02-11):** Add a small conversation-history container.
- [ ] **Day 115 (2027-02-12):** Support structured-output request options.
- [ ] **Day 116 (2027-02-13):** Validate JSON-mode responses.
- [ ] **Day 117 (2027-02-14):** Add optional schema validation for structured output.
- [ ] **Day 118 (2027-02-15):** Represent tool-call payloads without executing them.
- [ ] **Day 119 (2027-02-16):** Represent tool results in the response model.
- [ ] **Day 120 (2027-02-17):** Test multi-turn message ordering.
- [ ] **Day 121 (2027-02-18):** Parse token-usage fields from compatible APIs.
- [ ] **Day 122 (2027-02-19):** Add a stable usage data model.
- [ ] **Day 123 (2027-02-20):** Define a configurable token-cost calculator interface.
- [ ] **Day 124 (2027-02-21):** Require explicit pricing inputs rather than stale hard-coded rates.
- [ ] **Day 125 (2027-02-22):** Document cost-estimation assumptions.
- [ ] **Day 126 (2027-02-23):** Design a Server-Sent Events parser.
- [ ] **Day 127 (2027-02-24):** Test SSE chunk boundaries and partial lines.
- [ ] **Day 128 (2027-02-25):** Add a streaming completion method.
- [ ] **Day 129 (2027-02-26):** Handle stream errors and malformed terminal events.
- [ ] **Day 130 (2027-02-27):** Close stream resources on early exit.
- [ ] **Day 131 (2027-02-28):** Add a streaming usage example.
- [ ] **Day 132 (2027-03-01):** Define a bounded tool-call round-trip interface.
- [ ] **Day 133 (2027-03-02):** Support multiple tool definitions per request.
- [ ] **Day 134 (2027-03-03):** Validate tool schemas before sending.
- [ ] **Day 135 (2027-03-04):** Expose response metadata through typed fields.
- [ ] **Day 136 (2027-03-05):** Normalize finish reasons across response modes.
- [ ] **Day 137 (2027-03-06):** Represent refusal and empty-output cases explicitly.
- [ ] **Day 138 (2027-03-07):** Document output limits and truncation behavior.
- [ ] **Day 139 (2027-03-08):** Test capability fallbacks across providers.
- [ ] **Day 140 (2027-03-09):** Review the GPT feature surface for consistency.

### Days 141–168: Provider support and async APIs

- [ ] **Day 141 (2027-03-10):** Define provider profiles without embedding secrets.
- [ ] **Day 142 (2027-03-11):** Support configurable compatible-provider base URLs.
- [ ] **Day 143 (2027-03-12):** Document provider-specific key conventions.
- [ ] **Day 144 (2027-03-13):** Add caller-controlled model aliases.
- [ ] **Day 145 (2027-03-14):** Document known provider capability differences.
- [ ] **Day 146 (2027-03-15):** Create offline provider test doubles.
- [ ] **Day 147 (2027-03-16):** Add a compatible-endpoint setup guide.
- [ ] **Day 148 (2027-03-17):** Isolate provider-specific behavior from the common client.
- [ ] **Day 149 (2027-03-18):** Document async design and dependency trade-offs.
- [ ] **Day 150 (2027-03-19):** Add an optional HTTPX extra.
- [ ] **Day 151 (2027-03-20):** Implement an asynchronous chat-completions client.
- [ ] **Day 152 (2027-03-21):** Test async success paths with mocked transports.
- [ ] **Day 153 (2027-03-22):** Match synchronous error handling in async calls.
- [ ] **Day 154 (2027-03-23):** Validate async timeout behavior.
- [ ] **Day 155 (2027-03-24):** Add bounded async retries.
- [ ] **Day 156 (2027-03-25):** Design cancellation-safe async streaming.
- [ ] **Day 157 (2027-03-26):** Implement async streaming with resource cleanup.
- [ ] **Day 158 (2027-03-27):** Test async chunks, failures, and cancellation.
- [ ] **Day 159 (2027-03-28):** Share request and response types across APIs.
- [ ] **Day 160 (2027-03-29):** Test parity between sync and async behavior.
- [ ] **Day 161 (2027-03-30):** Test concurrent requests for shared-state leakage.
- [ ] **Day 162 (2027-03-31):** Document connection pooling and client lifecycle.
- [ ] **Day 163 (2027-04-01):** Add an async usage example.
- [ ] **Day 164 (2027-04-02):** Ensure cancellation leaves no background tasks.
- [ ] **Day 165 (2027-04-03):** Test async handling of provider rate limits.
- [ ] **Day 166 (2027-04-04):** Document optional dependency installation.
- [ ] **Day 167 (2027-04-05):** Test provider profiles against common contracts.
- [ ] **Day 168 (2027-04-06):** Review async and provider APIs before stabilizing.

### Days 169–196: Persistence, queues, and background work

- [ ] **Day 169 (2027-04-07):** Define a conversation-storage protocol.
- [ ] **Day 170 (2027-04-08):** Design a versioned SQLite conversation schema.
- [ ] **Day 171 (2027-04-09):** Configure explicit persistence database paths.
- [ ] **Day 172 (2027-04-10):** Generate stable conversation IDs.
- [ ] **Day 173 (2027-04-11):** Persist a conversation through the storage interface.
- [ ] **Day 174 (2027-04-12):** Load conversations in message order.
- [ ] **Day 175 (2027-04-13):** Test persistence round trips and missing records.
- [ ] **Day 176 (2027-04-14):** Add schema-version metadata and migrations.
- [ ] **Day 177 (2027-04-15):** Use transactions for multi-step persistence.
- [ ] **Day 178 (2027-04-16):** Define safe concurrent database behavior.
- [ ] **Day 179 (2027-04-17):** Support explicit conversation deletion.
- [ ] **Day 180 (2027-04-18):** Document retention settings and defaults.
- [ ] **Day 181 (2027-04-19):** Document risks of storing prompts and responses.
- [ ] **Day 182 (2027-04-20):** Keep application code independent of SQLite details.
- [ ] **Day 183 (2027-04-21):** Define a queue protocol for long-running tasks.
- [ ] **Day 184 (2027-04-22):** Implement an in-memory queue for deterministic tests.
- [ ] **Day 185 (2027-04-23):** Create task models with IDs and timestamps.
- [ ] **Day 186 (2027-04-24):** Represent queued, running, succeeded, and failed states.
- [ ] **Day 187 (2027-04-25):** Separate worker logic from API handlers.
- [ ] **Day 188 (2027-04-26):** Distinguish retryable and terminal task failures.
- [ ] **Day 189 (2027-04-27):** Add a dead-letter path for exhausted tasks.
- [ ] **Day 190 (2027-04-28):** Prototype a SQLite-backed queue.
- [ ] **Day 191 (2027-04-29):** Test ordering, transitions, and duplicate handling.
- [ ] **Day 192 (2027-04-30):** Add worker concurrency limits.
- [ ] **Day 193 (2027-05-01):** Define backpressure when the queue is full.
- [ ] **Day 194 (2027-05-02):** Add a background-task example with status polling.
- [ ] **Day 195 (2027-05-03):** Document persistence and queue recovery.
- [ ] **Day 196 (2027-05-04):** Review lifecycle, concurrency, and queue failure modes.

### Days 197–224: Embeddings, retrieval, and RAG

- [ ] **Day 197 (2027-05-05):** Define a provider-neutral embeddings protocol.
- [ ] **Day 198 (2027-05-06):** Add an embedding-provider adapter interface.
- [ ] **Day 199 (2027-05-07):** Represent vectors and dimensions explicitly.
- [ ] **Day 200 (2027-05-08):** Define a chunk model with source metadata.
- [ ] **Day 201 (2027-05-09):** Implement deterministic text chunking.
- [ ] **Day 202 (2027-05-10):** Support validated configurable chunk overlap.
- [ ] **Day 203 (2027-05-11):** Preserve source and section metadata.
- [ ] **Day 204 (2027-05-12):** Test chunk boundaries and empty input.
- [ ] **Day 205 (2027-05-13):** Define a document-loader protocol.
- [ ] **Day 206 (2027-05-14):** Add a plain-text loader.
- [ ] **Day 207 (2027-05-15):** Add a Markdown loader that preserves headings.
- [ ] **Day 208 (2027-05-16):** Add an optional PDF loader with scoped dependencies.
- [ ] **Day 209 (2027-05-17):** Test malformed and empty documents.
- [ ] **Day 210 (2027-05-18):** Batch embeddings within provider limits.
- [ ] **Day 211 (2027-05-19):** Add an embedding-cache interface.
- [ ] **Day 212 (2027-05-20):** Define a vector-store protocol.
- [ ] **Day 213 (2027-05-21):** Implement a small exact-search local store.
- [ ] **Day 214 (2027-05-22):** Test cosine similarity and dimension checks.
- [ ] **Day 215 (2027-05-23):** Add top-k retrieval with stable tie-breaking.
- [ ] **Day 216 (2027-05-24):** Support metadata filters.
- [ ] **Day 217 (2027-05-25):** Test retrieval ranking on a deterministic corpus.
- [ ] **Day 218 (2027-05-26):** Build a context formatter with token limits.
- [ ] **Day 219 (2027-05-27):** Represent citations as structured data.
- [ ] **Day 220 (2027-05-28):** Format citations without inventing source details.
- [ ] **Day 221 (2027-05-29):** Test chunk-to-answer citation mapping.
- [ ] **Day 222 (2027-05-30):** Compose loaders, chunking, embeddings, and retrieval.
- [ ] **Day 223 (2027-05-31):** Add a credential-free RAG example.
- [ ] **Day 224 (2027-06-01):** Document retrieval limits and prompt-injection risks.

### Days 225–252: Tool calling and controlled agents

- [ ] **Day 225 (2027-06-02):** Define a typed tool schema and result.
- [ ] **Day 226 (2027-06-03):** Implement a registry for explicitly approved tools.
- [ ] **Day 227 (2027-06-04):** Register callables with declared schemas.
- [ ] **Day 228 (2027-06-05):** Validate arguments against tool schemas.
- [ ] **Day 229 (2027-06-06):** Reject unregistered tool names.
- [ ] **Day 230 (2027-06-07):** Parse JSON arguments with clear errors.
- [ ] **Day 231 (2027-06-08):** Add per-tool execution timeouts.
- [ ] **Day 232 (2027-06-09):** Require allowlisting before any tool executes.
- [ ] **Day 233 (2027-06-10):** Limit tool-result size in model context.
- [ ] **Day 234 (2027-06-11):** Serialize tool results through a safe contract.
- [ ] **Day 235 (2027-06-12):** Test registry, validation, and execution failures.
- [ ] **Day 236 (2027-06-13):** Parse model tool calls into typed objects.
- [ ] **Day 237 (2027-06-14):** Limit tool-loop iterations.
- [ ] **Day 238 (2027-06-15):** Test loop termination and repeated-call protection.
- [ ] **Day 239 (2027-06-16):** Record agent steps as structured trace events.
- [ ] **Day 240 (2027-06-17):** Implement a minimal sequential agent runner.
- [ ] **Day 241 (2027-06-18):** Separate model planning from tool execution.
- [ ] **Day 242 (2027-06-19):** Add per-tool permissions and policy checks.
- [ ] **Day 243 (2027-06-20):** Block dangerous operations by default in examples.
- [ ] **Day 244 (2027-06-21):** Audit tool names and outcomes without logging secrets.
- [ ] **Day 245 (2027-06-22):** Define human approval for consequential tools.
- [ ] **Day 246 (2027-06-23):** Make tool-failure policy explicit.
- [ ] **Day 247 (2027-06-24):** Expose traces for debugging and evaluation.
- [ ] **Day 248 (2027-06-25):** Add a safe arithmetic-tool example.
- [ ] **Day 249 (2027-06-26):** Add a stubbed search-tool example.
- [ ] **Day 250 (2027-06-27):** Test multi-step flows with deterministic model fixtures.
- [ ] **Day 251 (2027-06-28):** Add adversarial prompt-injection cases.
- [ ] **Day 252 (2027-06-29):** Review execution boundaries and residual risks.

### Days 253–280: Security, budgets, and evaluation

- [ ] **Day 253 (2027-06-30):** Write a threat model for clients, documents, tools, and deployments.
- [ ] **Day 254 (2027-07-01):** Audit credential storage and accidental exposure paths.
- [ ] **Day 255 (2027-07-02):** Redact authorization headers and tokens from logs.
- [ ] **Day 256 (2027-07-03):** Validate custom endpoint URLs.
- [ ] **Day 257 (2027-07-04):** Document SSRF risks for user-controlled URLs.
- [ ] **Day 258 (2027-07-05):** Set request and prompt size limits.
- [ ] **Day 259 (2027-07-06):** Limit response bodies and streamed output.
- [ ] **Day 260 (2027-07-07):** Test HTTPS defaults and intentional local HTTP use.
- [ ] **Day 261 (2027-07-08):** Review runtime and development dependencies.
- [ ] **Day 262 (2027-07-09):** Add secret-scanning checks to CI.
- [ ] **Day 263 (2027-07-10):** Minimize CI permissions.
- [ ] **Day 264 (2027-07-11):** Ensure configuration errors never print secrets.
- [ ] **Day 265 (2027-07-12):** Create a prompt-injection regression corpus.
- [ ] **Day 266 (2027-07-13):** Test malicious instructions inside retrieved documents.
- [ ] **Day 267 (2027-07-14):** Document source-trust boundaries.
- [ ] **Day 268 (2027-07-15):** Define an evaluation-dataset schema.
- [ ] **Day 269 (2027-07-16):** Build a deterministic offline evaluation runner.
- [ ] **Day 270 (2027-07-17):** Define an application-specific scoring interface.
- [ ] **Day 271 (2027-07-18):** Document limits of model-based judges.
- [ ] **Day 272 (2027-07-19):** Store a versioned evaluation baseline.
- [ ] **Day 273 (2027-07-20):** Add a CLI for evaluation runs.
- [ ] **Day 274 (2027-07-21):** Generate machine-readable and human-readable reports.
- [ ] **Day 275 (2027-07-22):** Add request, token, and cost ceilings.
- [ ] **Day 276 (2027-07-23):** Enforce token budgets before oversized requests.
- [ ] **Day 277 (2027-07-24):** Document privacy and PII handling.
- [ ] **Day 278 (2027-07-25):** Define retention and deletion expectations.
- [ ] **Day 279 (2027-07-26):** Add a security checklist for tools and data changes.
- [ ] **Day 280 (2027-07-27):** Require tests and security checks before releases.

### Days 281–308: Application API and integrations

- [ ] **Day 281 (2027-07-28):** Create a separate example application.
- [ ] **Day 282 (2027-07-29):** Add FastAPI as an optional dependency.
- [ ] **Day 283 (2027-07-30):** Implement a health endpoint.
- [ ] **Day 284 (2027-07-31):** Implement a typed chat-completion endpoint.
- [ ] **Day 285 (2027-08-01):** Validate request models and payload sizes.
- [ ] **Day 286 (2027-08-02):** Return a stable response schema.
- [ ] **Day 287 (2027-08-03):** Map library errors to safe HTTP statuses.
- [ ] **Day 288 (2027-08-04):** Add optional bearer-token authentication.
- [ ] **Day 289 (2027-08-05):** Limit request size before parsing large bodies.
- [ ] **Day 290 (2027-08-06):** Define a rate-limit interface and local implementation.
- [ ] **Day 291 (2027-08-07):** Configure explicit CORS origins.
- [ ] **Day 292 (2027-08-08):** Test endpoint validation, authentication, and errors.
- [ ] **Day 293 (2027-08-09):** Wrap the client behind an application service.
- [ ] **Day 294 (2027-08-10):** Add streaming HTTP with disconnect handling.
- [ ] **Day 295 (2027-08-11):** Add an endpoint to enqueue long-running jobs.
- [ ] **Day 296 (2027-08-12):** Add a safe job-status endpoint.
- [ ] **Day 297 (2027-08-13):** Add conversation create, retrieve, and delete endpoints.
- [ ] **Day 298 (2027-08-14):** Integrate persistence behind a storage protocol.
- [ ] **Day 299 (2027-08-15):** Expose a RAG retrieval endpoint.
- [ ] **Day 300 (2027-08-16):** Expose tools only through the approved registry.
- [ ] **Day 301 (2027-08-17):** Verify OpenAPI docs and response schemas.
- [ ] **Day 302 (2027-08-18):** Add curl examples for local workflows.
- [ ] **Day 303 (2027-08-19):** Document environment-file handling for the app.
- [ ] **Day 304 (2027-08-20):** Define a webhook interface for external events.
- [ ] **Day 305 (2027-08-21):** Add one bounded adapter behind a protocol.
- [ ] **Day 306 (2027-08-22):** Test webhook signatures or authentication.
- [ ] **Day 307 (2027-08-23):** Add integration-test stubs without live services.
- [ ] **Day 308 (2027-08-24):** Review API boundaries and integration failure behavior.

### Days 309–336: Observability, deployment, and operations

- [ ] **Day 309 (2027-08-25):** Introduce structured logs with stable event names.
- [ ] **Day 310 (2027-08-26):** Add request correlation IDs.
- [ ] **Day 311 (2027-08-27):** Redact credentials and sensitive prompt content.
- [ ] **Day 312 (2027-08-28):** Define a vendor-neutral metrics interface.
- [ ] **Day 313 (2027-08-29):** Measure request latency by outcome.
- [ ] **Day 314 (2027-08-30):** Track returned token usage.
- [ ] **Day 315 (2027-08-31):** Track categorized error rates safely.
- [ ] **Day 316 (2027-09-01):** Test metric emission and secret redaction.
- [ ] **Day 317 (2027-09-02):** Add optional OpenTelemetry support.
- [ ] **Day 318 (2027-09-03):** Trace outbound model requests.
- [ ] **Day 319 (2027-09-04):** Propagate trace context across layers.
- [ ] **Day 320 (2027-09-05):** Separate liveness from readiness checks.
- [ ] **Day 321 (2027-09-06):** Implement graceful shutdown for workers and clients.
- [ ] **Day 322 (2027-09-07):** Create a minimal Dockerfile.
- [ ] **Day 323 (2027-09-08):** Run the container as a non-root user.
- [ ] **Day 324 (2027-09-09):** Use multi-stage builds when useful.
- [ ] **Day 325 (2027-09-10):** Add a container health check.
- [ ] **Day 326 (2027-09-11):** Build and smoke-test the image in CI.
- [ ] **Day 327 (2027-09-12):** Document dependency pinning and updates.
- [ ] **Day 328 (2027-09-13):** Generate an SBOM for release artifacts.
- [ ] **Day 329 (2027-09-14):** Add container vulnerability scanning.
- [ ] **Day 330 (2027-09-15):** Write deployment-neutral configuration guidance.
- [ ] **Day 331 (2027-09-16):** Document secret injection for deployment environments.
- [ ] **Day 332 (2027-09-17):** Create an operations runbook.
- [ ] **Day 333 (2027-09-18):** Define a reproducible load-test harness.
- [ ] **Day 334 (2027-09-19):** Measure throughput and latency baselines.
- [ ] **Day 335 (2027-09-20):** Document persistent-data backup and restore.
- [ ] **Day 336 (2027-09-21):** Review deployability and recovery procedures.

### Days 337–365: Performance, release, and year-end review

- [ ] **Day 337 (2027-09-22):** Benchmark the client with deterministic fake responses.
- [ ] **Day 338 (2027-09-23):** Test bounded concurrency under representative load.
- [ ] **Day 339 (2027-09-24):** Measure queue throughput and recovery.
- [ ] **Day 340 (2027-09-25):** Report p50, p95, and p99 latency.
- [ ] **Day 341 (2027-09-26):** Profile memory for long conversations and streaming.
- [ ] **Day 342 (2027-09-27):** Optimize only measured bottlenecks.
- [ ] **Day 343 (2027-09-28):** Evaluate cache value against correctness and freshness.
- [ ] **Day 344 (2027-09-29):** Define cache keys and invalidation rules.
- [ ] **Day 345 (2027-09-30):** Test cache isolation across models and providers.
- [ ] **Day 346 (2027-10-01):** Run the suite on Python 3.11.
- [ ] **Day 347 (2027-10-02):** Run the suite on Python 3.12.
- [ ] **Day 348 (2027-10-03):** Run the suite on Python 3.13.
- [ ] **Day 349 (2027-10-04):** Add Linux and macOS checks where supported.
- [ ] **Day 350 (2027-10-05):** Verify source and wheel distributions.
- [ ] **Day 351 (2027-10-06):** Apply semantic versioning to the public API.
- [ ] **Day 352 (2027-10-07):** Prepare a changelog for the next minor release.
- [ ] **Day 353 (2027-10-08):** Refresh the quickstart from a clean environment.
- [ ] **Day 354 (2027-10-09):** Write an end-to-end tutorial through deployment.
- [ ] **Day 355 (2027-10-10):** Keep demo data synthetic and secret-free.
- [ ] **Day 356 (2027-10-11):** Run a credential-free demo smoke test.
- [ ] **Day 357 (2027-10-12):** Prepare release notes and migration details.
- [ ] **Day 358 (2027-10-13):** Verify licenses and attributions.
- [ ] **Day 359 (2027-10-14):** Run a final dependency and secret audit.
- [ ] **Day 360 (2027-10-15):** Review public entry points for security issues.
- [ ] **Day 361 (2027-10-16):** Review open issues and deferred work.
- [ ] **Day 362 (2027-10-17):** Publish known limitations and operational caveats.
- [ ] **Day 363 (2027-10-18):** Create a release candidate only after checks pass.
- [ ] **Day 364 (2027-10-19):** Verify release artifact installation and examples.
- [ ] **Day 365 (2027-10-20):** Write a retrospective and define the next roadmap.

## Progress discipline

At the end of a successful run, update the relevant checkbox and progress-log entry with the implementation when practical. Never mark a day complete merely because a task was attempted. If a task is blocked, leave it unchecked and record the exact blocker.