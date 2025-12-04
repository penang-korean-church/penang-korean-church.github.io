---
layout: default
title: "페낭한인교회"
description: "말레이시아 페낭에서 함께 예배하는 한인 교회. 1994년 설립, 주일예배 오전 11시, 예배·교제·사역 안내"
keywords: "페낭한인교회, Penang Korean Church, 말레이시아 한인교회, 페낭 교회, 한인 예배"
last_modified_at: 2025-12-04
---

<div class="container">
  <!-- Hero Section -->
  <section class="hero">
    <h1 class="hero-title">페낭에서 함께 예배하는 한인 교회입니다</h1>
    <p class="hero-text">
      말레이시아 페낭에 거주하시는 한인 분들과 여행자들을 환영합니다.
      우리는 복음 안에서 하나 되어 하나님을 예배하고, 서로 사랑하며, 이 땅을 섬기는 공동체입니다.
    </p>
    <div class="hero-actions">
      <a href="{{ '/pages/services/' | relative_url }}" class="btn btn-primary">예배 시간 보기</a>
      <a href="{{ '/pages/location/' | relative_url }}" class="btn btn-ghost">찾아오시는 길</a>
    </div>
  </section>

  <!-- Recent News Section -->
  <section class="section">
    <header class="section-header">
      <h2 class="section-title">소식 & 공지</h2>
      <p class="section-subtitle">최근 교회 소식을 전해드립니다</p>
    </header>

    <div class="card-grid">
      {% assign recent_posts = site.posts | limit: 3 %}
      {% for post in recent_posts %}
      <article class="card">
        <div class="card-meta">
          <span>{{ post.date | date: "%Y년 %m월 %d일" }}</span>
          {% if post.category %}
          <span class="card-category">{{ post.category }}</span>
          {% endif %}
        </div>
        <h3 class="card-title">
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </h3>
        {% if post.summary %}
        <p class="card-summary">{{ post.summary }}</p>
        {% endif %}
        <a href="{{ post.url | relative_url }}" class="card-link">자세히 보기 →</a>
      </article>
      {% endfor %}
    </div>

    <div class="text-center mt-lg">
      <a href="{{ '/news/' | relative_url }}" class="btn btn-ghost">모든 소식 보기</a>
    </div>
  </section>

</div>
