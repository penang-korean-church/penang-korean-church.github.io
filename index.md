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

  <!-- 2026 Annual Theme Verse -->
  <section class="annual-theme">
    <div class="annual-theme-content">
      <p class="annual-theme-label">2026년 연간 주제 말씀</p>
      <h2 class="annual-theme-title">그와 함께 머물기</h2>
      <p class="annual-theme-verse">
        "와서 보아라." 그들이 따라가서, 예수께서 묵고 계시는 곳을 보고,<br>
        그 날을 그와 함께 지냈다.
      </p>
      <p class="annual-theme-reference">요한복음 1:39</p>
    </div>
  </section>

  <!-- Church Introduction Section -->
  <section class="section" style="background-color: var(--color-surface); padding: 2rem; margin: 2rem 0; border-radius: 16px;">
    {% assign current_month = 'now' | date: "%m" %}
    {% if current_month == "12" %}
    <div style="text-align: center; margin-bottom: 1.5rem;">
      <img src="{{ '/assets/images/december-service.jpg' | relative_url }}" alt="페낭한인교회 12월 예배 모습" style="max-width: 100%; border-radius: 12px; box-shadow: 0 4px 12px rgba(15, 30, 60, 0.1);">
    </div>
    {% endif %}
    <div style="text-align: center; max-width: 700px; margin: 0 auto;">
      <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--color-text-main);">하나님을 예배하는 공동체</h3>
      <p style="color: var(--color-text-muted); line-height: 1.8;">
        페낭한인교회는 1994년 설립 이후 말레이시아 페낭에서 복음 안에서 하나 되어 하나님을 예배하고,
        서로 사랑하며, 이 땅을 섬기는 믿음의 공동체입니다.
      </p>
    </div>
  </section>

  <!-- Recent News Section -->
  <section class="section">
    <header class="section-header">
      <h2 class="section-title">소식 & 공지</h2>
      <p class="section-subtitle">최근 교회 소식을 전해드립니다</p>
    </header>

    <div class="card-grid">
      {% for post in site.posts limit:3 %}
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
