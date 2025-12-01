# 페낭한인교회 웹사이트 (Penang Korean Church Website)

말레이시아 페낭한인교회의 공식 웹사이트입니다. Jekyll 기반으로 제작되었으며 GitHub Pages에 배포됩니다.

**Since 1994** | 말레이시아 페낭에서 함께 예배하는 한인 교회

## 🌐 Live Site

- **Production**: https://aaron-jang.github.io/penang-korean-church/
- **Church Website**: www.pkc1994.modoo.at

## ✨ 주요 기능

- **반응형 디자인**: 모바일 우선, 모든 기기에서 완벽하게 작동
- **한국어 지원**: 한글 콘텐츠 중심
- **깔끔한 디자인**: 하늘색 포인트 컬러의 밝고 차분한 디자인
- **소식 & 공지**: Jekyll 블로그 포스트 기능 활용
- **SEO 최적화**: Open Graph, Twitter Cards, Structured Data 지원
- **소셜 미디어 공유**: 최적화된 이미지 및 메타 태그
- **RSS 피드**: 최신 소식 구독 가능

## 📁 프로젝트 구조

```
├── _config.yml              # Jekyll 설정 및 교회 정보
├── _data/
│   ├── church_info.yml      # 교회 상세 정보
│   ├── services.yml         # 예배 시간표
│   ├── ministries.yml       # 사역 및 부서 정보
│   ├── events.yml           # 행사 일정
│   └── weekly_servers.yml   # 주간 봉사자 명단
├── _includes/
│   ├── header.html          # 사이트 헤더
│   └── footer.html          # 사이트 푸터
├── _layouts/
│   ├── default.html         # 기본 레이아웃 (SEO 메타 태그 포함)
│   ├── page.html            # 페이지 레이아웃
│   └── post.html            # 뉴스/공지 레이아웃
├── _posts/                  # 소식 & 공지사항
│   ├── 2024-12-01-december-events.md
│   ├── 2024-12-20-christmas-service.md
│   └── ...
├── pages/                   # 정적 페이지
│   ├── about.md             # 교회 소개
│   ├── services.md          # 예배 안내
│   ├── ministries.md        # 사역 & 부서
│   └── location.md          # 찾아오시는 길
├── assets/
│   ├── css/
│   │   └── style.css        # 전체 스타일시트
│   └── images/              # 이미지 파일
│       ├── og-image.jpg     # Open Graph 이미지 (1200x630)
│       ├── logo.png         # 교회 로고 (512x512)
│       ├── favicon-32x32.png
│       ├── favicon-16x16.png
│       └── apple-touch-icon.png
├── index.md                 # 홈페이지
├── news.html                # 소식 목록
├── sitemap.xml              # 사이트맵
├── robots.txt               # 검색 엔진 크롤러 설정
└── feed.xml                 # RSS 피드
```

## 🚀 로컬 개발 환경 설정

### 필수 요구사항

- Ruby 2.7 이상
- Jekyll 4.0 이상
- Bundler

### 설치 및 실행

1. **의존성 설치**:
```bash
gem install jekyll bundler
```

2. **Gemfile 생성** (프로젝트 루트에):
```ruby
source "https://rubygems.org"

gem "jekyll", "~> 4.3"
gem "webrick", "~> 1.8"

group :jekyll_plugins do
  gem "jekyll-feed"
end
```

3. **Gem 설치**:
```bash
bundle install
```

4. **로컬 서버 실행**:
```bash
bundle exec jekyll serve
```

5. **브라우저에서 확인**: `http://localhost:4000`

## 📦 GitHub Pages 배포

### 현재 설정 (프로젝트 저장소)

이 프로젝트는 `aaron-jang/penang-korean-church` 저장소로 배포됩니다.

`_config.yml` 설정:
```yaml
url: "https://aaron-jang.github.io"
baseurl: "/penang-korean-church"
```

### 배포 단계

1. **변경사항 커밋**:
```bash
git add .
git commit -m "Update content"
git push origin main
```

2. **GitHub Pages 활성화**:
   - GitHub 저장소 → Settings → Pages
   - Source: `main` 브랜치 선택
   - 1-2분 후 자동 배포

3. **사이트 접속**: https://aaron-jang.github.io/penang-korean-church/

## 🎨 커스터마이징

### 교회 정보 업데이트

- **기본 정보**: `_config.yml` 수정
- **교회 소개**: `pages/about.md` 수정
- **예배 시간**: `pages/services.md` 또는 `_data/services.yml` 수정
- **찾아오시는 길**: `pages/location.md` 수정
- **사역 & 부서**: `pages/ministries.md` 수정

### 소식/공지 추가

`_posts/` 디렉토리에 새 파일 생성: `YYYY-MM-DD-title.md`

```markdown
---
title: "소식 제목"
date: 2024-12-15
category: "공지"
tags: ["태그1", "태그2"]
summary: "간단한 요약"
---

여기에 내용을 작성하세요...
```

### 디자인 변경

`assets/css/style.css`의 CSS 변수 수정:

```css
:root {
  --color-primary: #4fa9ff;        /* 메인 포인트 컬러 */
  --color-primary-soft: #e0f0ff;   /* 부드러운 배경색 */
  --color-background: #f5f7fb;     /* 페이지 배경색 */
  --color-text: #2c3e50;           /* 기본 텍스트 색상 */
  /* ... 더 많은 변수들 ... */
}
```

### 이미지 교체

`assets/images/` 디렉토리의 이미지 교체:

- **og-image.jpg**: 1200x630px (소셜 미디어 공유 이미지)
- **logo.png**: 512x512px (교회 로고)
- **favicon-32x32.png**: 32x32px (파비콘)
- **favicon-16x16.png**: 16x16px (작은 파비콘)
- **apple-touch-icon.png**: 180x180px (iOS 홈 화면 아이콘)

## 🔍 SEO 최적화

### 포함된 SEO 기능

- **메타 태그**: Title, Description, Keywords, Author
- **Open Graph**: Facebook, LinkedIn 등 소셜 미디어 공유 최적화
- **Twitter Cards**: 트위터 공유 최적화
- **Structured Data (JSON-LD)**: Google 검색 결과 리치 스니펫
- **Canonical URL**: 중복 콘텐츠 방지
- **Sitemap.xml**: 검색 엔진 크롤링 지원
- **Robots.txt**: 검색 엔진 크롤러 설정
- **RSS Feed**: 콘텐츠 구독 지원
- **지리적 메타 태그**: 페낭 지역 검색 최적화

### Google Search Console 등록

1. [Google Search Console](https://search.google.com/search-console/) 접속
2. 사이트 URL 추가
3. `sitemap.xml` 제출: `https://aaron-jang.github.io/penang-korean-church/sitemap.xml`

## 📞 교회 정보

- **교회명**: 페낭한인교회 (Penang Korean Church)
- **설립**: 1994년
- **담임목사**: 이충원 목사
- **주소**: 598-01-02, Menara Asas, Tanjung Bungah, 11200, Penang, Malaysia
- **전화**: +60-4-299-7935
- **휴대전화**: +60-17-510-3771
- **이메일**: penangkc1994@naver.com
- **웹사이트**: www.pkc1994.modoo.at

### 주일 예배

- **시간**: 매주 주일 오전 11시
- **장소**: 본당

## 🛠 기술 스택

- **Static Site Generator**: Jekyll 4.3+
- **Hosting**: GitHub Pages
- **Language**: Ruby, Liquid, HTML, CSS, JavaScript
- **Markdown**: kramdown
- **SEO**: Open Graph, Twitter Cards, Schema.org
- **Image Processing**: ImageMagick (로컬 개발용)

## 📱 브라우저 지원

- Chrome (최신 버전)
- Firefox (최신 버전)
- Safari (최신 버전)
- Edge (최신 버전)
- 모바일 브라우저 (iOS Safari, Chrome Mobile)

## 📄 라이선스

이 웹사이트 템플릿은 교회 목적으로 자유롭게 사용 및 수정할 수 있습니다.

## 🤝 기여

문제가 발견되거나 개선 사항이 있으시면 Issue를 등록하거나 Pull Request를 보내주세요.

## 📧 문의

- **이메일**: penangkc1994@naver.com
- **전화**: +60-4-299-7935
- **휴대전화**: +60-17-510-3771

---

**© 2024 페낭한인교회 (Penang Korean Church). All rights reserved.**
