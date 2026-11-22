/**
 * Theme Toggle
 * Dark/Light mode switcher with system preference support
 */

(function() {
  'use strict';

  // 시스템 테마 가져오기
  function getSystemTheme() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  // 초기 테마 설정
  function initTheme() {
    // localStorage에서 저장된 테마 가져오기
    const savedTheme = localStorage.getItem('theme');

    // 저장된 테마가 있으면 사용, 없으면 시스템 설정 따라가기
    const theme = savedTheme || getSystemTheme();

    // 테마 적용
    document.documentElement.setAttribute('data-theme', theme);

    return theme;
  }

  // 테마 전환 (라이트 ↔ 다크)
  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

    // 테마 변경
    document.documentElement.setAttribute('data-theme', newTheme);

    // localStorage에 저장 (이제부터 시스템 설정 무시)
    localStorage.setItem('theme', newTheme);

    // 아이콘 업데이트
    updateThemeIcon(newTheme);

    return newTheme;
  }

  // 테마 아이콘 업데이트
  function updateThemeIcon(theme) {
    const button = document.querySelector('.theme-toggle');
    if (!button) return;

    // 아이콘은 CSS가 data-theme 값으로 바꾼다. 여기서는 라벨만.
    if (theme === 'dark') {
      button.setAttribute('aria-label', '라이트 모드로 전환');
      button.setAttribute('title', '라이트 모드로 전환');
    } else {
      button.setAttribute('aria-label', '다크 모드로 전환');
      button.setAttribute('title', '다크 모드로 전환');
    }
  }

  // DOM 로드 후 실행
  function init() {
    // 초기 테마 설정
    const currentTheme = initTheme();

    // 버튼이 있으면 아이콘 업데이트
    updateThemeIcon(currentTheme);

    // 버튼 클릭 이벤트
    const button = document.querySelector('.theme-toggle');
    if (button) {
      button.addEventListener('click', toggleTheme);
    }

    // 시스템 테마 변경 감지 (사용자가 수동으로 설정 안 한 경우만)
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      // localStorage에 저장된 값이 없을 때만 시스템 설정 따라가기
      if (!localStorage.getItem('theme')) {
        const newTheme = e.matches ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', newTheme);
        updateThemeIcon(newTheme);
      }
    });
  }

  // DOM 완전 로드 후 이벤트 리스너 등록 (initTheme은 인라인 스크립트에서 이미 실행됨)
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

/**
 * iframe 포커스 표시
 * 크로스오리진 iframe(지도, 영상)에 키보드 포커스가 들어가면 부모 창은 blur 되고
 * :focus 가 iframe 요소에 매치되지 않는 브라우저가 있어, 클래스로 포커스 링을 그린다.
 */
(function() {
  'use strict';
  function mark() {
    var el = document.activeElement;
    if (el && el.tagName === 'IFRAME') el.classList.add('is-focused');
  }
  function clear() {
    document.querySelectorAll('iframe.is-focused').forEach(function(f) { f.classList.remove('is-focused'); });
  }
  window.addEventListener('blur', function() { setTimeout(mark, 0); });
  window.addEventListener('focus', clear);
  document.addEventListener('focusin', function(e) {
    clear();
    if (e.target && e.target.tagName === 'IFRAME') e.target.classList.add('is-focused');
  });
})();
