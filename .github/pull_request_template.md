## PR Title (Required)

<!--
Squash merge를 사용하므로 PR 제목이 main 브랜치의 최종 커밋 메시지가 됩니다.
아래 규칙을 반드시 지켜주세요 (PR title lint와 동일).
-->

Format:
`<type>(<scope>): <subject>`

- `type`: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`
- `scope`: `core`, `setup`, `auth`, `ci`, `docs`, `infra`, `backend`, `frontend`
- `subject`: 1~72자, 명확하고 간결하게
- Breaking change가 있으면 `!` 사용 가능:
  `feat(core)!: drop legacy token format`

Examples:
- ✅ `fix(auth): reject expired share token`
- ✅ `docs(ci): add PR title examples`
- ❌ `fix: no scope`
- ❌ `feature(auth): wrong type`
- ❌ `fix(auth): this subject is intentionally made far too long to exceed the seventy two character lint rule limit`

---

## Summary

<!-- 이 PR에서 무엇을 왜 변경했는지 3~5줄로 작성하세요 -->

---

## Addition (AI Agent Required)

<!--
AI agent가 아래 3개 섹션을 반드시 채워야 합니다.
- How to Test
- Focus for Review
- Manual Checks
-->

### How to Test

1.
2.
3.

<!-- 실행 가능한 테스트가 없다면 이유를 반드시 작성하세요. -->

### Focus for Review

<!-- 리뷰어가 집중해서 볼 포인트를 작성하세요. -->
<!-- 특별히 없으면 N/A: <reason> 형식으로 작성하세요. -->

### Manual Checks

<!-- 각 항목은 Yes/No 중 하나를 반드시 체크하세요. -->

- [ ] DB migration: Yes (Summary에 운영 리스크/롤백 방식 작성)
- [ ] DB migration: No
- [ ] Security/Permission change: Yes (Summary에 접근 범위 변화 작성)
- [ ] Security/Permission change: No
- [ ] External API/License change: Yes (Summary에 ESV 표기/호출/캐시 정책 작성)
- [ ] External API/License change: No
