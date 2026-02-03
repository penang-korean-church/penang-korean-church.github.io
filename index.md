---
layout: default
title: "페낭한인교회"
description: "말레이시아 페낭에서 함께 예배하는 한인 교회. 1994년 설립, 주일예배 오전 11시, 예배·교제·사역 안내"
keywords: "페낭한인교회, Penang Korean Church, 말레이시아 한인교회, 페낭 교회, 한인 예배"
last_modified_at: 2026-02-01
---

<!-- Hero Section -->
<section class="hero-fullscreen">
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <h1 class="hero-title">페낭한인교회</h1>
    <p class="hero-tagline">믿음의 첫 걸음이 행복한 교회</p>
    <p class="hero-text">페낭한인교회를 찾아주신 모든 분들을 환영합니다</p>
    <p class="hero-time">일요일 오전 11시 예배로 오세요</p>
    <div class="hero-actions">
      <a href="{{ '/pages/services/' | relative_url }}" class="btn btn-hero-primary">예배 안내</a>
    </div>
  </div>
</section>

<!-- Location Section -->
<section class="section-fullwidth section-white">
  <div class="container">
    <div class="two-column location-grid">
      <div class="column-info-lifehouse">
        <h2 class="location-time">일요일 오전 11시</h2>
        <p class="location-address">598-01-02, Menara Asas, Tanjung Bungah,<br>11200, Penang, Malaysia</p>
        <div class="location-buttons">
          <a href="{{ '/pages/location/' | relative_url }}" class="btn btn-primary">방문 계획하기</a>
          <a href="https://maps.google.com/?q=Menara+Asas,+Tanjung+Bungah,+Penang" target="_blank" class="btn btn-outline">📍 구글맵</a>
        </div>
      </div>
      <div class="column-map">
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3971.543!2d100.2834!3d5.4601!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x304ac38f4b5c3d9d%3A0x5e8f9c0e5d5c5d5c!2sMenara%20Asas%2C%20Tanjung%20Bungah%2C%20Penang!5e0!3m2!1sen!2smy!4v1234567890!5m2!1sen!2smy"
          width="100%"
          height="350"
          style="border:0; border-radius: 12px;"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade">
        </iframe>
      </div>
    </div>
  </div>
</section>

<!-- Annual Theme Section -->
<section class="section-fullwidth section-annual-theme">
  <div class="container">
    <div class="annual-theme-home">
      <p class="annual-theme-label">2026년 연간 주제 말씀</p>
      <h2 class="annual-theme-title">그와 함께 머물기</h2>
      <p class="annual-theme-verse">
        "와서 보아라."<br>그들이 따라가서, 예수께서 묵고 계시는 곳을 보고, 그 날을 그와 함께 지냈다.
      </p>
      <p class="annual-theme-reference">요한복음 1:39</p>
    </div>
  </div>
</section>

<!-- News Section -->
<section class="section-fullwidth section-gray">
  <div class="container">
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
  </div>
</section>

<!-- CTA Section -->
<section class="section-fullwidth section-dark">
  <div class="container">
    <div class="cta-content">
      <h2 class="cta-title">함께 예배드려요</h2>
      <p class="cta-text">페낭한인교회는 여러분을 기다립니다</p>
      <a href="{{ '/pages/location/' | relative_url }}" class="btn btn-hero-primary">방문 계획하기</a>
    </div>
  </div>
</section>
