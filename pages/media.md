---
title: "미디어"
subtitle: "페낭한인교회 예배 영상"
description: "페낭한인교회 주일예배 영상을 시청하세요"
keywords: "페낭한인교회 예배영상, 주일예배, 설교 영상"
last_modified_at: 2026-02-03
---

<div id="video-container">
  <p>영상을 불러오는 중...</p>
</div>

<script>
const RSS2JSON_API = 'https://api.rss2json.com/v1/api.json?rss_url=';
const YOUTUBE_RSS_URL = 'https://www.youtube.com/feeds/videos.xml?channel_id=UC6YwH5h_BXpT9whr79iQTMw';

async function loadVideos() {
  const container = document.getElementById('video-container');

  try {
    const response = await fetch(RSS2JSON_API + encodeURIComponent(YOUTUBE_RSS_URL));
    const data = await response.json();

    if (data.status !== 'ok' || !data.items || data.items.length === 0) {
      container.innerHTML = '<p>영상을 찾을 수 없습니다.</p>';
      return;
    }

    let html = '<div class="video-grid">';

    data.items.forEach(item => {
      const title = item.title;
      const videoId = item.guid.replace('yt:video:', '');
      const thumbnail = item.thumbnail || `https://i.ytimg.com/vi/${videoId}/hqdefault.jpg`;
      const date = new Date(item.pubDate).toLocaleDateString('ko-KR');

      html += `
        <div class="video-item">
          <a href="https://www.youtube.com/watch?v=${videoId}" target="_blank" rel="noopener noreferrer">
            <img src="${thumbnail}" alt="${title}">
            <div class="video-info">
              <h3>${title}</h3>
              <p>${date}</p>
            </div>
          </a>
        </div>
      `;
    });

    html += '</div>';
    container.innerHTML = html;

  } catch (error) {
    console.error('영상 로드 실패:', error);
    container.innerHTML = `<p>영상을 불러오는데 실패했습니다.</p><p>에러: ${error.message}</p>`;
  }
}

document.addEventListener('DOMContentLoaded', loadVideos);
</script>

<style>
.video-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-lg);
  margin-top: var(--space-lg);
}

@media (max-width: 900px) {
  .video-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .video-grid {
    grid-template-columns: 1fr;
  }
}

.video-item {
  background: var(--color-surface);
  border-radius: var(--radius-medium);
  overflow: hidden;
  box-shadow: var(--shadow-soft);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.video-item:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-medium);
}

.video-item a {
  text-decoration: none;
  color: inherit;
}

.video-item img {
  width: 100%;
  aspect-ratio: 16/9;
  object-fit: cover;
}

.video-info {
  padding: var(--space-md);
}

.video-info h3 {
  font-size: 1rem;
  margin: 0 0 var(--space-xs) 0;
  color: var(--color-text-main);
  line-height: 1.4;
}

.video-info p {
  font-size: 0.85rem;
  color: var(--color-text-muted);
  margin: 0;
}
</style>
