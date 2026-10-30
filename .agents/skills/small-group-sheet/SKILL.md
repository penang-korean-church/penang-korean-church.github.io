---
name: small-group-sheet
description: 페낭한인교회(pkc1994) 사이트 자료실(_resources/small-group/)에 주간 속회모임 나눔지를 추가하고 그 주 매일성경 해설 영상을 임베드하는 절차. 사용자가 "속회 나눔지 추가해줘", "이게 이번주 속회모임 나눔지야", "나눔지 내용 다시 확인해줘", "유튜브 링크 이거 맞는지 확인해봐" 라고 하거나, 시작 기도·함께 찬양·함께 읽기·함께 나눔·마침 기도 구조의 텍스트를 붙여넣으면 반드시 이 스킬을 사용한다. 자료실에 새 분류(일반자료 등)를 만드는 요청에도 참고한다.
---

# 속회 나눔지 추가하기

자료실은 Jekyll 컬렉션 `_resources/`다. 폴더 이름이 분류이고(`small-group` = 소그룹 모임 자료), 분류 목록은 `_data/resource_categories.yml`, 레이아웃은 `_layouts/resource.html`, 목록 페이지는 `/resources/`. 설계 배경은 `docs/superpowers/specs/2026-10-17-resources-small-group-design.md`.

나눔지는 보통 주일 소식 텍스트와 함께 들어온다. 둘 다 왔으면 나눔지를 먼저 만들어야 주일 소식의 속회인도자 항목에 경로를 넣을 수 있다(`weekly-news` 스킬 참고).

## 1. 파일

- 경로: `_resources/small-group/YYYY-MM-DD-<영어 월>-weekN.md`. 날짜는 속회 주간이 시작하는 **월요일**(주일 소식 날짜 + 1일). 예: 10/25 주일 → `2026-10-26-october-week4.md`.
- 생성되는 URL: `/resources/small-group/2026-10-26-october-week4/`. 주일 소식에서 이 경로를 `relative_url` 로 링크한다.
- front matter는 `title`, `date`, `summary`, `tags` 네 개뿐. `category` 를 넣지 않는다(폴더가 분류를 결정하고, 넣으면 레이아웃이 혼동된다).
- 직전 주 파일을 열어 구조를 맞춘다. 전체 뼈대는 `references/sheet-template.md`.

## 2. 본문

붙여넣은 텍스트를 다섯 섹션에 그대로 나눠 담는다. 문장을 다듬거나 요약하지 않는다. 기도문은 모임에서 소리 내어 읽는 것이라 원문 그대로여야 한다.

1. 🙏 시작 기도 — 기도문은 blockquote(`>`)
2. 🎵 함께 찬양 — 찬양 제목 bullet
3. 📖 함께 읽기 — 본문 범위 bullet (예: `**야고보서 5:14-16**`)
4. 💬 함께 나눔 — 질문을 번호 목록으로, 절 표시 괄호 유지
5. 🙏 중보기도 및 마침 기도 — 보통 `**주기도문**`

붙여넣기가 중간에 잘렸을 수 있다. 질문이 1개뿐이거나 마지막 섹션이 비어 있으면 그 사실을 보고한다. 사용자가 "다시 확인해줘" 라며 재전송하는 경우가 있었다.

주일 소식과 달리 나눔지에는 사람 이름이 거의 없지만, 나오면 같은 규칙으로 마스킹한다(`장\*훈(집)`).

## 3. 해설 영상 찾기

하단에 성서유니온 〈매일성경 오디오 해설〉 재생목록(`PLXD3svvkQBPHews8RDWcGqCDag563R2lr`)의 그 주 영상을 임베드한다. 재생목록 RSS는 404라서 스크립트가 재생목록 페이지를 직접 파싱한다:

```bash
# 본문 날짜(주일)로 찾기 — 제목이 「2026년 10월 25일 | 매일성경」 으로 시작
python3 .agents/skills/small-group-sheet/scripts/find_daily_bible_video.py --date 2026-10-25
# 또는 본문 키워드로
python3 .agents/skills/small-group-sheet/scripts/find_daily_bible_video.py 야고보서 5
```

출력은 `videoId <TAB> URL <TAB> 제목`. 나눔지 본문과 영상 제목의 성경 범위가 겹치는지 눈으로 확인한다(나눔지 5:14-16, 영상 5:13-20 처럼 나눔지가 영상 범위의 일부인 게 정상). 영상은 본문 날짜 당일에 올라오므로 미리 만들 때는 아직 없을 수 있다. 그때는 임베드 블록을 빼고 재생목록 링크 문단만 남긴 뒤, 보고에서 "영상은 X일에 올라오면 추가" 라고 알린다. 사용자가 링크를 직접 주면 그 videoId를 쓰되 날짜·본문이 맞는지 스크립트로 한 번 확인한다.

임베드 형식(`.video-wrapper` 는 16:9 반응형 CSS가 이미 있음):

```html
<div class="video-wrapper">
  <iframe src="https://www.youtube-nocookie.com/embed/EUGpiUhDC3M?list=PLXD3svvkQBPHews8RDWcGqCDag563R2lr" title="매일성경 해설 - 기도와 사랑의 공동체 (야고보서 5:13-20)" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>
</div>
```

`?list=` 를 붙이면 플레이어 안에서 재생목록 다른 날짜로도 넘어갈 수 있어서 사용자가 원했던 "리스트를 걸어달라"는 요구가 충족된다.

## 4. 검증과 보고

```bash
bundle exec jekyll build -q -d <scratchpad>/site
```

확인: `<scratchpad>/site/resources/small-group/<slug>/index.html` 이 생겼는지, `/resources/` 목록에 최신 순으로 올라왔는지, 그리고 나눔지가 `/news/`·홈 카드·`feed.xml` 에 **섞여 들어가지 않았는지**(컬렉션이라 안 섞이는 게 정상이고, 섞이면 front matter에 잘못된 키가 들어간 것).

보고: 파일 경로, 생성 URL, 임베드한 영상 제목·ID, 잘린 섹션 여부. 커밋은 "커밋 푸시해줘" 라고 할 때만 한다(절차는 `weekly-news` 스킬과 같다: pull → 선택 add → 한국어 메시지 + Co-Authored-By → push).

## 새 분류를 추가할 때

`_data/resource_categories.yml` 에 `slug / name / description` 항목을 추가하고 같은 이름의 폴더 `_resources/<slug>/` 를 만들면 목록 페이지와 레이아웃이 자동으로 인식한다. 일반자료(`general`)는 예정된 다음 분류다.
