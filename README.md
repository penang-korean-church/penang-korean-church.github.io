# Penang Korean Church Website

A simple, clean Jekyll website for Penang Korean Church (페낭 한인 교회), designed for GitHub Pages deployment.

## Features

- **Responsive Design**: Mobile-first, works perfectly on all devices
- **Korean Language**: Main content in Korean with an English Info page
- **Clean & Minimal**: Light blue accent colors with a bright, calm design
- **News & Announcements**: Blog posts for church news
- **Sermon Archive**: Collection for sermons with YouTube video embedding
- **Multiple Pages**: About, Services, Ministries, Location, and more

## Project Structure

```
├── _config.yml           # Jekyll configuration
├── _data/
│   └── services.yml      # Worship schedule data
├── _includes/
│   ├── header.html       # Site header
│   └── footer.html       # Site footer
├── _layouts/
│   ├── default.html      # Base layout
│   ├── page.html         # Page layout
│   ├── post.html         # News/announcement layout
│   └── sermon.html       # Sermon layout with video
├── _posts/               # News & announcements
├── sermons/              # Sermon collection
├── pages/                # Static pages
├── assets/css/
│   └── style.css         # Complete styling
├── index.md              # Home page
├── news.html             # News index
└── sermons.html          # Sermons index
```

## Local Development

### Prerequisites

- Ruby 2.7 or higher
- Jekyll 4.0 or higher
- Bundler

### Installation

1. Install dependencies:
```bash
gem install jekyll bundler
```

2. Create a `Gemfile`:
```ruby
source "https://rubygems.org"

gem "jekyll", "~> 4.3"
gem "webrick", "~> 1.8"

group :jekyll_plugins do
  gem "jekyll-feed"
end
```

3. Install gems:
```bash
bundle install
```

4. Run locally:
```bash
bundle exec jekyll serve
```

5. Visit `http://localhost:4000`

## GitHub Pages Deployment

### Option 1: Direct Repository

1. Create a new repository named `username.github.io`
2. Push this code to the repository
3. GitHub Pages will automatically build and deploy
4. Visit `https://username.github.io`

### Option 2: Project Repository

1. Create a new repository (any name)
2. Update `_config.yml`:
```yaml
url: "https://username.github.io"
baseurl: "/repository-name"
```
3. Push to GitHub
4. Enable GitHub Pages in Settings → Pages
5. Select branch: `main` or `master`
6. Visit `https://username.github.io/repository-name`

## Customization

### Update Church Information

1. **Contact Info**: Edit `_includes/footer.html`
2. **About Page**: Edit `pages/about.md`
3. **Service Times**: Edit `_data/services.yml`
4. **Location**: Edit `pages/location.md`

### Add News/Announcements

Create a new file in `_posts/` with format: `YYYY-MM-DD-title.md`

```markdown
---
title: "제목"
date: 2025-12-15
category: "공지"
tags: ["tag1", "tag2"]
summary: "요약"
---

Content here...
```

### Add Sermons

Create a new file in `sermons/` with format: `YYYY-MM-DD-title.md`

```markdown
---
title: "설교 제목"
date: 2025-12-15
preacher: "김은혜 목사"
bible_text: "요한복음 3:16"
youtube_url: "https://www.youtube.com/embed/VIDEO_ID"
summary: "요약"
---

Sermon notes here...
```

### YouTube Video Embedding

Replace `VIDEO_ID` with your actual YouTube video ID:
- Full URL: `https://www.youtube.com/watch?v=VIDEO_ID`
- Embed URL: `https://www.youtube.com/embed/VIDEO_ID`

## Design Customization

Edit `assets/css/style.css` CSS variables:

```css
:root {
  --color-primary: #4fa9ff;        /* Main accent color */
  --color-primary-soft: #e0f0ff;   /* Soft background */
  --color-background: #f5f7fb;     /* Page background */
  /* ... more variables ... */
}
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

This website template is free to use and modify for church purposes.

## Support

For questions or issues, contact:
- Email: info@penangkoreanchurch.org
- Phone: +60 12-345-6789
