# 자료실(소그룹 모임 자료) 설계

작성일: 2026-10-17

## 목적

교회 홈페이지에 **자료실** 코너를 신설한다. 1차로 **소그룹(속회) 모임 자료**만 연다.
자료는 파일이 아니라 **텍스트 글**이며, 소식(`_posts`)처럼 마크다운으로 작성해 각 자료가 자기 페이지를 갖는다.
2차로 **일반자료** 분류를 추가할 수 있도록, 분류는 폴더 하나와 데이터 한 줄만 더하면 되는 구조로 만든다.

## 결정 사항

| 항목 | 결정 |
|------|------|
| 자료 형태 | 텍스트 글 (마크다운 본문). 파일 첨부·외부 저장소 연동 없음 |
| 공개 범위 | 누구나 열람 가능 (정적 사이트, 접근 제한 없음) |
| 작성 흐름 | 소식과 동일: md 파일 추가 → 빌드 확인 → 커밋·푸시 |
| 1차 범위 | 소그룹 모임 자료만. 일반자료는 이번에 만들지 않음 |
| 소식과의 분리 | `_posts`와 별개 컬렉션. 소식 목록·홈 카드·RSS에 섞이지 않음 |

## 구조

### 저장

```
_resources/
└── small-group/                 ← 분류 = 폴더
    └── 2026-10-18-john-1-sharing.md
```

파일명은 소식처럼 `YYYY-MM-DD-slug.md`. front matter:

```yaml
---
title: "10월 셋째 주 속회 나눔 자료"
date: 2026-10-18
summary: "요한복음 1장 나눔 질문"
---
```

`category`는 적지 않는다. 폴더 경로에서 분류를 읽는다.

### 분류 정의

`_data/resource_categories.yml`:

```yaml
- slug: small-group
  name: 소그룹 모임 자료
  description: 속회 모임에서 함께 나누는 자료입니다
```

목록 페이지·본문 레이아웃·사이트맵이 모두 이 파일을 참조한다. 일반자료 추가 시 항목 하나와 `_resources/general/` 폴더만 추가한다.

### 주소

| 페이지 | URL |
|--------|-----|
| 자료실 목록 | `/resources/` |
| 자료 본문 | `/resources/small-group/2026-10-18-john-1-sharing/` |

`_config.yml`:

```yaml
collections:
  resources:
    output: true
    permalink: /resources/:path/
defaults:
  - scope: { path: "", type: "resources" }
    values: { layout: "resource" }
```

## 페이지

### 목록 `resources.html`

- `news.html`과 같은 `page-header` + `card-grid` 구성을 재사용한다.
- `_data/resource_categories.yml`을 순회하며 분류마다 섹션(`h2` + 카드 목록)을 만든다. 각 섹션은 해당 폴더의 문서를 `date` 내림차순으로 나열한다.
- 카드: 날짜 · 제목(링크) · summary · "자세히 보기 →".
- 분류가 하나뿐인 지금은 탭을 만들지 않는다. 분류가 늘어나 필요해지면 그때 추가한다.
- 문서가 없는 분류는 "아직 등록된 자료가 없습니다."를 표시한다.

### 본문 `_layouts/resource.html`

`_layouts/post.html`을 바탕으로 만들되:

- `post-category` 자리에 분류 이름(예: 소그룹 모임 자료)을 표시한다. 분류는 `page.path`의 `_resources/` 다음 폴더명을 `_data/resource_categories.yml`에서 찾아 얻는다.
- 하단 "목록으로 돌아가기"는 `/resources/`로 간다.
- 태그 footer는 유지한다(태그가 있을 때만).
- 소식의 하단 고정 섹션(예물·주차 안내)은 넣지 않는다. 자료는 본문만.

### 메뉴 `_includes/header.html`

"사역 & 부서"와 "찾아오시는 길" 사이에 `자료실` → `/resources/` 링크 추가.

### SEO

- `sitemap.xml`: `site.resources` 루프 추가 (changefreq monthly, priority 0.6). `/resources/` 목록 페이지는 기존 Pages 루프에 자동 포함된다.
- `_includes/navigation-schema.html`: 자료실 항목 추가.
- `_includes/breadcrumb-schema.html`: `/resources/` 경로 분기 추가.
- `feed.xml`은 소식 전용으로 두고 건드리지 않는다.

## 소식과의 연결

주보 소식에서 그 주 속회 자료로 링크할 수 있다. 방식은 기존 행사 링크와 동일:

```markdown
## 🏘️ [속회 모임 자료]({{ '/resources/small-group/2026-10-18-john-1-sharing/' | relative_url }})
```

## 작업 범위

| 구분 | 파일 |
|------|------|
| 신규 | `_resources/small-group/` (첫 자료 1건), `_data/resource_categories.yml`, `resources.html`, `_layouts/resource.html` |
| 수정 | `_config.yml`, `_includes/header.html`, `sitemap.xml`, `_includes/navigation-schema.html`, `_includes/breadcrumb-schema.html` |
| 변경 없음 | `assets/css/style.css`(기존 카드·post 스타일 재사용), `feed.xml`, `index.md`, `_posts/` |

첫 자료는 실제 속회 자료 텍스트를 받아 넣는다. 받기 전까지는 예시 문서 1건으로 빌드를 검증하고, 실제 자료로 교체한 뒤 배포한다.

## 검증

1. `bundle exec jekyll build`가 오류 없이 끝난다.
2. 빌드 결과에 `/resources/index.html`과 `/resources/small-group/<slug>/index.html`이 생성된다.
3. 목록 페이지에 자료 카드가 날짜 내림차순으로 나오고, 카드 링크가 본문 페이지로 간다.
4. 본문 페이지 상단에 "소그룹 모임 자료" 분류가 표시되고, 하단 버튼이 `/resources/`로 간다.
5. 헤더 메뉴에 자료실이 보이고 모바일 메뉴에서도 열린다.
6. `/news/` 목록, 홈 카드, `feed.xml`에 자료가 섞이지 않는다.
7. `sitemap.xml`에 자료실 목록과 자료 본문 URL이 포함된다.

## 다음 단계 (이번 범위 아님)

- 일반자료: `_resources/general/` 폴더 + `_data/resource_categories.yml` 항목 추가.
- 분류가 셋 이상 되면 목록 페이지에 탭 또는 앵커 내비게이션 추가.
