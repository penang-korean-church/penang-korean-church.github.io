---
name: event-post
description: 페낭한인교회(pkc1994) 사이트에 포스터·구글폼·고정 기간이 있는 행사/공지 소식 페이지를 별도 포스트로 만드는 절차. 사용자가 "여름성경학교처럼 별도 소식으로 만들어줘", "이 소식도 X일까지 고정되게 해줘", "이미지 하나 프로젝트 홈에 추가했는데 확인해봐", "구글폼 주소는 이거야", "찬양축제/세례/1인 1사역/수련회 소식 새로 만들어줘" 라고 하거나, 포스터 이미지 파일이나 forms.gle 링크를 주면서 소식을 만들라고 하면 반드시 이 스킬을 사용한다. 기존 행사 포스트의 문구 삭제·고정 기간 변경 요청에도 적용된다.
---

# 행사·공지 소식 포스트 만들기

몇 주에 걸쳐 반복 안내되는 행사(찬양축제, 세례, 1인 1사역 모집, 여름성경학교, 수련회)는 주일 소식 안에 넣지 않고 자기 페이지를 가진다. 이유는 두 가지다. 홈 화면에 행사일까지 고정 카드로 노출할 수 있고, 매주 주일 소식에서는 한 줄 링크로 끝낼 수 있다. 사용자가 포스터를 주일 소식에 넣었던 것을 "별도 소식으로 빼고 링크 걸어 달라"고 고친 뒤 자리 잡은 패턴이다.

## 1. 시작 전

- `git fetch && git pull --ff-only`.
- 비슷한 성격의 기존 포스트를 템플릿으로 읽는다: 포스터형 행사는 `_posts/2026-10-18-praise-festival-2026.md`, 신청서형은 `_posts/2026-11-15-thanksgiving-baptism-2026.md`, 모집형은 `_posts/2026-10-25-ministry-recruitment-2027.md`. 작년 같은 행사가 있으면(`ls _posts | grep <keyword>`) 모집 분야 표 같은 긴 내용은 거기서 가져온다.
- 사용자가 이미지를 "프로젝트 홈에 추가했다"고 하면 저장소 루트에서 `ls -t | head` 로 새 파일을 찾는다. jpg/png 원본이 루트에 그대로 있다.

## 2. 파일과 front matter

- 파일명: `_posts/YYYY-MM-DD-<영어 slug>.md`. 날짜는 **행사일**(신청 마감일이 아님). 행사일이 없는 모집 공지는 안내가 시작되는 주일 날짜.
- `category`: 행사면 `"행사"`, 모집·안내면 `"공지"`.
- `pinned_until: YYYY-MM-DD` — 홈 상단에 고정할 마지막 날. 보통 행사일이고, 모집은 사용자가 말한 마감일(예: 11월 30일). `index.md` 가 `site.time` 과 비교해 이 날짜까지 카드를 맨 앞에 두며 최대 3장이므로, 이미 고정된 포스트가 몇 개인지 확인하고 보고한다.
- `image: /assets/images/<slug>-poster.webp` 가 있으면 홈 카드에 썸네일로 쓰인다.
- `summary` 는 검색 결과와 카드에 그대로 나오므로 "교회명 + 행사명 + 일시 + 장소" 를 한 문장에 담는다.
- `date` 가 미래여도 `future: true` 라서 바로 보인다.

## 3. 포스터 이미지

원본은 대개 2~5MB라 그대로 올리지 않는다.

```bash
cwebp -q 82 -resize 1200 0 "<원본>" -o assets/images/<slug>-poster.webp   # 가로 1200px, 세로 비율 유지
# cwebp가 없으면: magick "<원본>" -resize 1200x -quality 82 assets/images/<slug>-poster.webp
git rm --cached -q "<원본>" 2>/dev/null; rm "<원본>"   # 루트의 원본은 저장소에 남기지 않는다
```

본문 마크업은 세로 포스터용 클래스를 쓴다(최대 480px, 가운데 정렬, 잘리지 않음):

```html
<div class="page-hero-image poster">
  <img src="/assets/images/<slug>-poster.webp" alt="포스터에 적힌 핵심 문구를 그대로: 행사명, 일시, 장소">
</div>
```

가로형 사진(단체사진 등)이면 `poster` 클래스를 빼고 일반 `page-hero-image` 를 쓴다.

## 4. 본문 구성

순서: 제목 배너 → 개요 표 → 포스터 → 캘린더 링크 → 신청 버튼 → 안내 문단. 필요 없는 블록은 뺀다.

**배너**(주제 문구가 있을 때):

```html
<div class="annual-theme" style="margin: 2rem 0;">
  <div class="annual-theme-content">
    <h2 class="annual-theme-title">온 맘다해 주 사랑하라!</h2>
    <p class="annual-theme-reference">교회 창립 32주년 전교인 찬양축제</p>
  </div>
</div>
```

성경 구절이나 여러 줄 문구는 `annual-theme-reference` 대신 `<p class="annual-theme-verse">` 에 `<br>` 로 줄을 나눈다.

**개요 표**: `| 항목 | 내용 |` 두 칸 표에 일시·장소·대상·문의. 세례처럼 교육 일정이 여러 회차면 날짜를 전부 적는다("10월 25일(주일)부터 3주간 (10월 25일, 11월 1일, 11월 8일), 오전 10시, 목양실").

**캘린더 링크**: 행사일과 각 교육 회차마다 `weekly-news` 스킬의 `scripts/gcal_link.py` 로 만든다. 여러 개면 `·` 로 이어 한 줄에 둔다.

**구글폼 버튼**: 폼 주소는 행사 포스트에만 둔다. 주일 소식은 이 포스트로 링크한다.

```html
<div style="text-align: center; margin: 1.5rem 0;">
  <a href="https://forms.gle/XXXX" target="_blank" rel="noopener noreferrer" class="btn btn-primary">세례신청서 작성하기</a>
</div>
```

버튼 아래에 오프라인 신청 경로("사역자 또는 속회 인도자에게")를 bullet로 남긴다.

**넣지 않는 것**: 주차 안내 섹션(주일 소식에만 있으면 된다고 사용자가 뺐다), 포스터에 적힌 캠페인 영문 슬로건이나 브랜드 문구(사용자가 "every1 Campaign" 을 빼 달라고 했다). 포스터에 있다고 전부 본문에 옮기지 않는다.

**이름**: 담당자가 평신도면 `장\*훈(집)` 으로 마스킹, 사모·선교사·목사는 그대로.

## 5. 주일 소식과 연결

행사 포스트를 만들었으면 같은 주 주일 소식의 해당 섹션 제목을 링크로 바꾼다:

```markdown
## 🎉 [교회창립 32주년 전교인 찬양 축제]({{ '/news/2026/10/18/praise-festival-2026/' | relative_url }})
```

주일 소식이 아직 없으면 `weekly-news` 스킬이 만들 때 이 경로를 쓰도록 보고에 URL을 명시한다.

## 6. 검증과 보고

```bash
bundle exec jekyll build -q -d <scratchpad>/site
```

확인: 포스트 URL 생성, 홈 카드에서 고정 순서(이 포스트가 앞에 오는지, 3장 제한에 밀리는 기존 고정 포스트가 없는지), 이미지 경로 200(빌드 결과에 webp가 복사됐는지), 폼 링크가 새 창으로 열리는 속성. 포스터는 Playwright로 홈과 포스트 페이지 스크린샷을 한 번 찍어 잘림이 없는지 보면 좋다(스크린샷은 `.playwright-mcp/` 에 저장되므로 확인 후 scratchpad로 옮기고 폴더를 지운다. 커밋에 섞이면 안 된다).

보고: 파일, URL, 고정 종료일, 변환한 이미지 크기, 주일 소식에 건 링크. 커밋은 "커밋 푸시해줘" 라고 할 때만: pull → 포스트·webp·원본 삭제를 `git add` 로 골라 담기 → 한국어 메시지 → push. 이전에 `git rm` 으로 스테이지된 삭제가 다른 커밋에 섞여 들어간 적이 있으니 커밋 전 `git status` 로 스테이지 내용을 본다.
